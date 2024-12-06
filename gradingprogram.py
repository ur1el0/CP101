#Roosc_Zano

pgrades = []
fgrades = []

def cal_ave(mlist):
    if not mlist:
        return 0
    total = sum(mlist)
    return total / len(mlist)
    
num =  int(input("Enter the number of Grades: "))
for i in range(1, num + 1):
    grades = int(input(f"Grades {i}: "))
    if grades > 74:
        pgrades.append(grades)
    else:
        fgrades.append(grades)
pgrade = len(pgrades)
fgrade = len(fgrades)

p_ave = cal_ave(pgrades)
f_ave = cal_ave(fgrades)
o_ave = cal_ave(pgrades + fgrades)

print("\nResults:")
print(f"Number of Passing Marks: {pgrade}")
print(f"Average of Passing Marks: {p_ave:.2f}")
print(f"Average of Failing Marks: {f_ave:.2f}")
print(f"Overall Average: {o_ave:.2f}")

                


        
        
        
        