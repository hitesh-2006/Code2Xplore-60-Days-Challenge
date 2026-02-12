

student_id = input("Enter Student ID: ")
email = input("Enter Email ID: ")
password = input("Enter Password: ")
referral = input("Enter Referral Code: ")

valid = 0


if len(student_id) == 7:
    if student_id[0] == 'C' and student_id[1] == 'S' and student_id[2] == 'E':
        if student_id[3] == '-':
            if student_id[4] >= '0' and student_id[4] <= '9':
                if student_id[5] >= '0' and student_id[5] <= '9':
                    if student_id[6] >= '0' and student_id[6] <= '9':
                        valid += 1

if email.count('@') == 1 and email.count('.') >= 1:
    if email[0] != '@' and email[len(email)-1] != '@':
        if email[len(email)-1] == 'u' and email[len(email)-2] == 'd' and email[len(email)-3] == 'e' and email[len(email)-4] == '.':
            valid += 1

if len(password) >= 8:
    if password[0] >= 'A' and password[0] <= 'Z':
        if (password.count('0') or password.count('1') or password.count('2') or
            password.count('3') or password.count('4') or password.count('5') or
            password.count('6') or password.count('7') or password.count('8') or
            password.count('9')):
            valid += 1

if len(referral) == 6:
    if referral[0] == 'R' and referral[1] == 'E' and referral[2] == 'F':
        if referral[3] >= '0' and referral[3] <= '9':
            if referral[4] >= '0' and referral[4] <= '9':
                if referral[5] == '@':
                    valid += 1

if valid == 4:
    print("APPROVED")
else:
    print("REJECTED")
