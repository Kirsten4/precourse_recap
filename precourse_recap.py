name = input("What is your name: ")
student_status = input("Are you a student at CodeClan? (yes/no): ")
student_status = student_status.lower()

if student_status == "yes":
    print(name + " is a student at CodeClan.")
else:
    print(name + " is not a student.")

weeks_of_python = 5
weeks_of_javascript = 5
weeks_of_java = 6

total_study = weeks_of_python + weeks_of_javascript + weeks_of_java
print("Total study time is " + str(total_study) + " weeks.")

study_completed = input("How many weeks of CodeClan have you completed?: ")
if study_completed.isdigit():
    print("Input is valid.")
    study_completed = int(study_completed)
else:
    study_completed = int(input("Input invalid, please provide a number: "))
    
remaining_study = total_study - study_completed
print("You have " + str(remaining_study) + " weeks left at CodeClan")

still_a_student = remaining_study > 0
print("Still a student? " + str(still_a_student) )

while still_a_student:
    remaining_study -= 1
    still_a_student = remaining_study > 0
    print("You now only have " + str(remaining_study) + " weeks left on the course.")

message = "Congratulations you have completed the course!"
print(message.upper())