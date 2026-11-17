# Context-Fabric integer sentinel collision reproducer

This reproduces a data loss bug in the `.tf` → `.cfm` → API load path when a
node integer feature contains `-1` as an actual value. It was observed with
`context-fabric==0.5.8` (the version used by Doc4CF when this was recorded).

## Run it

Use Python 3.13 or newer in a clean environment:

```powershell
python -m pip install context-fabric==0.5.8
python reproducers/context-fabric-int-sentinel/reproduce.py
```

The script writes a tiny corpus and its compiled `.cfm` cache to a uniquely
named directory in the system temporary directory. It intentionally leaves
that directory in place so Windows can release memory-mapped files when the
process exits; remove the printed directory after the command finishes if you
do not need it.

## Expected and observed behavior

The TF source declares `repeat` as an integer node feature. Node 1 has the
explicit value `-1`, node 2 has `2`, and node 3 is missing. The source-backed
load returns `-1` for node 1. The first load also emits a warning that the
value collides with the `None` sentinel. A fresh load from the generated CFM
cache returns `None` for node 1 and omits node 1 from the feature's `items()`.

Expected: node 1 remains `-1` after compilation and reload; node 3 remains
`None`.

Observed: both node 1 and node 3 read as `None` after reload, and the real
`-1` value is no longer present in the feature mapping.

The reproducer exits successfully when this collision is observed, and prints
the Context-Fabric version, warning, and both load results.

## Upstream issue draft

**Title:** Integer node value `-1` is lost as the missing-value sentinel in CFM

**Body:**

When compiling a `.tf` node integer feature containing an explicit `-1`,
Context-Fabric warns that the value collides with the `None` sentinel. After a
fresh load from the generated `.cfm`, `Feature.v(node)` returns `None` and
`Feature.items()` omits that node. The source-backed load returns `-1` as
expected, so compilation changes the feature's observable values.

Please preserve the distinction between an explicitly stored `-1` and a
missing feature value, or reject this value at compilation rather than
silently changing it. The attached `reproduce.py` is self-contained and
reproduces this behavior with `context-fabric==0.5.8`.

## Old Babylonian corpus impact

The pinned `Nino-cunei/oldbabylonian` revision
`cd8ffe826a598af4715fd724387d9834ec1300d8` documents `repeat` as “the value n
(unknown) is represented as -1”. In that revision, nodes `50077` and `158822`
have explicit `-1` values. Doc4CF's generated `repeat` feature page therefore
omits those two values after loading the CFM cache. This is a Context-Fabric
representation collision, not evidence that those corpus annotations are
mistakes.
