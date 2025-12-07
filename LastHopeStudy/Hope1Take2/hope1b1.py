def process(pokedex, pairs):
    if not pairs:
        return ()
    
    return tuple(
        tuple(
            pokemon.lower()
            for (pokemon, region, power, power2) in pokedex
            if r.lower() == region.lower()
               or power.lower() == p.lower()
               or (power2 is not None and power2.lower() == p.lower())
        )
        for (r, p) in pairs
    )

assert process((
    ('Pikachu', 'Kanto', 'Electric', None),
    ('Dedenne', 'Kalos', 'ELECTRIC', 'Fairy'),
    ('Mimikyu', 'Alola', 'ghost', 'Fairy'),
), (
    ("Kanto", "Electric"),
    ("Kalos", "Ghost"),
)) == (
    ("pikachu", "dedenne"),
    ("dedenne", "mimikyu"),
)
assert process((),()) == (())
    