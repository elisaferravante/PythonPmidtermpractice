print(type(2+3))
print(type(6/2 ))
print(type(2 != 3))
print(2+3)
print(len(["abc", 2]))
a = 2
b=3
c="abc"
print(a)
print(a,b,c)
print(a,b,c,sep="")
print(c*(a-b))
d=c.find("b")
print(d)
print(d and b)
print(d==True)
e=str(a)+str(b)+str(c)+str(d)
print(e)


def extract_b_words(file):
    """
    :param file:
    :return:
    """
    with open(file, 'r') as f:
        words = f.read().split()
        for words in words:
            if len(words) == 3 and words.lower().startswith('b'):
                print(words)



