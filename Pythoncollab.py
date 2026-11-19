
# BUzz - Campus Event & Opportunity Discovery System

import csv
import os
from datetime import datetime


# Sample events
default_events = [
    {
        "id": "1",
        "title": "AI Club Recruitment",
        "category": "AI",
        "date": "20-11-2026",
        "description": "Recruitment for the university AI Club"
    },
    {
        "id": "2",
        "title": "IoT Workshop",
        "category": "IoT",
        "date": "22-11-2026",
        "description": "Hands-on Internet of Things workshop"
    },
    {
        "id": "3",
        "title": "Coding Competition",
        "category": "Programming",
        "date": "25-11-2026",
        "description": "Competitive programming event"
    },
    {
        "id": "4",
        "title": "Astronomy Club Meet",
        "category": "Astronomy",
        "date": "27-11-2026",
        "description": "Discussion about space and astronomy"
    },
    {
        "id": "5",
        "title": "Startup and Innovation Talk",
        "category": "Entrepreneurship",
        "date": "29-11-2026",
        "description": "Talk about startups and innovation"
    }
]


# Save events in CSV file
def save_events(events):

    fields = ["id", "title", "category", "date", "description"]

    with open("events.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(events)


# Load events from CSV file
def load_events():

    if not os.path.exists("events.csv"):
        save_events(default_events)

    with open("events.csv", "r") as file:
        reader = csv.DictReader(file)
        events = list(reader)

    if not events:
        events = default_events.copy()
        save_events(events)

    return events


# Validate date
def valid_date(date):

    try:
        datetime.strptime(date, "%d-%m-%Y")
        return True

    except ValueError:
        return False


# Get date for sorting
def get_date(event):

    try:
        return datetime.strptime(event["date"], "%d-%m-%Y")

    except ValueError:
        return datetime.max


# Display one event
def display_event(event):

    print("\nEvent ID:", event["id"])
    print("Title:", event["title"])
    print("Category:", event["category"])
    print("Date:", event["date"])
    print("Description:", event["description"])
    print("-" * 45)


# View all events
def view_events(events):

    if not events:
        print("\nNo events available.")
        return

    print("\n========== UPCOMING CAMPUS EVENTS ==========")

    sorted_events = sorted(events, key=get_date)

    for event in sorted_events:
        display_event(event)


# Search events
def search_events(events):

    key = input("\nEnter event name or keyword: ").strip().lower()

    if not key:
        print("Please enter a search keyword.")
        return

    found = False

    print("\n========== SEARCH RESULTS ==========")

    for event in events:

        details = (
            event["title"] + " " +
            event["category"] + " " +
            event["description"]
        ).lower()

        if key in details:
            display_event(event)
            found = True

    if not found:
        print("No matching events found.")


# Generate a new event ID
def generate_id(events):

    ids = []

    for event in events:

        if event["id"].isdigit():
            ids.append(int(event["id"]))

    if ids:
        return str(max(ids) + 1)

    return "1"


# Add a new event
def add_event(events):

    print("\n========== ADD A NEW EVENT ==========")

    title = input("Event title: ").strip()
    category = input("Event category: ").strip()
    date = input("Event date (DD-MM-YYYY): ").strip()
    description = input("Event description: ").strip()

    if not title or not category or not description:
        print("\nAll fields must be filled.")
        return

    if not valid_date(date):
        print("\nInvalid date. Please use DD-MM-YYYY.")
        return

    new_event = {
        "id": generate_id(events),
        "title": title,
        "category": category,
        "date": date,
        "description": description
    }

    events.append(new_event)
    save_events(events)

    print("\nEvent added successfully!")
    display_event(new_event)


# Edit an existing event
def edit_event(events):

    event_id = input("\nEnter the Event ID to edit: ").strip()

    for event in events:

        if event["id"] == event_id:

            print("\nCurrent event details:")
            display_event(event)

            print("Enter new details (leave blank to keep existing value).")

            title = input("New title: ").strip()
            category = input("New category: ").strip()
            date = input("New date (DD-MM-YYYY): ").strip()
            description = input("New description: ").strip()

            if date and not valid_date(date):
                print("\nInvalid date. No changes were saved.")
                return

            if title:
                event["title"] = title

            if category:
                event["category"] = category

            if date:
                event["date"] = date

            if description:
                event["description"] = description

            save_events(events)

            print("\nEvent updated successfully!")
            return

    print("\nNo event found with that ID.")


# Delete an existing event
def delete_event(events):

    event_id = input("\nEnter the Event ID to delete: ").strip()

    for event in events:

        if event["id"] == event_id:

            display_event(event)

            confirm = input("Are you sure you want to delete this event? (yes/no): ")
            confirm = confirm.strip().lower()

            if confirm == "yes":

                events.remove(event)
                save_events(events)

                print("\nEvent deleted successfully!")

            else:
                print("\nDeletion cancelled.")

            return

    print("\nNo event found with that ID.")


# Recommend events based on interests
def recommend_events(events):

    print("\n========== DISCOVER EVENTS FOR YOU ==========")

    interest = input(
        "Enter your interests (separate using commas): "
    ).strip().lower()

    interests = [
        item.strip() for item in interest.split(",") if item.strip()
    ]

    if not interests:
        print("Please enter at least one interest.")
        return

    recommendations = []

    for event in events:

        details = (
            event["title"] + " " +
            event["category"] + " " +
            event["description"]
        ).lower()

        score = 0

        for item in interests:

            if item in details:
                score += 1

        if score > 0:
            recommendations.append((score, event))

    recommendations.sort(
        key=lambda x: (-x[0], get_date(x[1]))
    )

    if not recommendations:
        print("\nNo suitable events found.")
        return

    print("\n========== YOUR RECOMMENDATIONS ==========")

    for score, event in recommendations:

        print("\nInterest Match Score:", score)
        display_event(event)


# Display event statistics
def event_statistics(events):

    print("\n========== EVENT STATISTICS ==========")

    if not events:
        print("No event data available.")
        return

    print("\nTotal Events:", len(events))

    categories = {}

    for event in events:

        category = event["category"]

        if category in categories:
            categories[category] += 1

        else:
            categories[category] = 1

    print("\nCategory-wise Event Distribution:")

    for category, count in categories.items():

        print(category, ":", count)

    popular_category = max(categories, key=categories.get)

    print("\nMost Active Category:", popular_category)


# Display available commands
def show_help():

    print("\n========== BUzz COMMANDS ==========")
    print("browse      - View all campus events")
    print("search      - Search for an event")
    print("add         - Add a new event")
    print("edit        - Edit an existing event")
    print("delete      - Delete an event")
    print("recommend   - Get personalized recommendations")
    print("stats       - View event statistics")
    print("help        - Display available commands")
    print("exit        - Close BUzz")
    print("=" * 36)


# Main program
def main():

    events = load_events()

    print("\n==========================================")
    print("                  BUzz")
    print("     CAMPUS EVENT & OPPORTUNITY DISCOVERY")
    print("==========================================")

    print("\nWelcome to BUzz!")
    print("Discover events, explore opportunities and")
    print("stay connected with campus activities.")

    show_help()

    while True:

        command = input("\nBUzz > ").strip().lower()

        if command == "browse":
            view_events(events)

        elif command == "search":
            search_events(events)

        elif command == "add":
            add_event(events)

        elif command == "edit":
            edit_event(events)

        elif command == "delete":
            delete_event(events)

        elif command == "recommend":
            recommend_events(events)

        elif command == "stats":
            event_statistics(events)

        elif command == "help":
            show_help()

        elif command == "exit":
            print("\nThank you for using BUzz!")
            print("Stay curious. Stay connected.")
            break

        elif command == "":
            continue

        else:
            print("\nUnknown command.")
            print("Type 'help' to view available commands.")


# Start the program
main()
