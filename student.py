student={}
print("welcome to do student result mangement system")
print("1 Add student:  ")
print("2 Enter student score:  ")
print("3 View score:  ")
print("4 Average score for each student:  ")
what=int(input("what do you want to do?: "))


def Add_student():
    user=input("Enter the student number ")
    name=input("enter the student name ")

    if user in student:
        print("student number already exists")

    else:
        student[user]= {"name":name,"subject":{}}
        

def Add_score():
    user = input("Enter the student number: ")

    if user not in student:
        print("student not found")
        return

    while True:
        key = input("Enter the subject (enter stop to finish): ")
        if key.lower() == "stop":
            break

        value = int(input("Enter the score: "))
        student[user]["subject"][key] = value

def view_score():
    for user in student:
        print(f"student number: {user}")
        print(f"student name: {student[user]['name']}")
        for key,value in  student[user]["subject"].items ():
               print(f"{key}:{value}")

       

if what ==1:
     Add_student()
elif what==2:
    Add_score()
elif what ==3:
    view_score()








