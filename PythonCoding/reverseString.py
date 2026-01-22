def reverseWithSlicing(str):
    return str[::-1]

def reverseWithoutSlicing(str):
    rev=""

    for ch in str:
        rev=ch+rev
    return rev

def reverseWithWhile(str):
    rev=""
    i=len(str)-1
    while(i>=0):
        rev+= str[i]
        i -= 1
    
    return rev

str=input("Enter a string: ")

print("With slicing: ",reverseWithSlicing(str))
print("With for Loop:", reverseWithoutSlicing(str))
print("With while loop:", reverseWithWhile(str))





    

    
