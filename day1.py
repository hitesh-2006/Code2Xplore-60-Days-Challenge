full_name = input("Enter Full Name: ")
email = input("Enter Email ID: ")
mobile = input("Enter Mobile Number: ")
age = int(input("Enter Age: "))

name_valid = True

if full_name.startswith(" ") or full_name.endswith(" "):
    name_valid = False


elif full_name.count(" ") < 1:
    name_valid = False
email_valid = True


if email.count("@") != 1 or email.count(".") < 1:
    email_valid = False

elif email.startswith("@"):
    email_valid = False



mobile_valid = True


if len(mobile) != 10:
    mobile_valid = False

elif not mobile.isdigit():
    mobile_valid = False

elif mobile.startswith("0"):
    mobile_valid = False


age_valid = True

if age < 18 or age > 60:
    age_valid = False


if name_valid and email_valid and mobile_valid and age_valid:
    print("User Profile is VALID")
else:
    print("User Profile is INVALID")
