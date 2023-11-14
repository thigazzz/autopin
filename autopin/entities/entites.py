from dataclasses import dataclass


@dataclass
class Image:
    id: int
    topic: str
    src: str
    name: str


@dataclass
class Topic:
    name: str
    url: str
