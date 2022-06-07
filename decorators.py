#decorator demonstrate
#adding decorator

def decor_sumTwoNumbers(resultFunction):
    def isNumerEqual(a, b):
        if a == b:
            print("Both numbers are equals!!")
        else:
            print("Numbers are not equal!!")
        return resultFunction(a, b)

    return isNumerEqual

@decor_sumTwoNumbers
def sumTwoNumbers(a, b):
    print("Inside sumTwoNumbers!!")
    return a+b

first_number = int(input("Enter first number:"))
second_number = int(input("Enter second number:"))

#printing addintion of two numbers
print("Addition is:", sumTwoNumbers(first_number, second_number))