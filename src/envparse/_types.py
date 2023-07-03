import typing as t


Value = str

Transformer = t.Callable[[Value], t.Any]

ItemKey = str

EnvKey = str


__all__ = [
    "Value",
    "Transformer",
    "ItemKey",
    "EnvKey",
]
