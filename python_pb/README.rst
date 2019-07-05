dazl-pb
=======

Protobuf-generated classes (and type hints) for use with dazl.

This module can be used directly without dazl if all you want are the
Protobuf-generated classes, but it is not explicitly designed with this in
mind.

If you'd like to build this from source, run

```
make wheel
```

Notes

This is not a "normal" Python module in the sense that none of the Python code
checked into Git is actually contained in the source zip. This code is used to
_generate_ a Python library; it is not, itself a Python library.

This bulid is therefore quite a bit more complicated than a usual Python build.
Because this is such a bespoke build, the Poetry/pyproject.toml approach
doesn't really work here, so a virtualenv is created and used as part of the
build instead.
