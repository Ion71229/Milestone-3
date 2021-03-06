"""
Your code here
You can delete these comments, but do not change the name of this file
Write your code to expect a terminal of 80 characters wide and 24 rows high
"""
import sys
import gspread
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPE_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPE_CREDS)
SHEET = GSPREAD_CLIENT.open('Student_Information')

STUDENT_NAME = []
STUDENT_ROLL_NUMBER = []
STUDENT_ADDRESS = []
STUDENT_EMAIL = []
STUDENT_AGE = []
STUDENT_MOBILE_NUMBER = []
STUDENT_CLASS = []


class STUDENT_MANAGEMENT_SYSTEM: # All STUDENT 'INFORMATION' IS HERE.

    @staticmethod
    def ADD_STUDENT_INFORMATION(): # THIS FUNCTION HELP TO 'ADD INFORMATION' FOR STUDENT.
        print("ADDING STUDENT INFORMATION : \n")
        print("ENTER STUDENT NAME :", end=" ")# HERE YOU CAN ENTER 'STUDENT NAME'
        NAME = input().upper()
        while not NAME:# THIS IS USED TO CHECK THE EMPTY INPUT
            print("Sorry, Try to Enter The  'STUDENT NAME' Again!")
            print("ENTER STUDENT NAME :", end=" ")
            NAME = input().upper()
        STUDENT_NAME.append(NAME)
        
        while True:#THE 'WHILE TRUE' I USED FOR INTEGER INPUT IF IT IS EMPTY TO RETURN THE FUNCTION
            try:
                print("ENTER STUDENT ROLL NUMBER :", end=" ")#ADD THE STUDENT ROLL NUMBER HERE:
                ROLL_NUMBER = int(input())
                break
            except ValueError:
                print("Please Enter a Valid Number")
        STUDENT_ROLL_NUMBER.append(ROLL_NUMBER)
        
        while True:
            try:
                print("ENTER STUDENT AGE :", end=" ")#ADD THE STUDENT AGE HERE:
                AGE = int(input())
                break
            except ValueError:
                print("Please Enter a Valid Number")
        STUDENT_AGE.append(AGE)

        print("ENTER STUDENT CLASS :", end=" ")#ADD THE STUDENT CLASS HERE:
        CLASS = input().upper()
        while not CLASS:
            print("Sorry, Try to Enter The 'STUDENT CLASS' Again!")
            print("ENTER STUDENT CLASS :", end=" ")
            CLASS = input().upper()
        STUDENT_CLASS.append(CLASS)

        print("ENTER STUDENT E-MAIL ID :", end=" ")#ADD THE STUDENT EMAIL ID HERE:
        EMAIL_ID = input().upper()
        while not EMAIL_ID:
            print("Sorry, Try to Enter The 'STUDENT E-MAIL ID' Again!")
            print("ENTER STUDENT E-MAIL ID :", end=" ")
            EMAIL_ID = input().upper()
        STUDENT_EMAIL.append(EMAIL_ID)

        print("ENTER STUDENT ADDRESS :", end=" ")#ADD THE STUDENT ADDRESS HERE:
        ADDRESS = input().upper()
        while not ADDRESS:
            print("Sorry, Try to Enter The 'ADDRESS' Again!")
            print("ENTER STUDENT ADDRESS :", end=" ")
            ADDRESS = input().upper()
        STUDENT_ADDRESS.append(ADDRESS)

        while True:
            try:
                print("ENTER STUDENT MOBILE NUMBER :", end=" ")#ADD THE STUDENT MOBILE NUMBER HERE:
                MOBILE_NUMBER = int(input())
                break
            except ValueError:
                print("Please Enter a Valid Number")
        STUDENT_MOBILE_NUMBER.append(MOBILE_NUMBER)
        print("\n")
        print("\t STUDENT INFORMATION ADDED SUCCESSFULLY.")
        print("\n")

    @staticmethod
    def DELETE_STUDENT_INFORMATION(): #  THIS FUNCTION HELP TO 'DELETE' DATA OF STUDENT.
        print("DELETING STUDENT INFORMATION : \n")

        if len(STUDENT_NAME) == 0 and len(STUDENT_ROLL_NUMBER) == 0 and len(
            STUDENT_AGE) == 0 and len(STUDENT_CLASS) == 0 and len(
                STUDENT_MOBILE_NUMBER) == 0 and len(
                    STUDENT_ADDRESS) == 0 and len(STUDENT_EMAIL) == 0:
            print("\n")
            print("\t 'PLEASE FILL SOME INFORMATION DON'T KEEP IT EMPTY")
            print("\n")
        else:
            while True:
                try:
                    print("ENTER STUDENT ROLL NUMBER :", end=" ")
                    ROLL_NUMBER = int(input())
                    break
                except ValueError:
                    print("Please Enter a Valid Number")
            LOC = STUDENT_ROLL_NUMBER.index(ROLL_NUMBER)

            STUDENT_ROLL_NUMBER.remove(STUDENT_ROLL_NUMBER[LOC])
            STUDENT_NAME.remove(STUDENT_NAME[LOC])
            STUDENT_MOBILE_NUMBER.remove(STUDENT_MOBILE_NUMBER[LOC])
            STUDENT_AGE.remove(STUDENT_AGE[LOC])
            STUDENT_ADDRESS.remove(STUDENT_ADDRESS[LOC])
            STUDENT_EMAIL.remove(STUDENT_EMAIL[LOC])
            STUDENT_CLASS.remove(STUDENT_CLASS[LOC])

            print("\n")
            print("\t\t STUDENT INFORMATION DELETED SUCCESSFULLY.")
            print("\n")

    @staticmethod
    def UPDATE_STUDENT_INFORMATION():#    THIS FUNCTION HELP TO 'UPDATE' DATA OF STUDENT.
        print("UPDATE STUDENT INFORMATION : \n")

        if len(STUDENT_NAME) == 0 and len(STUDENT_ROLL_NUMBER) == 0 and len(
            STUDENT_AGE) == 0 and len(STUDENT_CLASS) == 0 and len(
                STUDENT_MOBILE_NUMBER) == 0 and len(
                    STUDENT_ADDRESS) == 0 and len(STUDENT_EMAIL) == 0:
            print("\n")
            print("\t\t\t 'PLEASE FILL SOME INFORMATION DON'T KEEP IT EMPTY")
            print("\n")
        else:
            print("ENTER STUDENT ATTRIBUTE YOU WANT TO UPDATE :", end="\n")
            print("NAME, ROLL NUMBER, AGE, MOBILE NR, ADDRESS, EMAIL, CLASS.")
            print("ENTER HERE :", end=" ")
            ATTRIBUTE = input().upper()
            while not ATTRIBUTE:
                print("Sorry, Try to Enter The 'ATTRIBUTE' Again!")
                print("ENTER HERE :", end=" ")
                ATTRIBUTE = input().upper()

            if ATTRIBUTE == 'NAME':
                print("ENTER 'OLD NAME' :", end=" ")
                OLD_NAME = input().upper()
                while not OLD_NAME:
                    print("Sorry, Try to Enter The 'OLD_NAME' Again!")
                    print("ENTER 'OLD NAME' :", end=" ")
                    OLD_NAME = input().upper()
                LOC_NAME = STUDENT_NAME.index(OLD_NAME)

                print("ENTER 'NEW NAME' :", end=" ")
                NEW_NAME = input().upper()
                while not NEW_NAME:
                    print("Sorry, Try to Enter The 'NEW_NAME' Again!")
                    print("ENTER 'NEW NAME' :", end=" ")
                    NEW_NAME = input().upper()
                STUDENT_NAME[LOC_NAME] = NEW_NAME
                print("\t 'NAME UPDATED SUCCESSFULLY.")
                print("\n")

            elif ATTRIBUTE == 'ROLL NUMBER':
                while True:
                    try:
                        print("ENTER 'OLD ROLL NUMBER' :", end=" ")
                        OLD_ROLL_NUMBER = int(input())
                        break
                    except ValueError:
                        print("Please Enter a Valid 'OLD ROLL NUMBER'")
                LOC_ROLL = STUDENT_ROLL_NUMBER.index(OLD_ROLL_NUMBER)

                while True:
                    try:
                        print("ENTER 'NEW ROLL NUMBER' :", end=" ")
                        NEW_ROLL = int(input())
                        break
                    except ValueError:
                        print("Please Enter a Valid 'NEW ROLL NUMBER'")
                STUDENT_ROLL_NUMBER[LOC_ROLL] = NEW_ROLL
                print("\t 'ROLL NUMBER UPDATED SUCCESSFULLY.")
                print("\n")

            elif ATTRIBUTE == 'AGE':
                while True:
                    try:
                        print("ENTER 'OLD AGE' :", end=" ")
                        OLD_AGE = int(input())
                        break
                    except ValueError:
                        print("Please Enter a Valid 'OLD AGE'")
                LOC_ROLL = STUDENT_AGE.index(OLD_AGE)

                while True:
                    try:
                        print("ENTER 'NEW AGE' :", end=" ")
                        NEW_AGE = int(input())
                        break
                    except ValueError:
                        print("Please Enter a Valid 'NEW AGE'")
                STUDENT_AGE[LOC_ROLL] = NEW_AGE
                print("\t 'AGE UPDATED SUCCESSFULLY.")
                print("\n")

            elif ATTRIBUTE == 'ADDRESS':
                print("ENTER 'OLD ADDRESS' :", end=" ")
                OLD_ADDRESS = input()
                while not OLD_ADDRESS:
                    print("Sorry, Try to Enter The 'OLD_ADDRESS' Again!")
                    print("ENTER 'OLD ADDRESS' :", end=" ")
                    OLD_ADDRESS = input()
                LOC_ADDRESS = STUDENT_ADDRESS.index(OLD_ADDRESS)

                print("ENTER 'NEW ADDRESS' :", end=" ")
                NEW_ADDRESS = input()
                while not NEW_ADDRESS:
                    print("Sorry, Try to Enter The 'NEW_ADDRESS' Again!")
                    print("ENTER 'NEW ADDRESS' :", end=" ")
                    NEW_ADDRESS = input()
                STUDENT_ADDRESS[LOC_ADDRESS] = NEW_ADDRESS
                print("\t 'ADDRESS UPDATED SUCCESSFULLY.")
                print("\n")

            elif ATTRIBUTE == 'EMAIL':
                print("ENTER 'OLD EMAIL' :", end=" ")
                OLD_EMAIL = input()
                while not OLD_EMAIL:
                    print("Sorry, Try to Enter The 'OLD_EMAIL' Again!")
                    print("ENTER 'OLD EMAIL' :", end=" ")
                    OLD_EMAIL = input()
                LOC_EMAIL = STUDENT_EMAIL.index(OLD_EMAIL)

                print("ENTER 'NEW EMAIL' :", end=" ")
                NEW_EMAIL = input()
                while not NEW_EMAIL:
                    print("Sorry, Try to Enter The 'NEW_EMAIL' Again!")
                    print("ENTER 'NEW EMAIL' :", end=" ")
                    NEW_EMAIL = input()
                STUDENT_EMAIL[LOC_EMAIL] = NEW_EMAIL
                print("\t 'EMAIL - ID UPDATED SUCCESSFULLY.")
                print("\n")

            elif ATTRIBUTE == 'CLASS':
                print("ENTER 'OLD CLASS' :", end=" ")
                OLD_CLASS = input()
                while not OLD_CLASS:
                    print("Sorry, Try to Enter The 'OLD_CLASS' Again!")
                    print("ENTER 'OLD CLASS' :", end=" ")
                    OLD_CLASS = input()
                LOC_CLASS = STUDENT_CLASS.index(OLD_CLASS)

                print("ENTER 'NEW CLASS' :", end=" ")
                NEW_CLASS = input()
                while not NEW_CLASS:
                    print("Sorry, Try to Enter The 'NEW_CLASS' Again!")
                    print("ENTER 'NEW CLASS' :", end=" ")
                    NEW_CLASS = input()
                STUDENT_CLASS[LOC_CLASS] = NEW_CLASS
                print("\t 'CLASS UPDATED SUCCESSFULLY.")
                print("\n")

            elif ATTRIBUTE == 'MOBILE NUMBER':
                while True:
                    try:
                        print("ENTER 'OLD MOBILE NUMBER' :", end=" ")
                        OLD_MOBILE = int(input())
                        break
                    except ValueError:
                        print("Please Enter a Valid 'OLD MOBILE NUMBER'")
                LOC_MOBILE = STUDENT_MOBILE_NUMBER.index(OLD_MOBILE)

                while True:
                    try:
                        print("ENTER 'NEW MOBILE NUMBER' :", end=" ")
                        NEW_MOBILE = int(input())
                        break
                    except ValueError:
                        print("Please Enter a Valid 'NEW MOBILE NUMBER'")
                STUDENT_MOBILE_NUMBER[LOC_MOBILE] = NEW_MOBILE
                print("\t 'MOBILE NUMBER UPDATED SUCCESSFULLY.")
                print("\n")

    @staticmethod
    def DISPLAY_STUDENT_INFORMATION():#    THIS FUNCTION HELP TO 'DISPLAY' DATA OF STUDENT.
        print("DISPLAYING STUDENTS INFORMATION : \n")

        if len(STUDENT_NAME) == 0 and len(STUDENT_ROLL_NUMBER) == 0 and len(
            STUDENT_AGE) == 0 and len(STUDENT_CLASS) == 0 and len(
                STUDENT_MOBILE_NUMBER) == 0 and len(
                    STUDENT_ADDRESS) == 0 and len(STUDENT_EMAIL) == 0:
            print("\n")
            print("\t\t\t'OOPS! NOTHING TO DISPLAY, BECAUSE NO DATA IS THERE.")
            print("\n")
        else:
            print("STUDENT'S NAME : ", end="\n")

            for x in STUDENT_NAME:
                print(x)
            print()

            print(end="\n")

            print("STUDENT'S ROLL NUMBER :", end="\n")

            for y in STUDENT_ROLL_NUMBER:
                print(y)
            print()

            print(end="\n")

            print("STUDENT'S AGE :", end="\n")

            for z in STUDENT_AGE:
                print(z)
            print()

            print(end="\n")

            print("STUDENT'S MOBILE NUMBER :", end="\n")

            for x in STUDENT_MOBILE_NUMBER:
                print(x)
            print()

            print(end="\n")

            print("STUDENT'S EMAIL :", end="\n")

            for y in STUDENT_EMAIL:
                print(y)
            print()

            print(end="\n")

            print("STUDENT'S CLASS :", end="\n")

            for z in STUDENT_CLASS:
                print(z)
            print()

            print(end="\n")

            print("STUDENT'S ADDRESS :", end="\n")

            for x in STUDENT_ADDRESS:
                print(x)
            print()

            print(end="\n")


