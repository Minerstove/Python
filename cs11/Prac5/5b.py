def markdown_file_bases(filenames):
    fixed_filenames = []

    for file in filenames:
        if file.endswith(".md"):
            base, _ = file.rsplit(".md", 1)
            fixed_filenames.append(base)
        else:
            pass

    return fixed_filenames

assert markdown_file_bases((
    'hello.md',
    'fromtheoutside.jpg',
    'lol.mdown',
    'lol.amd',
    'md.txt',
    'lol.png.md',
    'lol.png.png',
    'lol.md.md',
    'lol',
    'md.md.md',
    'md.md.lol',
    'lolo.md',
)) == [
    'hello',
    'lol.png',
    'lol.md',
    'md.md',
    'lolo',
], markdown_file_bases((
    'hello.md',
    'fromtheoutside.jpg',
    'lol.mdown',
    'lol.amd',
    'md.txt',
    'lol.png.md',
    'lol.png.png',
    'lol.md.md',
    'lol',
    'md.md.md',
    'md.md.lol',
    'lolo.md',
))



