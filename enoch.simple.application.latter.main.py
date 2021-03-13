name=input("whats your name ?? ")
if len(name)<3:
    print("name must atleast 3 letters")
elif len(name) >50:
    print("name must be less than 50 characters")
else:
    print("name looks great")
birth_year=input("input birth year")
age=2021-int(birth_year)
if age<18:
    print("sorry you are not eligible for the application try next year")
elif age>65:
    print("sorry the application for youths")
else:
    print("continue to the next dash")
male=True
female=False
gender=input("enter your gender")
gender=male or female
if male or female:
    print("thats good continue")
else:
    print("gender should always be male or famale")
    print("please try again")
kcpe=True
kcse=True
diploma=True
degree=True
level_of_studies=input("enter your level of studies")
if kcse or degree or diploma :
    print("you attain the level required")
elif kcpe:
    print("please visit the nearest technical college and enroll for a computing course")
    print("sorry for the inconvinience")
    print("try again after you finish your course")
else:
    print("sorry we cannot employ you")
married=True
single=False
maritual_stastus=input("maritual stastus")
if married or single:
    print("you have finished you application")
else:
    print("sorry i dont understand that ")
    print("maritual status should be either single or married")
    print("try again")
