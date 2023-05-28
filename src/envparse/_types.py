import typing as t


Value = str

Transformer = t.Callable[[Value], Value]

ItemKey = str

EnvKey = str


__all__ = [
    "Value",
    "Transformer",
    "ItemKey",
    "EnvKey",
]
