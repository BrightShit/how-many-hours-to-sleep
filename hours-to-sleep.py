old = int(input("Hey! how old are you?\n1) 0-3 months\n2) 4-11 months)\n3) 1-2 years"
                 + '\n4) 3-5 years\n5) 6-13\n6) 14-17\n7) 18-25\n8) 26-64\n9) 65\n'))
hours_of_sleep = int (input("How many hours a day do you usually sleep? \n"))

if old == 1 and hours_of_sleep >=14 and hours_of_sleep <=17:
    print('You sleep the recommended amount (14-17)')
elif old == 1 and hours_of_sleep <14 or hours_of_sleep > 17:
    print("You need to sleep between 14-17 hours a day")

elif old == 2 and hours_of_sleep >=12 and hours_of_sleep <=15:
    print('You sleep the recommended amount (12-15)')
elif old == 2 and hours_of_sleep <12 or hours_of_sleep > 15:
    print("You need to sleep between 12-15 hours a day")

elif old == 3 and hours_of_sleep >=11 and hours_of_sleep <=14:
    print('You sleep the recommended amount (11-14)')
elif old == 3 and hours_of_sleep <11 or hours_of_sleep > 14:
    print("You need to sleep between 11-14 hours a day")

elif old == 4 and hours_of_sleep >=10 and hours_of_sleep <=13:
    print('You sleep the recommended amount (10-13)')
elif old == 4 and hours_of_sleep <10 or hours_of_sleep > 13:
    print("You need to sleep between 10-13 hours a day")

elif old == 5 and hours_of_sleep >=9 and hours_of_sleep <=11:
    print('You sleep the recommended amount (9-11)')
elif old == 5 and hours_of_sleep <9 or hours_of_sleep > 11:
    print("You need to sleep between 9-11 hours a day")

elif old == 6 and hours_of_sleep >=8 and hours_of_sleep <=10:
    print('You sleep the recommended amount (8-10)')
elif old == 6 and hours_of_sleep <8 or hours_of_sleep > 10:
    print("You need to sleep between 8-10 hours a day")

elif old == 7 and hours_of_sleep >=7 and hours_of_sleep <=9:
    print('You sleep the recommended amount (7-9)')
elif old == 7 and hours_of_sleep <7 or hours_of_sleep > 9:
    print("You need to sleep between 7-9 hours a day")

elif old == 8 and hours_of_sleep >=7 and hours_of_sleep <=9:
    print('You sleep the recommended amount (7-9)')
elif old == 8 and hours_of_sleep <7 or hours_of_sleep > 9:
    print("You need to sleep between 7-9 hours a day")

elif old == 9 and hours_of_sleep >=7 and hours_of_sleep <=8:
    print('You sleep the recommended amount (7-8)')
elif old == 9 and hours_of_sleep <7 or hours_of_sleep > 8:
    print("You need to sleep between 7-8 hours a day")
