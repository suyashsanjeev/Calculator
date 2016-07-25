finNum = 0
prev = 1
prev2 = 1
for i in range (8):
    finNum = prev + prev2
    prev2 = prev
    prev = finNum
print(finNum)
