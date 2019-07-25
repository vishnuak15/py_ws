import random as rn
lst = []
for i in range(1,101):
    if i % 3 == 0 and i % 6 == 0 and not i % 9 ==0:
        lst.append(rn.randint(1,1000))
print(lst)