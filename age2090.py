# the program will calculate when will you be 100 yr old
yearAge = int(input("What is Your age/Year of birth?"))
isAge = False
isYear = False


if len(str(yearAge)) == 4:
    isYear = True
else:
    isAge = True


if yearAge < 1900 and isYear:
    print("you seem to be the oldest person alive")
    exit()
if yearAge > 2022:
    print("you are not born yet")
    exit()

if isAge:
    yearAge = 2022 - yearAge

print(f"you will be 100 yearold in {yearAge + 100} ")

interestedYear = int(input("Enter the year  you want to know your age in \n"))
print(f"you will be {interestedYear -yearAge} yearold in {interestedYear} ")
