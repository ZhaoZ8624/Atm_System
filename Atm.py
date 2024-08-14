class Atm:
    """
    Initializes the attributes:
        __pin (default: None)
        __balance (default: 0)
    Calls the __menu() method from the constructor.
    """
    def __init__(self):
        self.__pin = None
        self.__balance = 0
        self.__menu()
    """
    __menu uses a loop to display the menu options and take user input.
    Implement logic to call appropriate methods based on user input:
        __generate_pin()
        __change_pin()
        __check_balance()
        __withdraw()
        __deposit()
        Exit the program
    """
    def __menu(self):
        is_on = True
        while is_on:
            print("\n1.Generate PIN\n2.Change PIN\n3.Check Balance\n4.Withdraw\n5.Desposit\n6.Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                result = self.__generate_pin()
                if not result:
                    self.__menu()
                    break
            elif choice == 2:
                result = self.__change_pin()
                if not result:
                    self.__menu()
                    break
            elif choice == 3:
                self.__balance_check()
            elif choice == 4:
                result = self.__withdraw()
                if not result:
                    self.__menu()
                    break
            elif choice == 5:
                result = self.__deposit()
                if not result:
                    self.__menu()
                    break
            elif choice == 6:
                print("Atm System Closing...")
                break
    """
    Prompts user to input a pin, and checks if the pin is valid.
    """
    def __get_pin(self):
        pin = input("Enter your pin: ")
        if len(pin) == 4 and pin.isdigit():
            return int(pin)
        else:
            print("**Invalid PIN**")
            return None
    """
    Prompts user to input a pin, and checks if inputted pin matches the stored pin.
    """
    def __verify_pin(self):
        pin = int(input("Enter your pin: "))
        if self.__pin == pin:
            return True
        else:
            print("**Incorrect PIN**")
            return False
    """
    Prompt the user to enter a new 4-digit PIN and confirm it.
    Ensure the PINs match and set the __pin attribute.
    If the PINs do not match, display an error message.
    If a PIN is already set, inform the user and redirect to the menu.
    """
    def __generate_pin(self):
        if self.__pin is not None:
            print("**PIN has already been set**")
            return False
        pin = self.__get_pin()
        if pin is None:
            return False
        check_pin = int(input("Confirm your pin: "))
        if pin == check_pin:
            self.__pin = check_pin
            print("**Generation Successful**")
            return True
        else:
            print("**Generation Unsuccessful**\n**Please try again later**")
            return False
    """
    Prompt the user to enter and confirm the old PIN.
    If the old PIN is correct, prompt the user to enter and confirm the new 4-digit PIN.
    Ensure the new PINs match and update the __pin attribute.
    If the PINs do not match or the old PIN is incorrect, display an error message.
    """
    def __change_pin(self):
        old_pin = int(input("Enter your old PIN: "))
        if self.__pin != old_pin:
            print("Incorrect PIN")
            return False
        else:
            pin = int(input("**Confirmation Successful**\nPlease enter your new PIN:"))
            if len(pin) != 4 or not pin.isdigit():
                print("**Invalid PIN**")
                return False
            check_pin = int(input("Please Confirm your new PIN:"))
            if pin == check_pin:
                self.__pin = check_pin
                print("**PIN Changed Successfully**")
                return True
            else:
                print("**PIN Change Unsuccessful**\n**Please try again later**")
                return False
    """
    Prompt the user to enter the PIN.
    If the PIN is correct, display the current balance.
    If the PIN is incorrect, display an error message.
    """  
    def __balance_check(self):
        if self.__verify_pin() == True:
            print("Balance: $"+str(self.__balance))
    """
    Prompt the user to enter the PIN and the amount to withdraw.
    Ensure the amount is a multiple of 100 and not more than the current balance.
    If the conditions are met, deduct the amount from the balance and display a success message.
    If the conditions are not met, display an error message.
    """
    def __withdraw(self):
        if self.__verify_pin():
            amount = float(input("Enter the amount to withdraw: "))
            if amount%100 == 0 and amount <= self.__balance:
                self.__balance -= amount
                print("**Withdraw Successful**")
                return True
            else:
                print("**Withdraw Unsuccessful**")
                print("**Amount entered is not a multiple of 100 or exceeds bank balance**")
                return False
    """
    Prompt the user to enter the PIN and the amount to deposit.
    Ensure the amount is a multiple of 100 and greater than 0.
    If the conditions are met, add the amount to the balance and display a success message.
    If the conditions are not met, display an error message.
    """
    def __deposit(self):
        if self.__verify_pin():
            amount = float(input("Enter the amount to deposit: "))
            if amount%100 == 0 and amount > 0 :
                self.__balance += amount
                print("**Deposit Successful**")
                return True
            else:
                print("**Deposit Unsuccessful**")
                print("**Amount entered is not a multiple of 100 or less than or equal to 0**")
                return False
