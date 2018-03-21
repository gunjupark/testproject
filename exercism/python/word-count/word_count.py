import re

def word_count(phrase):
    st = re.sub('[,_ .:!@#$%^&*\n\t]',' ',phrase.lower())
    tmp = st.split()
    #dequote function used
    for i in range(0,len(tmp)) :
        if (tmp[i][0] == tmp[i][-1]) and (tmp[i][0] == "'") : 
            tmp[i]=tmp[i][1:-1]
    #dict initialize
    dic ={}
    for i in tmp :
        dic[i] = tmp.count(i)
    return dic


