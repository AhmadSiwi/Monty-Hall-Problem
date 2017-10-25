import random
d = ["sheep","sheep","sheep"]
fixCount = 0
changeCount = 0
fixTrue = 0
changeTrue = 0
for i in range(1000000):
    d[0]="sheep"
    d[1]="sheep"
    d[2]="sheep"
    a = random.randint(0,2)
    d[a] = "car"
    b = random.randint(0,2)
    c=0
    x = [0,1,2]
    random.shuffle(x)
    for i in x:
        if ((i != a)and(i != b)):
            c=i
    change = random.randint(0,1)
    if change == 1:
        if(((b==0)and(c==1))or((b==1)and(c==0))):
            b=2
        elif(((b==0)and(c==2))or((b==2)and(c==0))):
            b=1
        elif(((b==2)and(c==1))or((b==1)and(c==2))):
            b=0
        changeCount += 1
        if d[b] == "car":
            changeTrue += 1
    else:
        fixCount+=1
        if d[b]=="car":
            fixTrue+=1
print(fixTrue/fixCount)
print(changeTrue/changeCount)
