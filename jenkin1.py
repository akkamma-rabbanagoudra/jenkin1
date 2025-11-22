import sys

if len(sys.argv) == 3:
    script_name = sys.argv[0]
    name = sys.agrv[1]
    rollno = sys.argv[2]
    print("User provided input values:")
else:
    script_name = sys.argv[0]
    name = "Akku"
    rollno = "101"
    print("No input given - using default values:")

print("Script Name:", script_name)
print("Student Name:", name)
print("Roll Number:", rollno)
