num = int(input("enter the no :"))
rev = 0
while num != 0:
    rev = rev * 10 + num % 10
    num //=10
print(f"reverse of is {rev}")
