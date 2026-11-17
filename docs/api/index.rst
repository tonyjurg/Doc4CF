Doc4CF API Reference
====================

.. container:: api-intro

   Doc4CF turns a versioned Text-Fabric corpus into a browsable static reference.
   The build starts with measured corpus data: feature metadata, populated node
   types, targets, values, and structural relationships. These measurements can
   be exported as a deterministic JSON inventory without contacting a model.

   Optional context analysis uses that inventory to draft a dataset profile,
   feature families, and relationships. A later site build can combine the
   source corpus with reviewed context and generate descriptions for selected
   features. Model output is validated against known features and observed
   values, cached by its inputs, and kept separate from source metadata. The
   resulting site includes feature pages, corpus structure and text views, a
   knowledge graph, and optional context-review pages.

   The :doc:`architecture overview <architecture>` diagrams this flow and
   explains how the Python modules implement each stage.

Reference for |docs_version|, package version |release|. Choose a tagged release
from the version selector in the sidebar to view the API at that release.

.. container:: api-links

   :doc:`Python API <modules>`
   Package functions, inventory export, and reusable context analysis.

   :doc:`Architecture <architecture>`
   How deterministic corpus measurements, optional enrichment, and generated
   artifacts fit together.

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: API reference

   architecture
   modules

* :ref:`genindex`
* :ref:`modindex`
