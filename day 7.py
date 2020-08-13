# counting bus system carries people per year

daily_carry = 1200000
yearly_carry = 0
for i in range(365):
    yearly_carry +=daily_carry

print(yearly_carry)
#print(365 * 1200000)