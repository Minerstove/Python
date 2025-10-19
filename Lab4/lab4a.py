def word_mutations(word):
    n = len(word)
    l_word = list(word)
    mutations = set()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    for i in range(n + 1):
        for letter in alphabet:
            mutant1 = "".join(l_word[:i] + [letter] + l_word[i:])
            mutations.add(mutant1)
            
            if i < n:
                temp = list(l_word)
                temp[i] = letter
                mutant2 = "".join(temp)
                mutations.add(mutant2)

    for i in range(n):
        mutant = "".join(l_word[:i] + l_word[i + 1:])
        mutations.add(mutant)

    return mutations

assert word_mutations('off') == {
    'aff', 'aoff', 'bff', 'boff', 'cff', 'coff', 'dff', 'doff', 'eff', 'eoff', 'ff', 'fff', 'foff',
    'gff', 'goff', 'hff', 'hoff', 'iff', 'ioff', 'jff', 'joff', 'kff', 'koff', 'lff', 'loff', 'mff',
    'moff', 'nff', 'noff', 'oaf', 'oaff', 'obf', 'obff', 'ocf', 'ocff', 'odf', 'odff', 'oef', 'oeff',
    'of', 'ofa', 'ofaf', 'ofb', 'ofbf', 'ofc', 'ofcf', 'ofd', 'ofdf', 'ofe', 'ofef', 'off', 'offa',
    'offb', 'offc', 'offd', 'offe', 'offf', 'offg', 'offh', 'offi', 'offj', 'offk', 'offl', 'offm',
    'offn', 'offo', 'offp', 'offq', 'offr', 'offs', 'offt', 'offu', 'offv', 'offw', 'offx', 'offy',
    'offz', 'ofg', 'ofgf', 'ofh', 'ofhf', 'ofi', 'ofif', 'ofj', 'ofjf', 'ofk', 'ofkf', 'ofl', 'oflf',
    'ofm', 'ofmf', 'ofn', 'ofnf', 'ofo', 'ofof', 'ofp', 'ofpf', 'ofq', 'ofqf', 'ofr', 'ofrf', 'ofs',
    'ofsf', 'oft', 'oftf', 'ofu', 'ofuf', 'ofv', 'ofvf', 'ofw', 'ofwf', 'ofx', 'ofxf', 'ofy', 'ofyf',
    'ofz', 'ofzf', 'ogf', 'ogff', 'ohf', 'ohff', 'oif', 'oiff', 'ojf', 'ojff', 'okf', 'okff', 'olf',
    'olff', 'omf', 'omff', 'onf', 'onff', 'oof', 'ooff', 'opf', 'opff', 'oqf', 'oqff', 'orf', 'orff',
    'osf', 'osff', 'otf', 'otff', 'ouf', 'ouff', 'ovf', 'ovff', 'owf', 'owff', 'oxf', 'oxff', 'oyf',
    'oyff', 'ozf', 'ozff', 'pff', 'poff', 'qff', 'qoff', 'rff', 'roff', 'sff', 'soff', 'tff', 'toff',
    'uff', 'uoff', 'vff', 'voff', 'wff', 'woff', 'xff', 'xoff', 'yff', 'yoff', 'zff', 'zoff',
}, word_mutations('off')

# {
#     'aff', 'aoff', 'bff', 'boff', 'cff', 'coff', 'dff', 'doff', 'eff', 'eoff', 'ff', 'fff', 'foff',
#     'gff', 'goff', 'hff', 'hoff', 'iff', 'ioff', 'jff', 'joff', 'kff', 'koff', 'lff', 'loff', 'mff',
#     'moff', 'nff', 'noff', 'oaf', 'oaff', 'obf', 'obff', 'ocf', 'ocff', 'odf', 'odff', 'oef', 'oeff',
#     'of', 'ofa', 'ofaf', 'ofb', 'ofbf', 'ofc', 'ofcf', 'ofd', 'ofdf', 'ofe', 'ofef', 'off', 'offa',
#     'offb', 'offc', 'offd', 'offe', 'offf', 'offg', 'offh', 'offi', 'offj', 'offk', 'offl', 'offm',
#     'offn', 'offo', 'offp', 'offq', 'offr', 'offs', 'offt', 'offu', 'offv', 'offw', 'offx', 'offy',
#     'offz', 'ofg', 'ofgf', 'ofh', 'ofhf', 'ofi', 'ofif', 'ofj', 'ofjf', 'ofk', 'ofkf', 'ofl', 'oflf',
#     'ofm', 'ofmf', 'ofn', 'ofnf', 'ofo', 'ofof', 'ofp', 'ofpf', 'ofq', 'ofqf', 'ofr', 'ofrf', 'ofs',
#     'ofsf', 'oft', 'oftf', 'ofu', 'ofuf', 'ofv', 'ofvf', 'ofw', 'ofwf', 'ofx', 'ofxf', 'ofy', 'ofyf',
#     'ofz', 'ofzf', 'ogf', 'ogff', 'ohf', 'ohff', 'oif', 'oiff', 'ojf', 'ojff', 'okf', 'okff', 'olf',
#     'olff', 'omf', 'omff', 'onf', 'onff', 'oof', 'ooff', 'opf', 'opff', 'oqf', 'oqff', 'orf', 'orff',
#     'osf', 'osff', 'otf', 'otff', 'ouf', 'ouff', 'ovf', 'ovff', 'owf', 'owff', 'oxf', 'oxff', 'oyf',
#     'oyff', 'ozf', 'ozff', 'pff', 'poff', 'qff', 'qoff', 'rff', 'roff', 'sff', 'soff', 'tff', 'toff',
#     'uff', 'uoff', 'vff', 'voff', 'wff', 'woff', 'xff', 'xoff', 'yff', 'yoff', 'zff', 'zoff',
# } - 


