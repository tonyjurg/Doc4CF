API and build architecture
==========================

Doc4CF has a deterministic data path and optional model-assisted stages. The
source of truth is the selected version of the Text-Fabric corpus; generated
interpretations and descriptions are stored separately and do not replace its
feature metadata.

.. mermaid::
   :caption: Corpus data flow from Text-Fabric files to the generated reference site.
   :name: doc4cf-data-flow
   :zoom:

   flowchart TD
       TF["Versioned .tf corpus"] --> LOAD["Text-Fabric load and measurement"]
       LOAD --> INV["Measured inventory"]
       INV -->|"optional: analyze context"| CTXMODEL["Dataset and feature-family analysis"]
       CTXMODEL -->|"validated JSON with inventory hash"| CTX["Context JSON artifacts<br/>human review before use"]
       TF -->|"loads and profiles corpus directly"| BUILD["Static-site generator"]
       CTX -. "optional reviewed context" .-> BUILD
       BUILD --> PROFILE["Feature and structure pages"]
       BUILD --> GRAPH["Knowledge graph and text views"]
       BUILD -->|"optional: --context-pages"| REVIEW["Context review pages"]
       PROFILE -->|"optional: --markdown"| MD["Doc4TF-inspired Markdown index and feature pages"]
       BUILD -->|"selected features only"| FEATMODEL["Optional feature descriptions"]
       FEATMODEL -->|"schema and evidence validation; cache"| PROFILE

The generator can also build directly from the corpus without exporting an
inventory file first. The inventory is a deterministic snapshot of source
metadata and measured values; context analysis and model descriptions are
optional additions.

Build stages
------------

1. **Load and measure.** :func:`doc4cf.generator.export_inventory` reads
   feature headers and loads corpus data with Text-Fabric. It records source
   identity, node types, populated feature coverage, edge targets, frequent
   values, examples, and a digest of the source files. It makes no model calls.
2. **Analyze optional context.** :func:`doc4cf.context.analyze_context` creates
   an inventory, then runs dataset-level and feature-family analysis as
   separate provider requests. It validates the JSON locally and writes
   versioned context artifacts containing the inventory digest and analysis
   provenance. These artifacts can be reviewed before use.
3. **Generate the site.** :func:`doc4cf.generator.generate` reads the corpus
   and builds feature, structure, text, and graph pages. When matching context
   artifacts are supplied, it can add context pages and enrich selected feature
   descriptions. With no model option, the generated corpus pages remain
   deterministic.

Markdown companion
------------------

Pass ``--markdown`` to write a lightweight Markdown set in
``OUTPUT/markdown/`` alongside the HTML site. It follows Doc4TF's
corpus-index and one-file-per-feature structure, with Doc4CF's measured values
and optional inferred descriptions added to the feature pages. The index uses
short feature descriptions and the two most common values; feature pages carry
the richer measurements and model attribution. This separates quick browsing
from per-feature detail and leaves the format straightforward to extend with
additional calculated summaries and clearly labeled interpretations. Markdown
rendering uses the same build responses and makes no extra model requests. See
the `runtime option guide <https://tonyjurg.github.io/Doc4CF/install-guide.html#runtime-options>`_.

Measured feature associations
-----------------------------

Node-feature pages can show a small, collapsible comparison between the
presence patterns of the current feature and other node features. This is a
deterministic corpus measurement; it does not use a model.

For each node type, Doc4CF treats a feature as present when Text-Fabric returns
an assigned value for a node, and absent when there is no assignment. An
explicit value such as ``0`` is present. Every node of that type contributes
to the comparison, including nodes where neither feature is assigned. The
resulting 2 × 2 contingency table is:

.. list-table:: Binary feature-presence contingency table
   :header-rows: 1

   * -
     - Compared feature present
     - Compared feature absent
   * - Current feature present
     - Both present (a)
     - Current feature only (b)
   * - Current feature absent
     - Compared feature only (c)
     - Both absent (d)

Doc4CF calculates the phi coefficient (the correlation of two binary
variables) from those four counts:

.. code-block:: text

   phi = (a*d - b*c) / sqrt((a+b)(c+d)(a+c)(b+d))

The coefficient ranges from −1 to +1. A positive value means the two features
tend to be present on the same nodes; a negative value means one tends to be
present where the other is absent. Zero indicates no measured binary
association. The feature page also reports the fraction of current-feature
nodes among nodes where the compared feature is present and among nodes where
it is absent, making the missing-data side of each comparison explicit.

Comparisons stay within one node type so, for example, word-level and
phrase-level coverage are not mixed. Constant features are omitted. A pair is
eligible when each feature has at least 10 present and 10 absent nodes of that
type, and the display requires ``abs(phi) >= 0.10``. It shows at most three
positive and two inverse associations per node type. Features with exactly
matching presence masks are grouped into one row, avoiding duplicate entries
for identical coverage patterns. The results describe this corpus snapshot;
they do not imply causation or define a linguistic relationship.

Above the expandable matrix, each feature page also lists up to three of its
strongest positive associations with ``phi >= +0.50`` as a quick summary. The
full matrix remains available for weaker positive associations and inverse
patterns.

In the N1904 snapshot, ``mood`` and ``tense`` have identical presence masks:
they are both assigned on 28,357 word nodes and both absent on the remaining
109,422 word nodes, giving ``phi = +1.00``. On word nodes, ``mood`` and
``case`` have 6,653 jointly present nodes, 72,865 case-only nodes, 21,704
mood-only nodes, and 36,557 nodes where both are absent (``phi ≈ −0.35``).
The latter illustrates why counting only shared assignments misses useful
inverse patterns.

Optional feature enrichment
---------------------------

For each selected feature, the generator sends its measured profile and any
applicable editorial notes or reviewed context to the configured provider.
With ``--targeted-evidence``, a planning request can ask for a small number of
rare-value or representative-example samples; Doc4CF retrieves those samples
locally from Text-Fabric before requesting the final description. It does not
let the provider query the corpus or choose arbitrary files.

Context responses must satisfy the stage schema and local checks. Feature
references must name corpus features, and cited values must occur in the
measured evidence. Truncated and empty responses are rejected. Invalid but
well-formed context JSON may receive bounded correction requests; it is not
accepted until validation passes.

Caching and review
------------------

Model requests are cached by their prompt and input payload, so completed
requests can be reused after an interrupted build. Context-aware builds also
compare the current inventory, context, model, prompt, and evidence mode with
the previous manifest. The context review report identifies descriptions whose
inputs changed and any evidence conflicts flagged by feature analysis. An
inventory digest prevents context artifacts from a different corpus snapshot
from being applied.

The command-line entry point accepts corpus and output paths and exposes the
runtime options documented in the `install guide <https://tonyjurg.github.io/Doc4CF/install-guide.html#runtime-options>`_.

Module map
----------

* :mod:`doc4cf.generator` loads and measures source data, manages provider
  requests, exports inventories, and renders the static site.
* :mod:`doc4cf.context` defines context prompts and schemas, validates model
  responses and saved artifacts, fingerprints inputs, and renders context pages.
* :mod:`doc4cf` exports the primary Python entry points; the command line is
  implemented by :func:`doc4cf.generator.main`.

.. seealso::

   * `Software design <https://tonyjurg.github.io/Doc4CF/software-design.html>`_
     for the package's internal design and output data flow.
   * `Install guide <https://tonyjurg.github.io/Doc4CF/install-guide.html#runtime-options>`_
     for CLI examples and provider configuration.
