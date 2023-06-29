print("Enter a five-digit integer:")
number = float(input())
result = 0
if number//100000 > 0 or number%1 > 0 or number // 10000 == 0:
    print ("Invalid number entered. Entered number have not five digits, or not integer")
else: 
    units = number%10
    number = number//10
    dozen = number%10
    number = number//10
    hundreds = number%10
    number = number//10
    thousands = number%10
    number = number//10
    tens_of_thousands = number%10
    number = number//10
    if tens_of_thousands - thousands == 0:
        print("Error, Calculation error is not allowed to divide by zero")
    else:
        result = ((dozen ** units) * hundreds)/(tens_of_thousands - thousands)
        print("Calculation result:", result)