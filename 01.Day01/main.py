def main():
    print("=====Welcome to our name generator=====\n")
    print("Start from your name!\n")
    
    # User input
    nama = input("What is your name? ").capitalize()
    makanan = input("What is your favorite food? ").capitalize()
    city = input("Where did you live? ").capitalize()
    
    # Combining together
    print(f"Your combined name could be {nama} {makanan} {city}, it is good right? \n")
    
    # Thankyou
    print("The program has been done!\n")
    print("=====Goodbye and have a great day!=====")

main()