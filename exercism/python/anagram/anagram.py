def detect_anagrams(word, candidates):
    if word.isupper() : return []
    srclist = list(word.lower())
    srclist.sort()
    reslist = []
    for i in candidates :
        comlist = list(i.lower())
        comlist.sort()
        if srclist == comlist :
            reslist.append(i)
    return reslist
