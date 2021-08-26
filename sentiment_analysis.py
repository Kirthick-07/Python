punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
            
            
def strip_punctuation(s):
    s1=s
    for i in punctuation_chars:
        if i in s:
            s1=s1.replace(i,'')
    return s1

def get_pos(stri):
    s=0
    lis=stri.split()
    for i in lis:
        il=i.lower()
        w=strip_punctuation(il)
        if w in positive_words:
            s+=1
    return s

r=open('project_twitter_data.csv','r')
o=r.read()

pos_count=get_pos(o)
print(pos_count)

def get_neg(stri):
    s=0
    lis=stri.split()
    for i in lis:
        il=i.lower()
        w=strip_punctuation(il)
        if w in negative_words:
            s+=1
    return s

neg_count=get_neg(o)
print(neg_count)
