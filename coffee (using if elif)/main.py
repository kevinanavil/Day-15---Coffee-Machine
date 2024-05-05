import coffee_data

resources = coffee_data.resources
menu = coffee_data.MENU
resources['money'] = 0
end_machine = False

while end_machine == False:

    coffee = input("What would you like? (espresso/latte/cappuccino):\n")

    if coffee == "off":
        end_machine = True

    elif coffee == "report":
        print(f"water : {resources['water']} ml")
        print(f"milk : {resources['milk']} ml")
        print(f"coffee : {resources['coffee']} ml")
        print(f"money : ${resources['money']}\n")

    else:
        if coffee == "1":
            coffee = "espresso"
        elif coffee == "2":
            coffee = "latte"
        elif coffee == "3":
            coffee = "cappuccino"        
        coffee_type = menu[coffee]
        water = coffee_type['ingredients']['water']

        if coffee == "espresso":
            milk = coffee_type['ingredients']['milk'] = 0
        else:
            milk = coffee_type['ingredients']['milk']
            
        powder = coffee_type['ingredients']['coffee']
        price = coffee_type['cost']
        resources['water'] -= water
        resources['milk'] -= milk
        resources['coffee'] -= powder
        resources['money'] += price
        
        if resources['water'] < 0 or resources['milk'] < 0 or resources['coffee'] < 0 or resources['money'] < 0:
            print("Sorry we're out of order TT")
            end_machine = True
        else:
            print(f"It's ${coffee_type['cost']}")
            quarters = input("quarters($0.25) = $")
            dimes = input("dimes($0.10) = $")
            nickels = input("nickels($0.05) = $")
            pennies = input("pennies($0.01) = $")
            pay = int(quarters) + int(dimes) + int(nickels) + int(pennies)

            if price > pay:
                print("Not enough, order it again!")
                end_machine = True
            
            else:
                print(f"\nHere you {coffee.capitalize()}. Enjoy!")
                print(f"Here you change ${pay-price}. Thankyou!\n")
