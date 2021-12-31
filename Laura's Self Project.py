def main():

    import datetime
    x = datetime.datetime.now()

    name = input("What is your name? ")

    if name == "Laura":
        print("Hello Laura!")
        Laura_age = input("How old are you? ")
        if int(Laura_age) < 40:
            print("You're a Spring Chicken!")
        if int(Laura_age) >= 40:
            print("Life begins at 40 - You're in your prime!")
        main()

    elif name == "Adam":
            print("Hi Adam!")
            day_of_week = input("What day is it today? ")
            is_weekend = "Saturday" or "Sunday"
            if day_of_week == x.strftime("%A") and day_of_week == is_weekend:
                print("Nothing gets past you! Have a great weekend")
            elif day_of_week == x.strftime("%A") and day_of_week != is_weekend:
                print("Nothing gets past you! Have a great day at work")
            elif day_of_week != x.strftime("%A"):
                print("You might want to buy a calendar")
            main()

    elif name == "Serge":
        print("Quack! Try another name!")
        main()

    elif name == "Nick" or "nick":
        number_of_computer_monitors = input("How many computer monitors do you have? ")
        if int(number_of_computer_monitors) <= 2:
            print("That's not too bad.")
        elif int(number_of_computer_monitors) >= 3 and int(number_of_computer_monitors) < 5:
            print("Are you sure you need that many?")
        elif int(number_of_computer_monitors) >= 5:
            print("Are you NASA???")
        print("Try a different name - ")
        main()

    else:
        print("Sorry, wrong person")
        main()

if __name__ == '__main__':
    main()