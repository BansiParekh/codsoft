a = float(input("Enter a value of a:"))
b = float(input("Enter a value of b:"))

print("1.Addition\n")
print("2.Subtraction\n")
print("3.Multiplication\n")
print("4.Division\n")

choice = input("enter a choice number:")

if choice == '1':
    result = a + b
    print("Result of Addition:",result)
elif choice == '2':
    result = a - b
    print("Result of Subtraction:",result)
elif choice == '3':
    result = a*b
    print("result of multiplication:",result)
elif choice == '4':
    if b != 0:
        result = a / b
        print("result of division:",result)
    else:
        print("zero is invalid number for doing this operation")
else:
    print("invalid operation")