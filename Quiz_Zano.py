total = 0

numgrade = int(input("Enter number of grades: "))

for i in range(1, numgrade + 1):
    totalgrades = float(input(f"Enter grade {i}: "))
    total += totalgrades
   
avegrade = total / numgrade
   
if avegrade >= 90:
    rank = 'A'
elif avegrade >= 80:
    rank = 'B'
elif avegrade >= 70:
    rank = 'C'
elif avegrade >= 60:
    rank = 'D'
else:
    rank = 'F'
    
print(f"Your average is {avegrade:.2f} and your grade is {rank}")