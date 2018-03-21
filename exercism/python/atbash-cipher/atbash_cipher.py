import re

def encode(plain_text):
    res = ''
    cnt = 0
    txt = re.sub('[,. ]','',plain_text.lower())
    for i in range(0,len(txt)) :
        if cnt == 5 : 
            res+=' '
            cnt=0
        if 96<ord(txt[i])<123 :
            res += chr(122-ord(txt[i])+97)
            cnt +=1
        else :
            res += txt[i]
            cnt +=1
    return res


def decode(ciphered_text):
    res =''
    txt = re.sub(' ','',ciphered_text.lower())
    for i in range(0,len(txt)) :
        if 96<ord(txt[i])<123 :
            res += chr(122-ord(txt[i])+97)
        else : res += txt[i]

    return res
