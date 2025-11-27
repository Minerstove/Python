from pasta import Pasta, Station

from lab7e import process_stations

def verify(condition: bool, message: str = "verification failed"):
    assert condition, message

get_happiness = process_stations((
    Station(pasta_type=Pasta.PUTTANESCA, h=32),
    Station(pasta_type=Pasta.PUTTANESCA, h=11),
    Station(pasta_type=Pasta.ANELLETTI, h=2),
    Station(pasta_type=Pasta.ANELLETTI, h=3),
    Station(pasta_type=Pasta.FAGOTTINI, h=5),
    Station(pasta_type=Pasta.PUTTANESCA, h=199),
    Station(pasta_type=Pasta.FAGOTTINI, h=5),
))

verify(get_happiness(1, 3, Pasta.PUTTANESCA) == 11)
verify(get_happiness(1, 3, Pasta.ANELLETTI) == 5)
verify(get_happiness(1, 3, Pasta.FAGOTTINI) == 0)
verify(get_happiness(0, 6, Pasta.ANELLETTI) == 5)
verify(get_happiness(0, 6, Pasta.PUTTANESCA) == 242)
