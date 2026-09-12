print("Welcome To Our Student Management System ")
students = {
        101: {"name": "Rahul", "marks": 85},
        102: {"name": "Amit", "marks": 72},
        103: {"name": "Sneha", "marks": 91}
    }
while True :

    print("Select From the below list")
    print("1. Add Student")
    print("2. Delete Student")
    print("3. Search Student")
    print("4. Update Student Marks")
    print("5. Display All Students")
    print("6. Find Student With Highest Marks")
    print("7. Exit")

    
    choice =input("Select Appropriate Option (1/2/3/4/5/6/7) : ")

    if choice in ['1','2','3','4','5','6','7']:
        try:
            if choice =='1':
                        student_id = int(input("Enter student ID: "))
                        name = input("Enter student name: ")
                        marks = int(input("Enter marks: "))
                        students[student_id] = {
                        "name": name,
                        "marks": marks
                        }
            elif choice =='2':
                    student_id = int(input("Enter student ID: "))    
                    if student_id in students:
                        del students[student_id]
                    else:
                        print("Student not found ")


            elif choice=='3':
                    student_id=int(input("Enter student ID: "))   
                    if student_id in students:
                        print("Name:", students[student_id]["name"])
                        print("Marks:", students[student_id]["marks"])
                    else:
                        print("Student not found")
            elif choice =='4':
                 student_id = int(input("Enter student ID: "))
                 if student_id in students:
                    marks = int(input("Enter new marks: "))
                    students[student_id]["marks"] = marks
                    print("Marks updated successfully")
                    print(students[student_id])
                 else:
                    print("Student not found")
                

            elif choice =='5':
                    print("Displaying All Information Of Student \n",students)
                
            elif choice=='6':
                    highest_mark = 0
                    highest_student = None
                    for key, value in students.items():
                        if value["marks"] > highest_mark:
                            highest_mark = value["marks"]
                            highest_student = value["name"]
                    print("Highest student:", highest_student)
                    print("Marks:", highest_mark)

            elif choice=='7':
                    print("Thank You")
                    break
        except ValueError:
              print("invalid input")            
    else:
        print("invalid input")
 