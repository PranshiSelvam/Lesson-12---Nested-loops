string = input("Enter your word or name : ")
character = input("Enter the letter or character you want to find the count for : ")

i = 0 
count = 0
while(i < len(string)):

    if (string[i] == character): 
        count = count + 1
    
    i = i + 1

print("The total number of times " , character , "has occured is ", count)
