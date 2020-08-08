number = int(input("Enter Your Number: "))
i=1
for i in range(1,number+1):
    sps = number-i
    s = ' ' * sps + '*'*(i*2) + ' ' * sps
    print(s)
    print(s)


