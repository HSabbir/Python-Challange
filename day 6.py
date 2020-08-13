f = int(input("Enter free bytes: "))
u = int(input("Enter used bytes: "))


free = f
while True:
    o = int(input("Enter delated bytes: "))
    if o > u:
        print("Wrong Input..Try Again")
        continue
    free = free + o
    u = u -o
    break
while True:
    n = int(input("Enter new file bytes: "))
    if n > free:
        print("Wrong Input..Try Again")
        continue

    free = free - n
    break

print(free)