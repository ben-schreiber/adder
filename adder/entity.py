from typing import NamedTuple


class EntityMetadata(NamedTuple):
    name: str
    created_on: str
    # TODO


class Entity:

    def __init__(self, name: str) -> None:
        self.name = name

    def create(self, or_replace: bool = False, if_not_exists: bool = False, *args, **kwargs):
        raise NotImplementedError()

    def drop(self):
        raise NotImplementedError()

    def describe(self) -> EntityMetadata:
        raise NotImplementedError()
