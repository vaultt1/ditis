# 9. Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber'slanguage"). 
# That is, double every consonant and place an occurrence of "o" in between. For example,translate("this is fun") should return the string "tothohisos isos fofunon".
# Rule: Double every consonant, place "o" in between.


def translate(text):
    res=''

    for t in text:
        if t not in 'aeiou AEIOU':
            res+=str(t)
            res+='o'    
            res+=str(t)
        else:
            res+=str(t)

    print(res)




def f1():
    text='this is fun'
    translate(text)


f1()