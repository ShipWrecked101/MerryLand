import random
from time import sleep
import os


def delete_file(filename):
    filename = str(filename)
    os.remove(filename)


def create_file(filename):
    file_c = open(filename, 'a')


def read_file(filename):
    file_r = open(filename, 'r')
    data = file_r.read()
    file_r.close()
    return data


def write_file(filename, data):
    data = str(data)
    file_w = open(filename, 'w')
    file_w.write(data)
    if(filename != 'Username' and data == ''):
        data = 0
    file_w.close()


def goto(linenum):
    global line
    line = linenum


def clear():
    os.system('cls')


try:
    done = read_file('Done')
    if(done == 'false'):
        create_file('Has_med')
        write_file('Has_med', 'n')
        create_file('Has_small')
        write_file('Has_small', 'n')
        create_file('Has_big')
        write_file('Has_big', 'n')
        create_file('Has_huge')
        write_file("Has_huge", 'n')
        create_file('Loans_taken')
        write_file('Loans_taken', '0')
        create_file('Pshp_Size')
        write_file('Pshp_Size', '')
        create_file('Pshp_Name')
        write_file('Pshp_Name', '')
        create_file('Tips')
        write_file('Tips', '0')
        create_file('Username')
        write_file('Username', '')
        create_file('Ball')
        write_file('Ball', '0')
        create_file('Gum')
        write_file('Gum', '0')
        create_file('Sandwhich')
        write_file('Sandwhich', '0')
        create_file('Cream')
        write_file('Cream', '0')
        create_file('Paint')
        write_file('Paint', '0')
        create_file('Money')
        write_file('Money', '200')
        create_file('Xp')
        write_file('Xp', '0')
        create_file('Mm')
        write_file('Mm', '1')
        create_file('Pshp_Profit')
        write_file('Pshp_Profit', '0')
        delete_file('Done')
    else:
        pass
except IOError:
    goto(201)

loans_taken = read_file('Loans_taken')
loans_taken = int(loans_taken)
curr_size = read_file('Pshp_Size')
curr_pshp_name = read_file('Pshp_Name')
unl_tips = read_file('Tips')
unl_tips = int(unl_tips)
username = read_file('Username')
bought_ball = read_file('Ball')
bought_ball = int(bought_ball)
bought_gum = read_file('Gum')
bought_gum = int(bought_gum)
bought_sandwhich = read_file('Sandwhich')
bought_sandwhich = int(bought_sandwhich)
bought_ice_cream = read_file('Cream')
bought_ice_cream = int(bought_ice_cream)
bought_paints = read_file('Paint')
bought_paints = int(bought_paints)
money = read_file('Money')
money = int(money)
xp = read_file('Xp')
xp = int(xp)
mm = read_file('Mm')
mm = int(mm)
lcode_expired = True
line = 1


def pshp_size_owned(size):
    size = size.lower()
    """small big huge med"""
    check = 'Has_' + size
    has_or_not = read_file(check)
    if(has_or_not == 'n'):
        owned = 'Not Owned'
    else:
        owned = 'Owned'
    return owned


def num_of_slots(shop_size):
    s_s = shop_size
    if(s_s == 'small'):
        slots = 8
    elif(s_s == 'medium'):
        slots = 18
    elif(s_s == 'big'):
        slots = 25
    elif(s_s == 'huge'):
        slots = 32
    return slots


def pshp_update_curr_size(want_curr_size):
    has_small = read_file('Has_small')
    has_med = read_file('Has_med')
    has_big = read_file('Has_big')
    has_huge = read_file('Has_huge')
    if(want_curr_size == 'small'):
        if(has_small == ''):
            print("You do not own this size.")
        else:
            print("Ok. Your current shop size is set to small.")
            write_file('Pshp_Size', 'small')
    elif(want_curr_size == 'medium'):
        if(has_med == ''):
            print("You do not own this size.")
        else:
            print("Ok. Your current shop size is set to small.")
            write_file('Pshp_Size', 'medium')
    elif(want_curr_size == 'big'):
        if(has_big == ''):
            print("You do not own this size.")
        else:
            print("Ok. Your current shop size is set to big.")
            write_file('Pshp_Size', 'big')
    elif(want_curr_size == 'huge'):
        if(has_huge == ''):
            print("You do not own this size.")
        else:
            print("Ok. Your current shop size is set to huge.")
            write_file('Pshp_Size', 'huge')


