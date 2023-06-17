#WAP to input marks of a student and print their grade according to the following

'''marks                  grade
90 to 100              
80 to 90
70 to 80
60 to 70
50 to 60
40 to 50
30 to 40
less than30'''

marks=int(input(enter the marks:))
if(marks>=90 and marks<=100):
    print("A+")
elif(marks>=80 and marks<90):
    print("A")    
elif(marks>=70 and marks<80):
    print("B+")
elif(marks>=60 and marks<70):
    print("B")
elif(marks>=50 and marks<60):
    print("C")    
elif(marks>=40 and marks<50):
    print("D")
elif(marks>30 and marks<40):
    print("E")
else:
    print("fail")