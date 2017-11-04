import random, string
t=[]
for i in range(5):
    s=''
    for j in range(random.randint(3,10)):
        s=s+random.choice(string.ascii_lowercase)
    print s
    t.append(s)
print t
t.sort()
print t
