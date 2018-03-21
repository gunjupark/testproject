def rotate(text, key):
    ltxt = list(text)
    for i in range(0,len(text)) :
        if 64<ord(ltxt[i])<91 :
            if ord(ltxt[i])+key >90 :
               ltxt[i] = chr(ord(ltxt[i])+key-26)
            else : ltxt[i] =chr(ord(ltxt[i])+key)
        elif 96<ord(ltxt[i])<123 :
            if ord(ltxt[i]) +key >122 :
                ltxt[i] = chr(ord(ltxt[i])+key-26)
            else : ltxt[i] =chr(ord(ltxt[i])+key)
        text =''
    for i in ltxt :
        text+=i
    return text
