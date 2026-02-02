from dataclasses import dataclass
from enum import Enum, auto

class Pasta(Enum):
    PUTTANESCA = auto()
    ANELLETTI = auto()
    FAGOTTINI = auto()

@dataclass
class Station:
    pasta_type: Pasta
    h: int
