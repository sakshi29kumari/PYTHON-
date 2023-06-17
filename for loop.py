#loops

'''for i in range(1,21):
    print(i)
    
#WAP to print all even no. from 10 to 20
for i in range(10,20,2):
   print(i)  '''
   
   
   #WAP to print the sum of all even no. and odd no. from 10 to 20  
e=o=0
for i in range(10,21):
   if(i%2==0):
       e=e+i
   else:
       o=o+i
print("sum of even no.=",e)
print("sum of odd no.=",o)
