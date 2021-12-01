def bmi_cal(age,height,weight):
    if age <= 16:
        print("Under age")
        return

        bmi = weight / (height * height)
    if bmi < 18.5:
        print("Underweight")
    elif bmi <= 18.5 and bmi < 25.0:
        print("Normal")
    elif bmi <= 25.0 and bmi < 30.0:
        print("Overweight")
    elif bmi <= 30.0:
        print("Obese")
    else:
        print("Nothing")

age = int(input("Enter your age:"))
height = float(input("Enter height:"))
weight = float(input("Enter your weight:"))
bmi_cal(age,height,weight)


