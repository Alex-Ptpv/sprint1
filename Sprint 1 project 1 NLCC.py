# Project: NL Chocolate Company Employee Travel Claim
# Written by: Josh White
# Date Written: Feb. 21, 2023

import datetime


# CONSTANTS


perdiem_rate = float(85)
mileage_rate = float(.17)
rental_rate = float(65)
hst_rate = float(.15)
max_days = datetime.timedelta(days=7)






# USER INPUTS
while True:
    emp_num = (input("Please input your 5 digit Employee Number: "))
    if len(emp_num) > 5:
        print("Employee number must be 5 characters, please try again ")
    elif len(emp_num) < 5:
        print("Employee number must be 5 characters, please try again ")
    elif not emp_num.isdigit():
        print("Employee Number must contain numeric input only, please try again: ")
    else:
        break

first_name = input("Please enter your first name: ").title()
last_name = input("Please enter your last name: ").title()
trip_loc = input("Please enter your trip location: ").title()



while True:
    car = input("Please enter if car is owned or rented (O or R): ").upper()
    if car =="":
        print("Cannot be left blank, please try again")
    elif car != "O" and car != "R":
        print("Enter only O or R for owned or rented ")
    else:
        break



while True:
    tot_km = float(input("Please enter your total KM: "))
    if tot_km > 2000:
        print("KM limit exceeded, try again ")
    else:
        break



while True:
    claim_type = input("Please enter ClaimType (S/E): ").upper()
    if claim_type != "S" and claim_type != "E":
        print("Error, please try again")
    else:
        break


while True:
   try:
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
   except:
       print("Start date is not valid, enter in format given")
   else:
    break


while True:
     end_date = input("Enter the end date (YYYY-MM-DD): ")
     end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
     if start_date > end_date:
         print("please try again")
     elif end_date - start_date > max_days:
         print("Exceeds total allowable days, try again")
     else:
         break





#CALCULATIONS
num_days = (end_date - start_date).days
perdiem = (num_days * perdiem_rate)

if car == "O":
    mile_amt = mileage_rate * tot_km
else:
    mile_amt = num_days * 65.00





if num_days > 3:
    bonus = 100
elif tot_km > 1000:
    bonus = tot_km * .04
elif claim_typeype == "E":
    bonus = 45.00
elif start_date.month == 12 and start_date.day == 15:
    Bonus = 50.00



claim_amt = perdiem + mile_amt +bonus
hst = claim_amt*hst_rate
claim_total = claim_amt + hst

#OUTPUT

print(f"-----------------------------------------------------------")
print(f"-----------NL Chocolate CO Employee Travel Claim-----------")
print(f"           -------------------------------------           ")
print(f"Employee Name: {first_name} {last_name}   ")
print(f"Employee Number:{emp_num}                  Claim Type:{claim_type}   ")
print(f"Car type:{car}                     ")
print(f"Trip Location:{trip_loc}                   Total KM:{tot_km}        ")
print(f"Departure:{start_date}  Return:{end_date}   Number of Days:{num_days}   ")
print(f"                                Per Diem----------------{perdiem}")
print(f"                                Mileage Amount----------{mile_amt}")
print(f"                                Bonus-------------------{bonus}")
print(f"                                HST---------------------{hst} ")
print(f"                                Total-------------------{claim_total}")
