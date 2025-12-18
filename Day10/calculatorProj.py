def add(a1, a2):
    return a1+a2

def subtraction(s1, s2):
    return s1-s2

def multiply(m1, m2):
    return m1*m2

def divide(d1, d2):
    return d1/d2

operations = {
    "+":add, "-":subtraction, "*":multiply,"/":divide
}
def performCalculations(n1, n2, operation):
    return 

def calculate():
    to_continue = True
    num1 = float(input("Enter the first number.\n"))
    while to_continue:
        operation = input("Enter the operation to perform.\n")
        num2 = float(input("Enter second num.\n"))
        result = operations[operation](num1, num2) 
        print(result)
        continue_operation = input("Type 'yes' to continue operation or 'no' to sstart new operation")
        if continue_operation == 'yes':
            num1 = result
        else:
            to_continue = False
            calculate()

    
        

