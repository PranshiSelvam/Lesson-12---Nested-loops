
def decimal_to_binary(n):
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary  
        n = n // 2  
    return binary if binary else "0"  

decimal_number = float(input("Enter a decimal number: "))

binary_number = decimal_to_binary(decimal_number)
print("The binary representation is:", binary_number)
