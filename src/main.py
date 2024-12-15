from .api_client import CitiBikeAngelsClient
from .cli import display_top_stations

def main():
    client = CitiBikeAngelsClient()
    
    while True:
        print("\nCiti Bike Angels Points Retrieval")
        print("1. View Top 10 Stations")
        print("2. View Top 20 Stations")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            display_top_stations(client, 10)
        elif choice == '2':
            display_top_stations(client, 20)
        elif choice == '3':
            print("Thank you for using the Citi Bike Angels App!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
