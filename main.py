print("Welcome to the dating calculator!")
you = input("What is your name? \n")
your_lover = input("What is your crush's name? \n")
print("Your love score is:" + str(len(you) * len(your_lover) * 10) + "%")
print("Congratulaiton! You are a perfect match!")