from dataclasses import dataclass
from enum import auto, Enum

class FruitKind(Enum):
    ACCESSORY = auto()
    MULTIPLE = auto()
    SIMPLE = auto()
    AGGREGATE = auto()

class Ripeness(Enum):
    UNRIPE = auto()
    RIPE = auto()
    OVERRIPE = auto()

@dataclass
class Fruit:
    name: str
    kind: FruitKind
    ripeness: Ripeness
