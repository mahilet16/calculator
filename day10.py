

# building up a calculator
import calclogo
logo=calclogo.logo
print(logo)
def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}
def calculation():
    num1=float(input("what is the first number: "))
    for i in operations:
            print(i)
    again=True
    while again:
        operation_symbol=input("pick an oeration from the above:")
        num2=float(input("what is the second number: "))
        calculation_function=operations[operation_symbol]
        first_answer=calculation_function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {first_answer}")
        choose=input(f"Type 'y' to continue calculating with {first_answer}, or type 'n' to start a new calculation: .: ")
        if choose=="y":
            num1=first_answer
        else:
             again==False
             calculation()
calculation()