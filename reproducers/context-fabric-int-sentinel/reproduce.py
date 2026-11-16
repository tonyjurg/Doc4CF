"""Show an explicit integer -1 becoming None after a CFM reload."""

from importlib.metadata import version
from pathlib import Path
from tempfile import mkdtemp

from cfabric.core import Fabric


def write_fixture(root: Path) -> None:
    files = {
        "otype.tf": """@node
@valueType=str

1\tsign
2-3\ttablet
""",
        "oslots.tf": """@edge
@valueType=int

2-3\t1
""",
        "otext.tf": """@config
@sectionFeatures=book
@sectionTypes=tablet
""",
        "book.tf": """@node
@valueType=str

2-3\tFixture
""",
        "repeat.tf": """@node
@valueType=int
@description=Unknown repeat is encoded as -1

1\t-1
2\t2
""",
    }
    for name, contents in files.items():
        (root / name).write_text(contents, encoding="utf-8")


def main() -> None:
    root = Path(mkdtemp(prefix="cfabric-int-sentinel-"))
    write_fixture(root)

    print(f"context-fabric version: {version('context-fabric')}")
    print(f"fixture directory: {root}")

    # The first load compiles the TF corpus and returns its source values.
    source_api = Fabric(locations=str(root)).load(["repeat"], silent="terse")
    if not source_api:
        raise RuntimeError("Context-Fabric failed to load the fixture.")
    source_value = source_api.F.repeat.v(1)
    print(f"source-backed value at node 1: {source_value!r}")
    print(f"source-backed value at missing node 3: {source_api.F.repeat.v(3)!r}")
    if source_value != -1:
        raise AssertionError(f"Expected source value -1; got {source_value!r}")

    # A fresh Fabric instance takes the compiled CFM path.
    cfm_api = Fabric(locations=str(root)).load(["repeat"], silent="terse")
    if not cfm_api:
        raise RuntimeError("Context-Fabric failed to reload the fixture.")
    feature = cfm_api.F.repeat
    cfm_value = feature.v(1)
    print(f"CFM-backed value at node 1: {cfm_value!r}")
    print(f"CFM-backed value at missing node 3: {feature.v(3)!r}")
    print(f"CFM-backed feature items: {list(feature.items())!r}")

    if cfm_value is None:
        print("REPRODUCED: explicit -1 became indistinguishable from missing data.")
    elif cfm_value == -1:
        print("The -1 value was preserved; this Context-Fabric version may be fixed.")
    else:
        raise AssertionError(f"Unexpected CFM-backed value: {cfm_value!r}")


if __name__ == "__main__":
    main()