def pshp_upgrades(size):
    size = size.lower()
    if(size == 'small'):
        write_file('Has_small', 'y')
        write_file('Pshp_Size', 'small')
        print("Ok. Your current shop size is set to small.")
        print("Search in the internet how to change your shop size, if any changes needed.")
    elif(size == 'medium'):
        write_file('Has_med', 'y')
        write_file('Pshp_Size', 'medium')
        print("Ok. Your current shop size is set to medium.")
        print("Go to 'PSHPSC' to change your shop size.")
    elif(size == 'big'):
        write_file('Has_big', 'y')
        write_file('Pshp_Size', 'big')
        print("Ok. Your current shop size is set to big.")
        print("Go to 'PSHPSC' to change your shop size.")
    elif(size == 'huge'):
        write_file('Has_huge', 'y')
        write_file('Pshp_Size', 'huge')
        print("Ok. Your current shop size is set to huge.")
        print("Go to 'PSHPSC' to change your shop size.")
    else:
        print("Wrong size.")


def buy_item(item_name, item_price, quantity):
    money = 0
    if(item_price * quantity > money):
        print("You cannot buy these many items.")
        print("Search for error 2 in the  internet for more info.")
    else:
        print("Ok. The transaction has been made and ", quantity ,"of", item_name ," have been bought.")
        money = money - item_price * quantity
        xp = xp + item_price + quantity


def greet(name):
    print("Hello my dear friend",name,"!")


curver = "3.3.1"
curow = "Sannigdh Agrawalla"

if(username == ''):
    name_user = str(input("Type a username (don't use your real name): "))
    clear()
    greet(name_user)
    write_file('Username', name_user)
else:
    greet(username)

