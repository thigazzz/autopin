from dataclasses import dataclass, field


@dataclass
class Image:
    id: int
    topic: str
    src: str
    name: str


@dataclass
class Topic:
    name: str
    description: str
    url: str = field(init=False)
