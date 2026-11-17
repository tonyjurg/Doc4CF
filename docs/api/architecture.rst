API and build architecture
==========================

Doc4CF has a deterministic data path and optional model-assisted stages. The
source of truth is the selected version of the Text-Fabric corpus; generated
interpretations and descriptions are stored separately and do not replace its
feature metadata.

.. mermaid::
   :caption: Corpus data flow from Text-Fabric files to the generated reference site.
   :name: doc4cf-data-flow

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
