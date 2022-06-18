
def how__many__hours__():
    old = int(input("Hey! how old are you?\n1) 0-3 months\n2) 4-11 months)\n3) 1-2 years"
                 + '\n4) 3-5 years\n5) 6-13\n6) 14-17\n7) 18-25\n8) 26-64\n9) 65\n'))
    hours = ""
    if old == 1:
        hours = "14-17"

    if old == 2:
        hours = "12-15"
    
    elif old == 3:
        hours = "11-14"
    
    elif old == 4:
        hours = "10-13"
    
    elif old == 5:
        hours = "9-11"
    
    elif old == 6:
        hours = "8-10"
    
    elif old == 7 or old == 8:
        hours = "7-9"

    elif old == 9:
        hours = "7-8"
    else:
        print("Choose a valid option")


    print("You need to sleep "+str(hours)+" hours a day")
how__many__hours__()
input()
