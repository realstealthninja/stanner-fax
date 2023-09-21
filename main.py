# Define the Ceefax pages
pages = {
    100: "Welcome to Ceefax!",
    101: "News Headlines",
    102: "Weather",
    103: "Sports",
    104: "Entertainment",
    105: "Travel",
}

# Define the current page
current_page = 100

# Ceefax program loop
while True:
    # Display the header
    print(f"{' Ceefax ':=^40}")
    print(f"Page {current_page}: {pages.get(current_page, 'Not Found')}\n")
    # Display the content for the current page
    if current_page == 100:
        print("Welcome to Ceefax!")
        print("Press ‘q’ to quit.")
    elif current_page == 101:
        print("News Headlines:")
        print("- Breaking news: Something happened!")
        print("- Another headline: Important stuff!")
    elif current_page == 102:
        print("Weather:")
        print("- Today: Sunny with a high of 25°C")
        print("- Tomorrow: Cloudy with a chance of rain")
    elif current_page == 103:
        print("Sports:")
        print("- Football: Team A vs. Team B - 2-1")
        print("- Tennis: Player X advances to the finals")
    elif current_page == 104:
        print("Entertainment:")
        print("- Movie: New blockbuster now in theaters!")
        print("- Music: Top hits of the week")
    elif current_page == 105:
        print("Travel:")
        print("- Travel advisory: Road closures in the city")
        print("- Airport: Flight delays expected")
    # Display navigation options
    print("\nNavigation:")
    print("Press ‘n’ for the next page.")
    print("Press ‘p’ for the previous page.")
    print("Press ‘q’ to quit.")

    # Get user input
    choice = input("Enter your choice: ").lower()

    # Process user input
    if choice == "q":
        break
    elif choice == "n":
        current_page += 1
        if current_page > max(pages.keys()):
            current_page = min(pages.keys())
    elif choice == "p":
        current_page -= 1
        if current_page < min(pages.keys()):
            current_page = max(pages.keys())
