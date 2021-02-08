import math
"""unit converter"""
print("welcome to jackline's unit converter")
## ask the user which operation they want to perform ##
operation =input("\n choose the operation you want to perform(reply with a,b,c,d,e) \n a. percent to letter grade \n b. distance to speed \n c. centimeters to meters \n d. shilling to dollar \n e. grams to kilograms \n \n operation number:")
# use if statement to choose among the 5 operation to perform #
if operation =="a":
  print("\n converting percent to letter grade\n")
percent= float(input('enter the percentage:'))
if percent >=70 and percent <100:
   grade="A"

elif percent >=60 and percent<70:
    grade="B"

elif percent>=50 and percent<60:
    grade="C"

elif percent>=40 and percent<50:
        grade="D"

elif percen<=20 and percent<30:
            grade="E"

elif percent>=0 and percent>10:
                grade="F"
else:
        grade=gradeError
        print("your grade:"+grade)
        print("\n thats all",+name+".")

if operation =="b":
    print("\n converting hours to seconds ")
hours=float(input('enter the time in hours'))
print(str(hours)+'hrs='+str(hours*360)+'seconds')

if operation=="c":
    print("\n converting distance to speed")
distance=float(input('enter the distance in kilometers:'))
time=float(input('enter time in hrs'))
print('speed used=' + str (distance/time)+'km/h')

if operation=="d":
    print("\n converting shilling to dollar")
shilling=float(input('enter currency in shilling:'))
print(str(shilling)+'shilling'+str(shilling/107)+'dollar')

if operation=="e":
   print("\nconverting grams to kilograms")
grams=float(input("please enter grams:"))
kilograms=grams/1000
print(kilograms,"kilograms")
































 