# 7. Write a program that will calculate the price for a quantity entered from the keyboard, given that the unit price is Rs 5 and there is a discount of 10 percent for quantities over 30 and a 15 percent discount for quantities over 50.

og_price = 5


quantity=int(input("Enter order quantity to know the price (There is a discount of 10 percent for quantities over 30 and a 15 percent discount for quantities over 50.): "))

if quantity>30:
    if quantity>50:
        final_price=(og_price*quantity)-((og_price*quantity)*0.15)
        print(f"Final price is: {final_price}")
    else:
        final_price=(og_price*quantity)-((og_price*quantity)*0.1)
        print(f"Final price is: {final_price}")
else:
    final_price=(og_price*quantity)
    print(f"Final price is: {final_price}")

