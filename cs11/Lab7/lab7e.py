from pasta import Pasta, Station

def process_stations(stations):
    n = len(stations)

    prefix = {
        Pasta.PUTTANESCA: [0] * (n + 1),
        Pasta.ANELLETTI:  [0] * (n + 1),
        Pasta.FAGOTTINI:  [0] * (n + 1),
    }

    for idx, station in enumerate(stations, start=1):

        for p in prefix:
            prefix[p][idx] = prefix[p][idx - 1]

        prefix[station.pasta_type][idx] += station.h

    def query(i, j, pasta_like):
        return prefix[pasta_like][j + 1] - prefix[pasta_like][i]

    return query

# Can use partial sums in the context of differing inputs by separating partial sums for each input.