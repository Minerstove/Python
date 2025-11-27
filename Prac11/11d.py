from oj import Genre, Movie

def classify_movies(movies):
    result = {}
    for g in Genre:
        result[g] = []

    for m in movies:
        result[m.genre].append(m)

    for g in Genre:
        lst = result[g]
        n = len(lst)

        for i in range(n):
            for j in range(0, n - i - 1):
                a = lst[j]
                b = lst[j + 1]

                if a.year > b.year or (a.year == b.year and a.name > b.name):
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]

        result[g] = lst

    return result

assert classify_movies((
    Movie(
        name='Happy Death Day',
        year=2017,
        genre=Genre.HORROR,
    ),
    Movie(
        name="Rosemary's Baby",
        year=1968,
        genre=Genre.HORROR,
    ),
    Movie(
        name='Morbius',
        year=2022,
        genre=Genre.HORROR,
    ),
    Movie(
        name='John Wick',
        year=2014,
        genre=Genre.ACTION,
    ),
    Movie(
        name='Wicked',
        year=2024,
        genre=Genre.FANTASY,
    ),
    Movie(
        name='M3GAN',
        year=2022,
        genre=Genre.HORROR,
    ),
)) == {
    Genre.HORROR: [
        Movie(
            name="Rosemary's Baby",
            year=1968,
            genre=Genre.HORROR,
        ),
        Movie(
            name='Happy Death Day',
            year=2017,
            genre=Genre.HORROR,
        ),
        Movie(
            name='M3GAN',
            year=2022,
            genre=Genre.HORROR,
        ),
        Movie(
            name='Morbius',
            year=2022,
            genre=Genre.HORROR,
        ),
    ],
    Genre.SCIFI: [],
    Genre.COMEDY: [],
    Genre.ACTION: [
        Movie(
            name='John Wick',
            year=2014,
            genre=Genre.ACTION,
        ),
    ],
    Genre.THRILLER: [],
    Genre.DRAMA: [],
    Genre.ROMANCE: [],
    Genre.FANTASY: [
        Movie(
            name='Wicked',
            year=2024,
            genre=Genre.FANTASY,
        ),
    ],
}, classify_movies((
    Movie(
        name='Happy Death Day',
        year=2017,
        genre=Genre.HORROR,
    ),
    Movie(
        name="Rosemary's Baby",
        year=1968,
        genre=Genre.HORROR,
    ),
    Movie(
        name='Morbius',
        year=2022,
        genre=Genre.HORROR,
    ),
    Movie(
        name='John Wick',
        year=2014,
        genre=Genre.ACTION,
    ),
    Movie(
        name='Wicked',
        year=2024,
        genre=Genre.FANTASY,
    ),
    Movie(
        name='M3GAN',
        year=2022,
        genre=Genre.HORROR,
    ),
))

