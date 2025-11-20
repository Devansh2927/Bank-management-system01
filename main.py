from pathlib import Path
import json
import string
import random

class Bank():
    database ='database.json'
    data =[]

    try:
        if Path(database).exists():
            with open(database) as fs:
               data =json.loads(fs.read())
        else:
            print("sorry we are facing some issues:-")

    except Exception as err:
        print(f"An error occured as {err}")

    @classmethod
    def __update(cls):
        with open(cls.database,'w')as fs:
            fs.write(json.dumps(cls.data))

    @staticmethod
    def __accountno():
        alpha =random.choices(string.ascii_letters,k =5)
        digits =random.choices(string.digits,k=4)
        id =alpha +digits
        random.shuffle(id)
        return "".join(id)  #list to convert string use of .join method

    def create_account(self):
        d ={
            "name":input('Enter your name:-'),
            "email":input("Enter your Mail id :"),
            "phone No.":int(input("Enter your phone Number")),
            "pin": int(input ("Please tell your pin (4 digit)")),
            "Account No.":Bank.__accountno(),
            "Balance" : 0
           }
        # Bank.data.append(d)
        # Bank.__update()

        # print(f"please note down your account number:{d['Account No.']}")
        if len(str(d['pin'])) != 4:
            print("Your pin is invalid")

        elif len(str(d["phone No."])) != 10:
            print("Please recheck your phone number")
        else:
            Bank.data.append(d)
            Bank.__update()

        print("\n Account created Successfully")

        for i in d:
            print(f"{i} :{d[i]}")
        print("Note down your account Number")

    def deposit_money(self):
        accNumber = input("Enter your account number:- ")
        pin = int(input("Enter your pin:- "))

        userdata = [i for i in Bank.data if i['Account No.'] == accNumber and i['pin'] == pin]
        print(user)
        if  not userdata:
            print("sorry no data found")

        else:
            amount = int(input("Enter the Amount you want to deposit:-"))
            if amount  > 10000 or amount < 0:
                print("sorry the amount is too much you cannot deposit above 10000")

            else:
                userdata[0]['Balance'] += amount
                Bank.__update()
                print("Amount deposited successfully ")

    def withdraw_money(self):
        accnumber = input("Enter your account number ")
        pin = int(input("Enter your pin "))

        userdata = [i for i in Bank.data if i['Account No.'] == accnumber and i['pin'] == pin]
        if not userdata:
               print("sorry no data found")
        else:
            amount = int(input("Enter amount to be withdrawn: "))
            if amount <= 0:
                print("Invalid amount")
            elif amount > 10000:
                print("Greater than 10000")
            else:
                if userdata[0]['Balance'] < amount:
                    print("Insufficent Balance")
                else:
                    userdata[0]['Balance'] -=amount
                    Bank.__update()
                    print("Amount Debited")

    def details(self):
        accNo = input("Enter your account no.: ")
        pin = int(input("Enter your pin: "))
        user_data = [i for i in Bank.data if i['Account No.'] == accNo and i['pin'] == pin]
        if not user_data:
            print("User not found!")
        else:
            for i in user_data[0]:
                print(f"{i}: {user_data[0][i]}")

    def  update_details(self):
        accNo = input("Enter your account no:-")
        pin = int(input("Enter your pin:-"))
        userdata = [i for i in Bank.data if i['Account No.'] == accNo and i['pin'] == pin]
        if not userdata:
            print("User not found!")
        else:
            print("you cannot change Account Number")
            print("Now update your details and skip if u don't want to update")
                #name ,pin,email,phone
        newdata= {
                "name": input("Enter your new name or press Enter:-"),
                "email":input("Enter your new Email or press enter to skip:-"),
                "pin": (input("Enter new Pin or press enter to skip:-")),
                "phone No":(input("Enter your new phone No:- "))
            }
        newdata["Account No."] = userdata[0]["Account No."]
        newdata["Balance"] = userdata[0]["Balance"]
        #Handle the skipped values:
        for i in newdata:
            if newdata[i]=="":
               newdata[i]=userdata[0][i]
        print(newdata)

        #We have to update new data to database:
        for i in userdata[0]:
            if userdata[0][i]==newdata[i]:
                continue
            else:
                if newdata[i].isnumeric():
                   userdata[0][i]=int(newdata[i])

                else:
                    userdata[0][i]=newdata[i]
        print(userdata)
        Bank.__update
        print("Details updated Successfully!")

    def Delete_account(self):
        accnumber = input("please tell your account number ")
        pin = int(input("please tell your pin aswell "))

        userdata = [i for i in Bank.data if i['Account No.'] == accnumber and i['pin'] == pin]

        if not  userdata:
            print("User not found")
        else:
            for i in Bank.data:
                if i["Account No."]==accnumber and i["pin"]==pin:
                    Bank.data.remove(i)
        Bank.__update()
        print("Account deleted successfully!")

user =  Bank()
print("press 1 for creating an account")
print("press 2 to credit money")
print("press 3 to debit money")
print("press 4 for show details")
print("press 5 for updating the details")
print("press 6 for deleting the account")

check =int(input("Enter your choice:"))

if check==1:
    user.create_account()

if check==2:
    user.deposit_money()

if check==3:
    user.withdraw_money()

if check==4:
    user.details()

if check==5:
    user.update_details()

if check==6:
    user.Delete_account()






