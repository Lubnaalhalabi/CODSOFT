from health_and_wellness import HealthBot
from personal_finance_and_innovation import FinanceBot
from technology_and_innovation import TechBot

def main():
    try:
        print("Choose a bot to interact with:")
        print("1. Health and Wellness")
        print("2. Technology and Innovation")
        print("3. Personal Finance and Investment")
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            bot = HealthBot()
        elif choice == "2":
            bot = TechBot()
        elif choice == "3":
            bot = FinanceBot()
        else:
            print("Invalid choice. Exiting.")
            return 

        bot.introduce_bot()  
    except ImportError as e:
        print(f"An error occurred while importing modules: {e}")
    except AttributeError as e:
        print(f"An error occurred while accessing bot methods: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
