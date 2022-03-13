import datetime
from datetime import date
import pyautogui as py
from time import sleep as z

def savings_plan():
    print('Please input the date of your next pay check')
    year = int(input('Enter a year'))
    month = int(input('Enter a month'))
    day = int(input('Enter a day'))

    start_date = datetime.date(year, month, day)
    print(start_date)

    print('Please input the end date of your savings plan')
    year_2 = int(input('Enter a year'))
    month_2 = int(input('Enter a month'))
    day_2 = int(input('Enter a day'))

    end_date = datetime.date(year_2, month_2, day_2)
    print(end_date)

    delta = end_date - start_date

    pay_interval = int(input("How often do you get paid? Every 1 or 2 weeks?... (1/2)"))

    if pay_interval == 2:

        savings_target = int(input('How much money would you like to save before the end date is reached?.. $'))
        print('$' + str(savings_target))

        remainder = delta.days % 14

        pay_periods = ((delta.days - remainder)/14)

        per_check_goal = (int(savings_target)/(pay_periods + 1))

        print("You will be paid " + str(pay_periods + 1) + " times before your goal date...")

        print("You will need to save $" + str(per_check_goal) + " every time you gate paid before your goal date...")

    if pay_interval == 1:

        savings_target = int(input('How much money would you like to save before the end date is reached?.. $'))
        print('$' + str(savings_target))

        remainder = delta.days % 7

        pay_periods = ((delta.days - remainder) / 7)

        per_check_goal = round((int(savings_target) / (pay_periods + 1)), 1)

        print("You will be paid " + str(pay_periods + 1) + " times before your goal date...")

        print("You will need to save $" + str(round(per_check_goal, 2)) + " every time you gate paid before your goal date...")

    #The save option is obviously set up for a windows device, different operating systems will need alterations
    save_option = input("Would you like to save this plan as a note?... (Yes/No)")
    if save_option.lower() == "no":
        pass
    if save_option.lower() == "yes":
        file_name = input("What would you like to name this plan?...")
        py.hotkey('win')
        py.write("notepad")
        py.hotkey("enter")
        z(1)
        py.write("You will be paid " + str(pay_periods + 1) + " times before your goal date...")
        py.hotkey("enter")
        py.write("You will need to save $" + str(round(per_check_goal, 2)) + " every time you gate paid before your goal date...")
        py.hotkey("enter")
        py.write("Start date: " + str(start_date))
        py.hotkey("enter")
        py.write("End date: " + str(end_date))
        z(1)
        py.hotkey("ctrl", "shift", "s")
        py.write(file_name)

savings_plan()


