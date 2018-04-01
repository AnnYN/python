def make_pizza (size,*toppings):
    print("\nMaking a "+str(size)+"--inch with following toppings：")
    for topping in toppings:
        print("-"+topping)
make_pizza(12,'apple','orage','egg')