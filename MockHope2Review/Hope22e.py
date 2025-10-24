def enumerate_files_in_order(files):
    files_only = [k for k,v in files.items() if v is None]
    folders_only = [k for k,v in files.items() if v is not None]

    result = []
    for file in sorted(files_only):
        result.append(file)

    for folder in sorted(folders_only):
        subpath = enumerate_files_in_order(files[folder])
        
        for subfile in subpath:
            result.append(f"{folder}/{subfile}")
    
    return result

assert enumerate_files_in_order({
    "cs11": {
        "le": {
            "answers.pdf": None,
            "le.pdf": None,
        },
        "lec1.pdf": None,
        "lec2.pdf": None,
        "lec3.pdf": None,
    },
    "cs11raffle.py": None,
    "cs12": {},
    "higurashi": {
        "readme.md": None,
        "spoilers.txt": None,
    },
    "higurashi.txt": None,
    "readme.md": None,
    "umineko": {
        "spoilers.txt": None,
    },
    "venv": {
        "bin": {
            "activate": None,
        },
    },
}) == [
    "cs11raffle.py",
    "higurashi.txt",
    "readme.md",
    "cs11/lec1.pdf",
    "cs11/lec2.pdf",
    "cs11/lec3.pdf",
    "cs11/le/answers.pdf",
    "cs11/le/le.pdf",
    "higurashi/readme.md",
    "higurashi/spoilers.txt",
    "umineko/spoilers.txt",
    "venv/bin/activate",
], enumerate_files_in_order({
    "cs11": {
        "le": {
            "answers.pdf": None,
            "le.pdf": None,
        },
        "lec1.pdf": None,
        "lec2.pdf": None,
        "lec3.pdf": None,
    },
    "cs11raffle.py": None,
    "cs12": {},
    "higurashi": {
        "readme.md": None,
        "spoilers.txt": None,
    },
    "higurashi.txt": None,
    "readme.md": None,
    "umineko": {
        "spoilers.txt": None,
    },
    "venv": {
        "bin": {
            "activate": None,
        },
    },
})
