s=str(input())
k=['!','@','#','$','%','&','*']
p=['1','2','3','4','5','6','7','8','9','0']
count=0
count2=0
if len(s) > 7:
    for i in range(len(s)):
        if s[i] in k:
            count+=1
    if count >= 1:
        for j in range(len(s)):
            if s[j] in p:
                count2+=1
        if count2 >= 2:
            print('Strong')
        else:
            print('Weak')

    else:
        print('Weak')
else:
    print('Weak')
