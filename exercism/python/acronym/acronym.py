def abbreviate(words):
    res =''
    words = words.replace(',','').replace('-',' ').upper()
    lst = words.split()
    for i in lst : 
        res += i[0]
    return res
