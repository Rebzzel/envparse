import os
import typing as t

from ._namespace import Namespace
from ._types import (
    Value,
    Transformer,
    ItemKey,
    EnvKey,
)


class EnvironmentParser:
    def __init__(
        self,
        prefix: str = "",
        prefix_delimiter: str = "_",
    ):
        self.prefix = prefix
        self.prefix_delimiter = prefix_delimiter
        self.items: t.Dict[ItemKey, t.Union[EnvKey, Transformer]] = {}

    def add(
        self,
        key: str,
        transformer: Transformer = str,
    ) -> None:
        item_key = self._make_item_key(key)
        env_key = self._make_env_key(key)
        self.items[item_key] = ( env_key, transformer )

    def parse_env(self) -> Namespace:
        attributes = {}

        for item_key, (env_key, transformer) in self.items.items():
            value = os.getenv(env_key)
            attributes[item_key] = (
                transformer(value) if value else None
            )

        return Namespace(**attributes)

    def _make_item_key(self, key: str) -> ItemKey:
        return key.lower()

    def _make_env_key(self, key: str) -> EnvKey:
        if not self.prefix:
            return key

        return "{}{}{}".format(
            self.prefix,
            self.prefix_delimiter,
            key,
        )


__all__ = ["EnvironmentParser"]
