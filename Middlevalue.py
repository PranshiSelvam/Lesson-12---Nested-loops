num = int(input("Enter a value : "))
t = num
numLen = 0
while t>0:
    numLen = numLen+1
    t = int(t/10)

if numLen >=4:
    numLen = int(numLen/2)
    chk = 0
    while num >0:
        rem = num%10
        if chk == numLen:
            midOne = rem
        elif chk == (numLen - 1): 
            midtwo = rem
        num = int(num/10)
        chk = chk+1
    prod = midOne * midtwo 
    print("\n The product of the middle digits of your numer is" , prod)

else:
    print("Your number is less that 4 digits")