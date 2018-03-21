import re

def hey(phrase):
    phrase = re.sub("[\t\r\n ]","",phrase)
    if phrase == "" : return "Fine. Be that way!"
    if phrase.isupper() :
        if phrase[-1]=='?' :return "Calm down, I know what I'm doing!"
        else : return "Whoa, chill out!"
    if phrase[-1] is '?' : return "Sure."
    else : return "Whatever."
