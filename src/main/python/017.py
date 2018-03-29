
# Problem 013
import math
import fractions

##If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
##
##If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
##
##
##NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
##

def singlenum2word(n):
    if n==1:
        word="one"
    elif n==2:
        word="two"
    elif n==3:
        word="three"
    elif n==4:
        word="four"
    elif n==5:
        word="five"
    elif n==6:
        word="six"
    elif n==7:
        word="seven"
    elif n==8:
        word="eight"
    elif n==9:
        word="nine"
    else:
        word = ""
    return word

def num2word(n): #takes a number and returns that number in word notation
    #note that the maximum size for n is 999
    string=str(n).zfill(3)
    word=""
    if int(string[0])==1:
        word+="one hundred"
    elif int(string[0])==2:
        word+="two hundred"
    elif int(string[0])==3:
        word+="three hundred"
    elif int(string[0])==4:
        word+="four hundred"
    elif int(string[0])==5:
        word+="five hundred"
    elif int(string[0])==6:
        word+="six hundred"
    elif int(string[0])==7:
        word+="seven hundred"
    elif int(string[0])==8:
        word+="eight hundred"
    elif int(string[0])==9:
        word+="nine hundred"
    if int(string[1:3])>=10:
        if len(word)>1:
            word+=" and "
        if int(string[1:3])==10:
            word+="ten"
        elif int(string[1:3])==11:
            word+="eleven"
        elif int(string[1:3])==12:
            word+="twelve"
        elif int(string[1:3])==13:
            word+="thirteen"
        elif int(string[1:3])==14:
            word+="fourteen"
        elif int(string[1:3])==15:
            word+="fifteen"
        elif int(string[1:3])==16:
            word+="sixteen"
        elif int(string[1:3])==17:
            word+="seventeen"
        elif int(string[1:3])==18:
            word+="eighteen"
        elif int(string[1:3])==19:
            word+="nineteen"
        elif int(string[1])==2:
            word+="twenty-"
            if int(string[2])!=0:
                word+=singlenum2word(int(string[2]))
        elif int(string[1])==3:
            word+="thirty-"
            if int(string[2])!=0:
                word+=singlenum2word(int(string[2]))
        elif int(string[1])==4:
            word+="forty-"
            if int(string[2])!=0:
                word+=singlenum2word(int(string[2]))
        elif int(string[1])==5:
            word+="fifty-"
            if int(string[2])!=0:
                word+=singlenum2word(int(string[2]))
        elif int(string[1])==6:
            word+="sixty-"
            if int(string[2])!=0:
                word+=singlenum2word(int(string[2]))
        elif int(string[1])==7:
            word+="seventy-"
            if int(string[2])!=0:
                word+=singlenum2word(int(string[2]))
        elif int(string[1])==8:
            word+="eighty-"
            if int(string[2])!=0:
                word+=singlenum2word(int(string[2]))
        elif int(string[1])==9:
            word+="ninety-"
            if int(string[2])!=0:
                word+=singlenum2word(int(string[2]))
    elif int(string[2:3])>=1:
        word+=" and "+singlenum2word(int(string[2]))
    return word

numlets=0
bigstring=""
for m in range(1,1000):
    string=num2word(m)
    bigstring+=string


redstring=''.join(e for e in bigstring if e.isalnum())
numlets+=len(redstring)
print(string)
##one thousand has 11 letters
numlets+=11
## removing the letters for the 9 extra ands at the beginning
numlets-=27

print(numlets)
