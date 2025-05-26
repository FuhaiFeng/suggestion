import json
import requests

def main():
    while True:
        print("\nSelect an option:")
        print("1. Generate a suggestion")
        print("2. Exit")
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            try:
                response = requests.get("http://localhost:8000/suggestion")
                response.raise_for_status()
                pretty_response = json.dumps(response.json(), indent=4)
                print("Response:")
                print(pretty_response)
            except requests.RequestException as e:
                print("An error occurred:", e)
        elif choice == "2":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()