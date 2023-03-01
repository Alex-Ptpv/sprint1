import datetime

import console

# main program menu

def display_menu():
    """Displays the menu options to the user."""
    print("Sprint 1 Project Fun")
    print("-        *         -")
    print("Travel Claims Processing System")
    print("1. Enter an Employee Travel Claim.")
    print("2. Fun Interview Question.")
    print("3. Cool Stuff with Strings and Dates.")
    print("4. Something Old, Something New")
    print("5. Quit Program.")
    print()


def validate_input():
    """Validates user input to allow only values 1-5."""
    while True:
        choice = input("Enter choice (1-5): ")
        if choice.isdigit() and int(choice) in range(1,6):
            return int(choice)
        else:
            print("Invalid input. Please enter a number between 1 and 5.")



def ncc_travel():
    # Newfoundland Chocolate Co. Travel Claim

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
        claim_type = input("Please enter ClaimType (S/E): ").upper()
        if claim_type != "S" and claim_type != "E":
            print("Error, please try again")
        else:
            break

    while True:
        car = input("Please enter if car is owned or rented (O or R): ").upper()
        if car == "":
            print("Cannot be left blank, please try again")
        elif car != "O" and car != "R":
            print("Enter only O or R for owned or rented ")
        else:
            break

    while True:
        if car == "O":
            tot_km = int(input("enter total km travelled: "))
            mile_amt = mileage_rate * tot_km
            if tot_km >= 2000:
                print("km permissions exceeded, try again:")
            else:
                break
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

    # CALCULATIONS
    num_days = (end_date - start_date).days
    perdiem = (num_days * perdiem_rate)

   # if car == "O":
    #    mile_amt = mileage_rate * tot_km
    if car == "R":
        mile_amt = num_days * 65.00
    else:
        mile_amt = mileage_rate * tot_km

    if car=="O" and tot_km > 1000:
        bonus_k = .04* mile_amt
    else:
        bonus_k = 0


    if claim_type == "E":
        bonus_c = 45.00
    else:
        bonus_c = 0

    if start_date.month == 12 and start_date.day == 15:
        bonus_d = 50.00 * num_days
    elif start_date.month == 12 and start_date.day == 16:
        bonus_d = 50.00 * num_days
    elif start_date.month == 12 and start_date.day == 17:
        bonus_d = 50.00 * num_days
    elif start_date.month == 12 and start_date.day == 18:
        bonus_d = 50.00 * num_days
    elif start_date.month == 12 and start_date.day == 19:
        bonus_d = 50.00 * num_days
    elif start_date.month == 12 and start_date.day == 20:
        bonus_d = 50.00 * num_days
    elif start_date.month == 12 and start_date.day == 21:
        bonus_d = 50.00 * num_days
    elif start_date.month == 12 and start_date.day == 22:
        bonus_d = 50.00 * num_days
    else:
        bonus_d = 0

    if num_days > 3:
        bonus_days = 100.00
    else:
        bonus_days = 0

    bonus = bonus_days + bonus_d + bonus_c + bonus_k

    claim_amt = perdiem + mile_amt + bonus
    hst = claim_amt * hst_rate
    claim_total = claim_amt + hst

    # FORMATTING
    start_date_dsp = (start_date.strftime("%d-%b-%y"))
    end_date_dsp = (end_date.strftime("%d-%b-%y"))
    perdiem_dsp = "${:,.2f}".format(perdiem)
    mile_amt_dsp = "${:,.2f}".format(mile_amt)

    if car =="O":
        tot_km_dsp = (f"Total KM:{tot_km}")
    else:
        tot_km_dsp = ""

    bonus_dsp = "${:,.2f}".format(bonus)
    hst_dsp = "${:,.2f}".format(hst)
    claim_total_dsp = "${:,.2f}".format(claim_total)

    # OUTPUT

    print(f"")
    print(f"                     *--*---**--***---***---***--**---*--*    ")
    print(f"                     NL Chocolate CO Employee Travel Claim ")
    print(f"                     *--*---**--***---***---***--**---*--*                         ")
    print(f"")
    print(f"Employee Name: {first_name} {last_name}   ")
    print(f"Employee Number:{emp_num}                             Claim Type:{claim_type}   ")
    print(f"Car type:{car}                     ")
    print(f"Trip Location:{trip_loc}                                       ")
    print(f"Departure:{start_date_dsp:<9}   ")
    print(f"Return:{end_date_dsp:<9}")
    print(f"Number of Days:{num_days}                                  Per Diem----------------{perdiem_dsp:>9} ")
    print(f"{tot_km_dsp:<14}                                    Mileage Amount----------{mile_amt_dsp:>9}")
    print(f"                                                  Bonus-------------------{bonus_dsp:>9}")
    print(f"                                                  HST---------------------{hst_dsp:>9} ")
    print(f"                                                  Total-------------------{claim_total_dsp:>9}")
    print(f"")
    print(f"-----------------------------------------------------------------------------------")
    input("Press any key to continue...")
    display_menu()
    choice = validate_input()
    choice_func(choice)

# FizzBuzz task

def fizz_buzz():
    for num in range(100):
        if num % 5 == 0 and num % 8 != 0:
            print("Fizz")
        elif num % 8 == 0 and num % 5 != 0:
            print("Buzz")
        elif num % 5 == 0 and num % 8 == 0:
            print("FizzBuzz")
        else:
            print(num)
    input("Press any key to continue...")
    display_menu()
    choice = validate_input()
    choice_func(choice)

def emp_inf():
    import datetime

    # Employee information
    first_name = "John"
    Last_name = "Doe"
    Phone_num = "555-1235"
    Start_date = datetime.date(2019, 5, 1)
    Birth_date = datetime.date(1990,1 ,1)

    # Current date
    Today = datetime.date.today()

    # Calculate age and years of employment
    Age = Today.year - Birth_date.year
    Years_of_employment = Today.year - Start_date.year

    # Format output string
    Output_string = (f'Hello {first_name} {Last_name}! Today is{Today: %A, %B %d, %Y}')
    Output_string += (f" You are {Age} years old and have been employed here for {Years_of_employment} years")
    Output_string += (f' Your phone number is {Phone_num}.')
    print(Output_string)

    input("Press any key to continue...")
    display_menu()
    choice = validate_input()
    choice_func(choice)

def console():

    # first install rich in the terminal
    # pip install rich
    from rich.console import Console
    # Create a console object
    console = Console()
    # Print some styled text
    console.print("Hello, [bold magenta]world[/bold magenta]!")
    # Print a table of data
    data = [("John", 24), ("Jane", 32), ("Bob", 45)]
    console.print("[bold underline]Name\tAge[/bold underline]")
    for name, age in data:
        console.print(f"{name}\t{age}")

    input("Press any key to continue...")
    display_menu()
    choice = validate_input()
    choice_func(choice)


def choice_func(val):
    while val != 5:
        if val == 1:
            ncc_travel()
        elif val == 2:
            fizz_buzz()
        elif val == 3:
            emp_inf()
        elif val == 4:
            console()
    if val == 5:
        print("thanks for using the Travel Claims Processing System")
        exit

display_menu()
choice = validate_input()
choice_func(choice)


