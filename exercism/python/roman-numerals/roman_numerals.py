def numeral(number):
    dic = {1000:'M', 900:'CM',500:'D',400:'CD',100:'C',90:'XC', 50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}
    res = ''
    mod = list(dic.keys()) # [1000,900,500,400,100,...]
    for i in sorted(mod)[::-1] :
        if int(number/i)>0 :
            res += int(number/i)*(dic.get(i))
            number -= int(number/i)*i
    return res