SMS = STUDENT_MANAGEMENT_SYSTEM()

if __name__ == '__main__':
    print("\n")

    print("' ********** WELCOME TO STUDENT INFORMATION SYSTEM ********** ' \n")
    run = True

    while run:
        print("PRESS FROM THE FOLLOWING OPTION : \n")

        print("PRESS 1 : TO ADD STUDENT INFORMATION.")
        print("PRESS 2 : TO DELETE STUDENT INFORMATION.")
        print("PRESS 3 : TO UPDATE STUDENT INFORMATION.")
        print("PRESS 4 : TO DISPLAY STUDENT INFORMATION.")
        print("PRESS 5 : TO EXIT SYSTEM.")

        while True:
            try:
                OPTION = int(input("ENTER YOUR OPTION : "))
                break
            except ValueError:
                print("\n")
                print("SORRY,PRESS FROM THE FOLLOWING OPTION :")

        if OPTION == 1:
            SMS.ADD_STUDENT_INFORMATION()
        elif OPTION == 2:
            SMS.DELETE_STUDENT_INFORMATION()
        elif OPTION == 3:
            SMS.UPDATE_STUDENT_INFORMATION()
        elif OPTION == 4:
            SMS.DISPLAY_STUDENT_INFORMATION()
        elif OPTION == 5:
            print("THANK YOU ! VISIT AGAIN.")
            run = False
        else:
            print("PLEASE CHOOSE CORRECT OPTION FROM THE FOLLOWING.")
            print("\n")
