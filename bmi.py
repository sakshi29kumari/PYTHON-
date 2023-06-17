#WAP to print the weight status of a person using bmi as shown in following table:

'''BMI                       Weight Status
below 18.5                Underweight
18.5-24.9                 Normal
25.0-29.9                 Overweight
30.0 and above            Obese

NOTE: To calculate BMI:
    input weight(kg) and height(in m)and then apply formula:
        weight /(height)**2'''

weight=int(input("enter weight in kg:"))
height=float(input("enter height in m:"))
bmi= weight/(height)**2
print("bmi=",bmi)
if(bmi<18.5):
    print("undreweight")
elif(bmi>=18.5 and bmi<=24.9):
    print("normal")
elif(bmi>=25 and bmi<=29.9):
    print("overweight")    
else:
    print("obese")