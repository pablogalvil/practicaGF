def sumar(num1, num2):
    if ((num1.isinteger() or num1.isdecimal()) and (num2.isinteger() or num2.isdecimal())):
        return (num1+num2)
    else:
        print("No son enteros o float")

def restar(num1, num2):
    if ((num1.isinteger() or num1.isdecimal()) and (num2.isinteger() or num2.isdecimal())):
        return (num1-num2)
    else:
        print("No son enteros o float")

def multiplicar(num1, num2):
    if ((num1.isinteger() or num1.isdecimal()) and (num2.isinteger() or num2.isdecimal())):
        i = 1
        resultado = num1
        while (i <= num2):
            resultado = resultado + num1
            i = i + 1
        return (num1)
    else:
        print("No son enteros o float")