from dataclasses import dataclass
from enum import Enum, auto

class Genre(Enum):
    HORROR = auto()
    SCIFI = auto()
    COMEDY = auto()
    ACTION = auto()
    THRILLER = auto()
    DRAMA = auto()
    ROMANCE = auto()
    FANTASY = auto()

@dataclass(frozen=True)
class Movie:
    name: str
    year: int
    genre: Genre
