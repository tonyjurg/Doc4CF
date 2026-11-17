API and build architecture
==========================

Doc4CF separates deterministic corpus measurements from optional model-written
interpretations. The Python API exposes the same core operations used by the
``doc4cf`` command line.

1. :func:`doc4cf.generator.export_inventory` reads a pinned Text-Fabric corpus
   version and exports measured feature profiles as JSON. It does not call a
   model or build HTML.
2. :func:`doc4cf.context.analyze_context` can use a configured provider to draft
   dataset context, feature families, and feature relationships. It validates
   the result against the current inventory and writes reusable JSON artifacts.
3. :func:`doc4cf.generator.generate` creates the static site. It can use those
   context artifacts and generate selected feature descriptions, or run without
   model enrichment for a fully deterministic build.

The command-line entry point accepts corpus and output paths and exposes the
runtime options documented in the `install guide <https://tonyjurg.github.io/Doc4CF/install-guide.html#runtime-options>`_.
Generated model descriptions are kept separate from source metadata. Context
artifacts carry inventory hashes and provenance so a site build can reject
stale inputs and report changes for review.

.. seealso::

   * `Software design <https://tonyjurg.github.io/Doc4CF/software-design.html>`_
     for the package's internal design and output data flow.
   * `Install guide <https://tonyjurg.github.io/Doc4CF/install-guide.html#runtime-options>`_
     for CLI examples and provider configuration.
