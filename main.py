# Define the Ceefax pages
pages = {
    100: {
        "title":   "Welcome to CeeFax\n\n\n",
        "content":
        """
When CEEFAX started in 1974, it was the first teletext facility in the world - enabling the viewer to "see facts" - and the start of interacti
ve television services that are now taken for granted. CEEFAX was developed two years earlier by BBC engineers who exploited the unused capacity of the 625 line television signal to send information. The text could be displayed instead of the television picture or overlaying it, and accessed at the touch of a button.CEEFAX was a minority interest at first, as a new television was needed to receive it, but the popularity of rented televisions, which could easily be upgraded, ensured uptake steadily increased. The service received a great boost once gaps in the television schedule began to be filled with a selection of pages from CEEFAX, accompanied by music. Eventually it had 22 million weekly users.
    Apart from news and sport coverage, including chess and racing, CEEFAX offered pages of weather, music reviews, travel information, jokes and even an alarm clock. At its height as many as 600 pages were available.
    As part of the analogue television signal, CEEFAX was discontinued when the network became digital-only in 2012, but more advanced interactive services such as the Red Button and BBC.co.uk are its spiritual successors. 
    """
        },
    # 101: "News Headlines",
    # 102: "Weather",
    # 103: "Sports",
    # 104: "Entertainment",
    # 105: "Travel",
}

# Define the current page
current_page: int = 100
user_input: str = ""

# Ceefax program loop
while user_input != "q":
    print(pages[current_page]["title"])
    print(pages[current_page]["content"])

    # Display navigation options
    print("\nNavigation:")
    print("Press ‘n’ for the next page.")
    print("Enter page number to reach the specified page")
    print("Press ‘p’ for the previous page.")
    print("Press ‘q’ to quit.")
    user_input = input("Enter your choice: ").lower()

    if user_input == "n":
        current_page += 1
        if current_page > max(pages.keys()):
            current_page = min(pages.keys())
    elif user_input == "p":
        current_page -= 1
        if current_page < min(pages.keys()):
            current_page = max(pages.keys())
    elif user_input.isdigit() and int(user_input) in pages.keys():
        current_page = int(user_input)
