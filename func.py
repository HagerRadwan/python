def add(num1 , num2):
    sum = num1+num2
    return sum
def sub(num1 , num2):
    sum = num1-num2
    return sum
def division(num1,num2):
    if(num2 != 0):
        sum = num1/num2
        return sum
    else:
        print("Math erro")

number1= int(input("Enter first number: "))
number2= int(input("Enter your second number: "))
sum_add =add(number1 , number2)
print("additional result is: " , sum_add)
sum_sub =sub(number1 , number2)
print("subtraction result is: " , sum_sub)
sum_divition =division(number1 , number2)
print("divition result is: " , sum_divition)