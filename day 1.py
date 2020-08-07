## Print Multiplication table

number = int(input("Enter Your Number: "))
for i in range(10):
    print(str(i+1)+' * '+str(number)+' = '+str(number*(i+1)))