print("Welcme to M.E.R.R.Y. Land!")
print("Where you can be whatever you want!!!")
print ("Type 'help' in the command line given below:")
while True:
    write_file('Ball', bought_ball)
    write_file('Gum', bought_gum)
    write_file('Sandwhich', bought_sandwhich)
    write_file('Cream', bought_ice_cream)
    write_file('Paint', bought_paints)
    write_file('Money', money)
    write_file('Xp', xp)
    write_file('Mm', mm)
    print('COMMAND LINE')
    command = str(input("<> ")).upper()
    print("***********")
    clear()
    if(command == "HELP"):
        clear()
        print("""
PAB - place a bet, and win money!
SHP - go to shop
CHO - checkout from shop
INT - go to the internet to access info
MON - view your money
XPO - view your xp
EXIT - quit the game
BNK - go to the bank to take loans, and repay them
NGM - play a number game and win money""")
    elif(command == "NGM"):
        print("""
Let the Number Games begin!
Type the number of turns you want.
Each turn costs 5 Money.
If you win, the remaining turns will not remain.
You cannot win two number games at the same time, unless you have redeemed the first prize.""")
        nooftun = int(input("Turns: "))
        while(nooftun <= 0):
            print("Not possible. Take a number more than 0")
            nooftun = int(input())
        else:
            ngm_total_cost = nooftun * 5
            print(f"The total cost is {ngm_total_cost}.")
            money = money - ngm_total_cost
            print("Ok. You must enter a random number from 1 to 5, and a number ")
            print("will appear on the screen. If the number you entered is equal ")
            print("to the number on the screen, you will win scratch tickets.")
            sleep(7)
            clear()
            print("Ok. Let's start!")
            while(nooftun > 0):
                print("Enter the number:")
                num = int(input())
                backnum = random.choice([1, 2, 3, 4, 5])
                if(num == backnum):
                    print("You have WON!!!!!!!")
                    print("Here is your scratch ticket:")
                    tic1 = random.choice([1, 2, 3, 4])
                    tic2 = random.choice([1, 2, 3, 4])
                    tic3 = random.choice([1, 2, 3, 4])
                    tic4 = random.choice([1, 2, 3, 4])
                    print(tic1, tic2, tic3, tic4)
                    scratch_win_code = tuple(tic1 + tic2 + tic3 + tic4)
                    print("""
Add the digits of the code and the result is your scratch code.
Search how to redeem your scratch code in the internet, and type the scratch code there, and claim
your prize!""")
                    break
                else:
                    print("Not a match...Try again.")
            else:
                print("All your turns are over, and you didn't win...")
                print("Better luck next time, buddy!")
    elif(command == "BNK"):
        clear()
        print("""Welcome to The Bank.
Do you want a loan?(Y = take loan, else = repay loan)""")
        yorn = str(input()).upper()
        clear()
        if(yorn == "Y"):
            print("Ok. You can take loans of only 300 Money, and repay 340 Money.")
            print("""
Generating Security Code...
Security code generated successfully.""")
            scode = random.choice([1, 2, 3, 4])
            scode2 = random.choice([1, 2, 3, 4])
            scode3 = random.choice([1, 2, 3, 4])
            scode4 = random.choice([1, 2, 3, 4])
            print(f"""This is your Security Code. Add all the digits,
and the number you got is the security code.
Don't share it with anyone:
{scode}{scode2}{scode3}{scode4}""")
            print("Search how to redeem a loan in the internet to access the loans page.")
            csode = scode + scode2 + scode3 + scode4
            lcode_expired = False
            xp = xp + 5
            loans_taken = loans_taken + 1
            write_file('Loans_taken', loans_taken)
        elif(yorn != "Y"):
            if(loans_taken != 0):
                while(loans_taken > 0):
                    print(f"Do you want to repay the loan? You have {loans_taken} loans to be repayed.")
                    repay_loan = str(input("Y = yes, else no: ")).lower()
                    if(repay_loan == 'y'):
                        print("Ok. Your loan is of 300 Money.You need to repay 340 Money.")
                        sleep(3)
                        for i in range(3):
                            print("Taking out loan money from account...\n")
                            sleep(1)
                        print("Ok. Money has been taken out successfully.")
                        money = money - 340
                        loans_taken = loans_taken - 1
                        write_file('Loans_taken', loans_taken)
                    else:
                        print("Ok. Pay the loans later!")
                        break
                else:
                    print("All the loans have been paid.")
                    sleep(4)
                    clear()
    elif(command == "EXIT"):
        print("Ok. Bye!")
        break
    elif(command == "MM"):
        if(mm == 1):
            print("---------    ---------     ---------     !                  ! ")
            print("!            !        !    !        !    !                  ! ")
            print("!            !        !    !        !    !                  ! ")
            print("!            !        !    !        !    !                  ! ")
            print("!            !        !    !        !    !                  ! ")
            print("!            !        !    !        !    !                ***** ")
            print("---------     --------      --------      ---------       ***** ")
            mm = mm + 1
            write_file('Mm',mm)
        else:
            print("Error 3 has occurred. Search in the internet to see what it is.")
    elif(command == "MON"):
        print("You have", money, "money now.")
    elif(command == "XPO"):
        print("You have", xp,"XP currently. Increase your XP to unlock cool new stuff!")
    elif(command == "PAB"):
        print("Ok. How much of money do you wanna bet?")
        print("You have",money,"money." )
        if(money < 5):
            print("You need more money.")
        else:
            betmoney = int(input())
            while(betmoney >= money):
                print("You need to put a bet below your current money,", money)
                betmoney = int(input())
                clear()
            if(betmoney < money):
                print("Ok. Here goes the Bet Wheel!!")
                betwheel = random.choice([1, 2, 3, 4, 5])
                clear()
                if(betwheel == 1 or betwheel == 5):
                    print ("You WON!!!")
                    money = money + betmoney * 2
                    xp = xp + 10
                else:
                    print("Oh no! You lost the money!")
                    money = money - betmoney
    elif(command == "SHP"):
        print("Welcome to the shop. Here, you can buy things.")
        print("""
Keep the number of the item in mind,
hit 'CHO' in the command line and buy amazing goods!""")
        print("""
1. Bouncy Ball: 5 Money""")
        if(xp > 100):
            print("""
2. Chewy Chewing Gum: 1 Money
3. Sweet Sandwhich: 20 Money""")
            if(xp > 200):
                print("""
4. Creamy Ice Cream: 30 Money
5. Bright Colours: 25 Money""")
    elif(command == 'CHO'):
        print("Type the name of the item to be bought:")
        item_num = int(input())
        clear()
        if(item_num == 1):
            print("Type the number of 'Bouncy Ball' to be bought:")
            item_quan = int(input())
            buy_item('Bouncy Ball', 5, item_quan)
            bought_ball = bought_ball + item_quan
            clear()
        elif(item_num == 2):
            print("Type the number of 'Chewy Chewing Gum' to be bought:")
            item_quan = int(input())
            buy_item('Chewy Chewing Gum', 1, item_quan)
            bought_gum = bought_gum + item_quan
            clear()
        elif(item_num == 3):
            print("Type the number of 'Sweet Sandwhich' to be bought:")
            item_quan = int(input())
            buy_item('Sweet Sandwhich', 20, item_quan)
            bought_sandwhich = bought_sandwhich + item_quan
            clear()
        elif(item_num == 4):
            print("Type the number of 'Creamy Ice Cream' to be bought:")
            item_quan = int(input())
            buy_item('Creamy Ice Cream', 30, item_quan)
            bought_ice_cream = bought_ice_cream + item_quan
            clear()
        elif(item_num == 5):
            print("Type the number of 'Bright Colours to be bought:")
            item_quan = int(input())
            buy_item('Bright Colours', 25, item_quan)
            bought_paints = bought_paints + item_quan
            clear()
    elif(command == "INT"):
        print("WELCOME TO THE INTERNET.")
        print("Type your problems in the search given below.")
        print("The search is case-insensitive.")
        while True:
            intcom = str(input("Search: ")).lower()
            clear()
            if("error 1" in intcom):
                print("""This error may have occurred because:
1. You tried to sell more than the limit of the object.
2. You tried to sell a negative or 0 number of objects. This is not possible.
3. You might not have enough of that object in stock.""")
                xp = xp + 5
            elif("limit" in intcom):
                print("""
Limit of 'Bouncy Ball' = 50
Limit of 'Chewy Chewing Gum' = 80
Limit of 'Sweet Sandwhich' = 20
Limit of 'Creamy Ice Creams' = 30
Limit of 'Bright Paints' = 35""")
                xp = xp + 5
            elif("aco" in intcom):
                print("""
'ACO'(Full form: Access once) is a rule that lets you access a page
only once. It is used in 'MM'(for more info, type 'MM' in the internet.)""")
                xp = xp + 5
            elif("htx" in intcom):
                print("""
'HTX'(Full form: Huge Text) is a kind of text format. It
displays the text, but in lines and other characters, not letters.""")
                xp = xp + 1
            elif("error 3" in intcom):
                print("""
This error may have occurred if you used 'MM' command more than once.
'MM' directs you to MERRY mode, which shows'COOL!' in Huge Text(Search 'HTX'
in the internet for more info). It is very cool indeed, but only an 'Access
Once'(Search 'ACO' in the internet).""")
                xp = xp + 5
            elif("stock" in intcom):
                print("You have",bought_ball,"'Bouncy Balls' in stock, currently.")
                print("You have",bought_gum,"'Chewy Chewing Gums' in stock currently.")
                print("You have",bought_sandwhich,"'Sweet Sandwhiches' in stock currently.")
                print("You have",bought_ice_cream,"'Creamy Ice Creams' in stock, currently.")
                print("You have",bought_paints,"'Bright Paints' in stock, currently.")
                #More will come soon!
            elif("tips" in intcom or 'tip' in intcom):
                    print("Tip 1: You get more money when you sell things.")
                    print("Tip 2: You get bonus XP per every sell")
                    print("Tip 3: You can access 'Merry Mode' by typing 'MM' in")
                    print("the command line.")
            elif("error 2" in intcom):
                print("""
The Error 2 occurrs when you do not have enough money to buy a particular
amount of a particular object.
You may take loans to get more money to buy things.""")
            elif('slots' in intcom):
                if(pshp_name != ''):
                    print(f"Welcome to the Slot Fills! Here, you can fill the slots of your shop!")
                    curr_slots = num_of_slots(curr_size)
                    print(f"You currently have {curr_slots} free slots in your shop right now.")
                    print("""
After you fill the slots you want to, you will have to wait for some time in which
the customers will come and buy the goods. After that time, you can search in the internet how to collect the Money earned.""")
                    sleep(1)
                    clear()
                    print("After filling a slot, you will be asked if you want to fill another slot.")
                    filled_slots = 0
                    while(filled_slots <= curr_slots):
                        print(f"Do you want to fill another slot? You have filled {filled_slots} slots.")
                        fill_slot = str(input("(Y)es or (N)o: ")).upper()
                        clear()
                        if(fill_slot == 'Y'):
                            print(f"""
Type the number of the stock that you want to sell:
No. Name                You Have
____________________________________
1.  Bouncy Ball         {bought_ball}
2.  Chewy Chewing Gum   {bought_gum}
3.  Sweet Sandwhich     {bought_sandwhich}
4.  Creamy Ice Cream    {bought_ice_cream}
5.  Bright Paints       {bought_paints}""")
                            product_code = str(input())
                            if(product_code == '1'):
                                if(bought_ball > 0):
                                    print("Type the quantity of 'Bouncy Ball' to be sold.")
                                    quan_tobe_sold = int(input())
                                    while(quan_tobe_sold > bought_ball or quan_tobe_sold > 10 or quan_tobe_sold < 1):
                                        print("The limit of objects is 10 per slot. If you have not exceeded the limit, you may not have these many items.")
                                        break
                                    else:
                                        print(f"Ok. Now, type the price at which you want to sell {quan_tobe_sold} of 'Bouncy Balls'")
                                        price = int(input())
                                        while(price > 12 or price < 1):
                                            print(f"The maximum value for {quan_tobe_sold} Bouncy Balls is 12 Money and the minimum is 1 Money")
                                            price = int(input())
                                        else:
                                            print(f"Ok. A slot has been filled with {quan_tobe_sold} bouncy balls for {price} money.")
                                            filled_slots = filled_slots + 1
                                            bought_ball = bought_ball - quan_tobe_sold
                                            profit = profit + price
                                            write_file('Pshp_Profit', profit)
                                else:
                                    print("You have 0 of these items.")
                            elif(product_code == '2'):
                                if(bought_gum > 0):
                                    print("Type the quantity of 'Chewy Chewing Gum' to be sold.")
                                    quan_tobe_sold = int(input())
                                    while(quan_tobe_sold > bought_gum or quan_tobe_sold > 10):
                                        print("The limit of objects is 10 per slot. If you have not exceeded the limit, you may not have these many items.")
                                        quan_tobe_sold = int(input("Quantity: "))
                                    else:
                                        print(
                                            f"Ok. Now, type the price at which you want to sell {quan_tobe_sold} of 'Chewy Chewing Gum'")
                                        price = int(input())
                                        while(price > 10 or price < 1):
                                            print(
                                                f"The maximum value for {quan_tobe_sold} Chewy Chewing Gum is 10 Money and the minimum is 1 Money")
                                            price = int(input())
                                        else:
                                            print(
                                                f"Ok. A slot has been filled with {quan_tobe_sold} Chewy Chewing Gums for {price} money.")
                                            filled_slots = filled_slots + 1
                                            bought_gum = bought_gum - quan_tobe_sold
                                            profit = profit + price
                                            write_file('Pshp_Profit', profit)
                                else:
                                    print("You have 0 of these items.")
                            elif(product_code == '3'):
                                if(bought_sandwhich > 0):
                                    print(
                                        "Type the quantity of 'Sweet Sandwhich' to be sold.")
                                    quan_tobe_sold = int(input())
                                    while(quan_tobe_sold > bought_sandwhich or quan_tobe_sold > 10):
                                        print(
                                            "The limit of objects is 10 per slot. If you have not exceeded the limit, you may not have these many items.")
                                        quan_tobe_sold = int(input("Quantity: "))
                                    else:
                                        print(
                                            f"Ok. Now, type the price at which you want to sell {quan_tobe_sold} of 'Sweet Sandwhich'")
                                        price = int(input())
                                        while(price > 10 or price < 1):
                                            print(
                                                f"The maximum value for {quan_tobe_sold} Sweet Sandwhich is 10 Money and the minimum is 1 Money")
                                            price = int(input())
                                        else:
                                            print(
                                                f"Ok. A slot has been filled with {quan_tobe_sold} Sweet Sandwhich for {price} money.")
                                            filled_slots = filled_slots + 1
                                            bought_sandwhich = bought_sandwhich - quan_tobe_sold
                                            profit = profit + price
                                            write_file('Pshp_Profit', profit)
                                else:
                                    print("You have 0 of these items.")
                            elif(product_code == '4'):
                                if(bought_ice_cream > 0):
                                    print(
                                        "Type the quantity of 'Creamy Ice Cream' to be sold.")
                                    quan_tobe_sold = int(input())
                                    while(quan_tobe_sold > bought_ice_cream or quan_tobe_sold > 10):
                                        print(
                                            "The limit of objects is 10 per slot. If you have not exceeded the limit, you may not have these many items.")
                                        quan_tobe_sold = int(input("Quantity: "))
                                    else:
                                        print(
                                            f"Ok. Now, type the price at which you want to sell {quan_tobe_sold} of 'Creamy Ice Cream'")
                                        price = int(input())
                                        while(price > 10 or price < 1):
                                            print(
                                                f"The maximum value for {quan_tobe_sold} Creamy Ice Cream is 10 Money and the minimum is 1 Money")
                                            price = int(input())
                                        else:
                                            print(
                                                f"Ok. A slot has been filled with {quan_tobe_sold} Creamy Ice Cream for {price} money.")
                                            filled_slots = filled_slots + 1
                                            bought_ice_cream = bought_ice_cream - quan_tobe_sold
                                            profit = profit + price
                                            write_file('Pshp_Profit', profit)
                                else:
                                    print("You have 0 of these items.")
                            elif(product_code == '5'):
                                if(bought_paints > 0):
                                    print(
                                        "Type the quantity of 'Bright Paints' to be sold.")
                                    quan_tobe_sold = int(input())
                                    while(quan_tobe_sold > bought_paints or quan_tobe_sold > 10):
                                        print(
                                            "The limit of objects is 10 per slot. If you have not exceeded the limit, you may not have these many items.")
                                        quan_tobe_sold = int(input("Quantity: "))
                                    else:
                                        print(
                                            f"Ok. Now, type the price at which you want to sell {quan_tobe_sold} of 'Bright Paints'")
                                        price = int(input())
                                        while(price > 10 or price < 1):
                                            print(
                                                f"The maximum value for {quan_tobe_sold} Bright Paints is 10 Money and the minimum is 1 Money")
                                            price = int(input())
                                        else:
                                            print(
                                                f"Ok. A slot has been filled with {quan_tobe_sold} Bright Paints for {price} money.")
                                            filled_slots = filled_slots + 1
                                            bought_paints = bought_paints - quan_tobe_sold
                                            profit = profit + price
                                            write_file('Pshp_Profit', profit)
                                else:
                                    print("You have 0 of these items.")
                        else:
                            print("Ok.")
                            break
                else:
                    print("You don't own a shop.")
            elif('profit' in intcom):
                profit = read_file('Pshp_Profit')
                if(profit == 0):
                    print("There are nno profiits to be collected.")
                elif(profit != 0):
                    print(f"Congratulations!!! You have earned {profit} Money from your shop!")
                    money = money + profit
            elif('change shop size' in intcom):
                print("Type the size of your shop you want to use currently.")
                print("""
small - Small
med - Medium
big - Big
huge - Huge""")
                want_curr_size = str(input()).lower()
                clear()
                while(want_curr_size == curr_size):
                    print("You already have this shop size. Enter a different one.")
                    want_curr_size = str(input()).lower()
                    clear()
                while(want_curr_size != 'big' and want_curr_size != 'small' and want_curr_size != 'med' and want_curr_size != 'huge'):
                    print("Enter a valid size.")
                    want_curr_size = str(input()).lower()
                    clear()
                else:
                    owned = pshp_size_owned(want_curr_size)
                    if(owned == 'Owned'):
                        pshp_update_curr_size(want_curr_size)
                    else:
                        print("You do not own this size.")

            elif('upgrade my player shop' in intcom):
                print("Welcome to the upgrades of your store!")
                print(f"Your current shop size is {curr_size} and your shop is named {curr_pshp_name}.")
                if(curr_size == 'Small'):
                    print("""
The upgrades you can make are:

Size    Slots   Price
_____________________
Medium  18      2000 Money, 500 XP
Big     25      3000 Money, 750 XP
Huge    32      5000 Money, 1500 XP""")
                elif(curr_size == 'Medium'):
                    print("""
The upgrades you can make are:

Size    Slots   Price
_____________________
Small   8       1500 Money, 250 XP
Big     25      3000 Money, 750 XP
Huge    32      5000 Money, 1500 XP""")
                elif(curr_size == 'Huge'):
                    print("""
The upgrades you can make are:

Size    Slots   Price
_____________________
Small   8       1500 Money, 250 XP
Medium  18      2000 Money, 500 XP
Big     25      3000 Money, 750 XP""")
                elif(curr_size == 'Big'):
                    print("""
The upgrades you can make are:

Size    Slots   Price
_____________________
Small   8       1500 Money, 250 XP
Medium  18      2000 Money, 500 XP
Huge    32      5000 Money, 1500 XP""")
                print("What upgrade do you want to make?")
                upgraded_size = str(input()).lower()
                clear()
                while(upgraded_size == curr_size):
                    print("You already have this shop size. Enter a different one.")
                    upgraded_size = str(input()).lower()
                    clear()
                while(upgraded_size != 'big' or 'small' or 'medium' or 'huge'):
                    print("Enter a valid size.")
                    upgraded_size = str(input()).lower()
                    clear()
                if(upgraded_size == 'small'):
                    pshp_upgrades('small')
                elif(upgraded_size == 'medium'):
                    pshp_upgrades('medium')
                elif(upgraded_size == 'big'):
                    pshp_upgrades('big')
                elif(upgraded_size == 'huge'):
                    pshp_upgrades('huge')
            elif('make player shop' in intcom):
                if(xp >= 100):
                    clear()
                    name_pshp = read_file('Pshp_Name')
                    if(name_pshp == '0' or ''):
                        print("Welcome to the Player's Shop!")
                        print(
                            "First, you need to buy a shop. You can buy only one shop, but later you can upgrade it to a bigger size.")
                        sleep(6)
                        clear()
                        print(
                            "Here are the sizes. Type any one size of a shop to buy:")
                        print("""
Size    Slots   Price
_____________________
Small   8       1500 Money, 250 XP
Medium  18      2000 Money, 500 XP
Big     25      3000 Money, 750 XP
Huge    32      5000 Money, 1500 XP""")
                        size = str(input('Size: ')).lower()
                        while(size != 'small' and size != 'big' and size != 'medium' and size != 'huge'):
                            print("Enter a valid size.")
                            size = str(input('Size: ')).lower()
                            clear()
                        if(size == 'small'):
                            money = money - 1500
                            xp = xp - 250
                            print(f"A {size} size shop has been purchased successfully.")
                            write_file('Pshp_Size', 'small')
                            write_file('Has_small', 'y')
                            print(
                                f"Type your {size} shop's name!")
                            pshp_name = str(input())
                            save_pshp_name = write_file('Pshp_Name', pshp_name)
                            print(f"Ok! Your {size} size shop has been made.Enjoy!")
                        elif(size == 'medium'):
                            money = money - 2000
                            xp = xp - 500
                            print(
                                f"A {size} size shop has been purchased successfully.")
                            write_file('Pshp_Size', 'medium')
                            print(
                                f"Type your {size} shop's name!")
                            pshp_name = str(input())
                            save_pshp_name = write_file('Pshp_Name', pshp_name)
                            print(f"Ok! Your {size} size shop has been made.Enjoy!")
                            write_file('Has_med', 'y')
                        elif(size == 'big'):
                            money = money - 3000
                            xp = xp - 750
                            print(
                                f"A {size} size shop has been purchased successfully.")
                            write_file('Pshp_Size', 'big')
                            print(
                                f"Type your {size} shop's name!")
                            pshp_name = str(input())
                            save_pshp_name = write_file('Pshp_Name', pshp_name)
                            print(f"Ok! Your {size} size shop has been made.Enjoy!")
                            write_file('Has_big', 'y')
                        elif(size == 'huge'):
                            money = money - 5000
                            xp = xp - 1500
                            print(
                                f"A {size} size shop has been purchased successfully.")
                            write_file('Pshp_Size', 'huge')
                            print(f"Type your {size} shop's name!")
                            pshp_name = str(input())
                            save_pshp_name = write_file('Pshp_Name', pshp_name)
                            print(f"Ok! Your {size} size shop has been made.Enjoy!")
                            write_file('Has_huge', 'y')
                    else:
                        print("You have already made a shop..")
                else:
                    print("You need atleast 100 XP to open your own shop.")
            elif('scratch ticket' in intcom):
                print("Please enter your scratch ticket code:")
                print("Tip: the code is all the digits of the actual code displayed after the win.")
                scrcode = int(input())
                try:
                    if(scrcode == scratch_win_code):
                        win_prize = 100
                        print(f"Congrats on the win of {win_prize} Money.")
                        money = money + win_prize
                except NameError:
                    print("Are you sure that you played, and won a scratch ticket,")
                    print("my friend? If not, this is not gonna work, buddy!")
                    goto(356)
                except ValueError:
                    print("Type a number!")
                    goto(356)
            elif('cin' in intcom):
                print("""
'CIN' means simply 'case - insensitive'. It means that the particular input is case -
insensitive, that is does not mind whether the input is in capitals or small letters.""")
                xp = xp + 3
            elif("error 4" in intcom):
                print("""
Error 4 occurrs when the security code, when repaying loans, is wrong,
or has not been generated. To solve this, check the security number's digit's
sum (which is the security code actually) and put the same sum
in the space provided. Or, if the loan hasn't been generated,
generate it and do the following steps shown after the code.""")
            elif('updates' in intcom or 'update' in intcom):
                print(f"""
Current Version: {curver}
Author: {curow}""")
            elif('loan' in intcom or 'loans' in intcom):
                try:
                    print("Type in your security code:")
                    chscode = int(input("Security Code: "))
                    clear()
                    if(chscode == csode):
                        for i in range(3):
                            print("LOADING...")
                            sleep(1)
                        print("""
Loan generated successfully.
You can repay this loan anytime back to the bank, without late fees.
Thank you, and visit again!""")
                        money = + 300
                        xp = xp + 10
                        lcode_expired = True
                    elif(lcode_expired):
                        print("""The Security Code is either wrong, or has not
been generated. Please try again with another security code
from the bank. This one has expired.""")
                        lcode_expired = True
                    else:
                        print("""The Security Code is either wrong, or has not
been generated. Please try again with another security code
from the bank. This one has expired.""")
                        lcode_expired = True
                except NameError:
                    print("You must take a loan first...")
                    goto(356)
                except ValueError:
                    print("Type a number!")
                    goto(356)
            elif('exit' in intcom):
                print("Ok. Bye!")
                clear()
                break
            else:
                if('error' in intcom):
                    print("Sorry, we cannot understand what you say.")
                    print("""
Do you mean:
____________
what is error 1?
what is error 2?
what is error 3?
what is error 4?""")
                elif('player shop' in intcom or 'shop' in intcom):
                    print("Sorry, we cannot understand what you say.")
                    print("""
Do you mean:
____________
how to make player shop?
how to fill slots in player shop?
how to claim profit in player shop?
how to upgrade my player shop?
how to change shop size?""")
                elif('limitob' in intcom):
                    print("Sorry, we cannot understand what you say.")
                    print("""
Do you mean:
____________
what are the item limits?""")
                else:
                    print("Sorry, we cannot understand what you say.")
                    print("Our Helper Bot too can't help you. ")
    else:
        print("Sorry, we cannot understand what you say.")