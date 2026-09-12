print("Welcome to our ATM Machine ")
balance= 10000

while True:

    print("1. Cheak Balance")
    print("2. Deposit")
    print("3. Withdraw ")
    print("4. Exit ")

    choice = input("Enter your choice (1/2/3/4): ")  
    if choice in ['1','2','3','4']:
                try:
                    if choice=='1':
                            print("Your current Bank Account Balance is :",balance)
                    elif choice=='2':
                        deposit=int(input("Enter the Amount You want to deposit : "))
                        balance=deposit+balance
                        print(balance)
                    elif choice=='3':
                        withdraw=int(input("Enter The Amount You Want TO Withdraw : "))  
                        if withdraw>balance:
                            print("insufficient Balance")
                        else:
                            balance = balance - withdraw
                            print("Your remaining balance:", balance)
                        
                    elif choice=='4':
                        print("Exit , thank you")
                        break
                except ValueError:
                    print("Invalid Input")     
    else:
            print("Invalid Input ")             
            


                
