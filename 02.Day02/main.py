def main():
    # Greetings
    print("=====WELCOME TO THE TIP CALCULATOR=====")
    
    # User Input
    total_bill = float(input("What was the total bill? "))
    tip = float(input("How much tip would you like to give (%)? (Put any number) "))
    tip_convert = tip/100
    tip_amount = float(total_bill) * tip_convert
    print(f"Your tip amount is {int(tip_amount) if tip_amount.is_integer() else f'{tip_amount:.2f}'}")
    
    # Total
    total_amount = float(total_bill + tip_amount)
    
    # Results
    print(f"Your total amount with tip is {int(total_amount) if total_amount.is_integer() else f'{total_amount:.2f}'}")
    
main()