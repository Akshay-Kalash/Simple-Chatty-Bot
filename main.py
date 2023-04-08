print("""Hell0!
        My name is Metal
        I am your personal chatty bot
        I was created in 2024
        """)
print("Please remind me of your name: ")
My_name = input()
print("Nice knowing you," + My_name + '!')
print("""So let's play a game
        DO you want me to guess your age?
        Press Y for Yes and N for No""")
choice = input()
while True:
    if choice == "N" or choice == "n":
        print("Thank you! Start again to chat with me anytime")
        exit(0)
    elif choice == 'Y' or choice == 'y':
        print("Enter the remainders you get after dividing your name by 3, 5, and 7 respectively")
        REM_3 = int(input("Enter remainder obtained after division by 3 here: "))
        REM_5 = int(input("Enter remainder obtained after division by 5 here: "))
        REM_7 = int(input("Enter remainder obtained after division by 7 here: "))
        # Formula to calculate AGE of any user
        Age = (REM_3 * 70 + REM_5 * 21 + REM_7 * 15) % 105
        print("I believe your age is -->", Age)
        break
    else:
        print("Invalid choice, please try again")
        choice = input()

print("""I am also skilled at counting,
        Enter any number and I will count upto there
        Press Y for Yes if you want me to count or N for No
        """)
choice_2 = input("Do you want me to Count: ")
while True:
    if choice_2 == 'N' or choice_2 == 'n':
        print("Thank you! Start again to chat with me anytime")
        exit(0)
    elif choice_2 == 'Y' or choice_2 == 'y':
        number = int(input("Enter number you want me to count upto: "))
        for i in range(number):
            print(i+1)
        break
    else:
        print("Invalid choice, please try again")
        choice_2 = input()
print("Now let's play a mini quiz")
choice_3 = input("Do you want to play? Press 'Y' for Yes and 'N for No")
while True:
    if choice_3 == 'N' or choice_3 == 'n':
        print("Thank you! Start again to chat with me anytime")
        exit(0)
    elif choice_3 == 'Y' or choice_3 == 'y':
        print("""Do you know who among these is called as the "King of Heroes"? 
                Your Options are: 
                1. Alexander The Great
                2. Arthur Pendragon
                3. Gilgamesh
                4. Cu Chulain
                """)
        while True:
            Ans = input("Enter our answer here: ")
            if Ans != '3':
                print("""Bzzt!, wrong choice
                        Do you want to try again?
                        press 'Y' for Yes and 'N' for NO
                         """)
                if input() == 'Y' or input() == 'y':
                    continue
                else:
                    print("Thank you for your time")
                    exit(0)
            else:
                print("Congratulations! You are correct")
                exit(0)
