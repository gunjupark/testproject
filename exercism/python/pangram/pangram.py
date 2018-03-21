def is_pangram(sentence):
alpha_set = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
    string_set = set(sentence.lower()) - set([0-9. ' _ ])
    return alpha_set == string_set
