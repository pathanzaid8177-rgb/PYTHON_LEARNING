#1.Take a number from the user and print whether it is positive, negative, or zero.
 
num = int(input("Enter any number : ")) 
if (num>0 ):
    print("The Number Is Positive : ",num)
elif (num==0):
    print("The Number Is Zero : ",num)
else:
    print("THe Number Is Negative :",num)        

#2. Take a number and check whether it is even or odd.

num = int(input("Enter any number : ")) 
if(num%2==0):
    print("THE GIVEN NUMBER IS EVEN")
else:
    print("THE GIVEN NUMBER IS ODD")    

#3. Take two numbers and print the greater number.    

num = int(input("Enter FIRST number : ")) 
num2 = int(input("Enter SECOND number : ")) 
if (num> num2):
    print("THE FIRST NUMBER IS GREATER : ",num)
else:
    print("THE SECOND NUMBER IS GREATER : ",num2)    

# 4.Take three numbers and print the largest.    

num = int(input("Enter FIRST number : ")) 
num2 = int(input("Enter SECOND number : ")) 
num3 = int(input("Enter third number : ")) 

if (num>= num2 and num>=num3):
    print("THE FIRST NUMBER IS GREATER : ",num)
elif(num2>=num and num2>=num3):
    print("THE SECOND NUMBER IS GREATER : ",num2)   
else:
    print("THE THIRD NUMBER IS GREATER : ",num3)        

#5. Take a person's age and print:Child if age < 13 ,Teenager if 13–19,Adult if 20+  

age = int(input("ENTER YOUR AGE : "))
if (age < 13):
    print("YOUR A CHILD BOY ")
elif(age>=13 and age <=19 ):
    print("YOUR A TEENAGER ")
else:
    print("ADULT")  
  
#6. Check whether a number is divisible by both 3 and 5.

num = int(input("Enter ANY number : "))
if (num%3==0 and num%5==0):
    print("THE IS NUMBER DIVISIBLE BY BOTH 3 AND 5 ")
else:
    print("NUMBER IS NOT EITHER DIVISIBLE BY 3 OR 5")   

#7. Take a student's marks and print their grade: 90+ → A, 75–89 → B,60–74 → C, 40–59 → D, Below 40 → Fail 

marks = int(input("Enter YOUR  GRADE : "))

if(marks>=90):
    print("A GRADE")
elif(marks>=75 and marks<=89):
    print("B GRADE") 
elif(marks>=40 and marks<=59):
    print("D GRADE")       
elif(marks>=60 and marks<=74):
    print("C GRADE")
elif(marks<40):
    print("FAIL")    
