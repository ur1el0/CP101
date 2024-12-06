#Roosc_Zano

gen_ave = 0

num = int(input("Enter the Number of Grades: "))

for fin in range(1, num + 1):
    grades = int(input(f"Grades {fin}: "))
    gen_ave += grades
    
gen_ave /= grades

qual = True
if gen_ave < 90 or grades < 83:
    qual = False
        
if qual:
    print("Remarks: Qualified")
else:
    print("Remarks: Not Qualified")           
