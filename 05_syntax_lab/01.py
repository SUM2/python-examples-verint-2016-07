

number1 = int(raw_input("Pleas write a number\n"))
for n in range(9):
    number2 = int(raw_input("Pleas write a number\n"))
    if number2 > number1:
        number1 = number2

print number1
