
import json
import os
from datetime import datetime

HISTORY_FILE = "data/search_history.json"

with open("data/posts.json", "r", encoding="utf-8") as file:
    posts = json.load(file)


def load_history():
    """Load saved searches from the JSON file."""
    if not os.path.exists(HISTORY_FILE):
        return []

    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            history = json.load(file)

        if isinstance(history, list) and all(
            isinstance(item, str) for item in history
        ):
            return history

        print("Search history file has an invalid format.")
        return []

    except (json.JSONDecodeError, OSError):
        print("Could not read search history. Starting with empty history.")
        return []


def save_history(history):
    """Save searches to the JSON file."""
    try:
        with open(HISTORY_FILE, "w", encoding="utf-8") as file:
            json.dump(history, file, indent=4, ensure_ascii=False)
    except OSError:
        print("Could not save search history.")


search_history = load_history()


def search_posts():
    search = input(
        "Enter keyword, hashtag, or year: "
    ).strip().lower()

    if not search:
        print("Search cannot be empty.")
        return

    search_history.append(search)
    save_history(search_history)

    media_filter = input(
        "Show all, photo, or video: "
    ).strip().lower()

    if media_filter not in ["all", "photo", "video"]:
        print("Invalid media type. Choose all, photo, or video.")
        return

    likes_input = input(
        "Minimum likes (0 for all): "
    ).strip()

    if not likes_input.isdigit():
        print("Please enter a valid non-negative number.")
        return

    min_likes = int(likes_input)
    found_posts = []

    for post in posts:
        caption = post["caption"].lower()
        hashtags = " ".join(post["hashtags"]).lower()
        date = post["date"]
        media_type = post["media_type"].lower()
        likes = post["likes"]

        matches_search = (
            search in caption
            or search in hashtags
            or search in date
        )

        matches_media = (
            media_filter == "all"
            or media_type == media_filter
        )

        matches_likes = likes >= min_likes

        if matches_search and matches_media and matches_likes:
            found_posts.append(post)

    if not found_posts:
        print("No matching posts found.")
        return

    print("\nSort by:")
    print("1. Likes (high to low)")
    print("2. Likes (low to high)")
    print("3. Date (newest first)")
    print("4. Date (oldest first)")

    sort_choice = input("Enter your choice (1-4): ").strip()

    if sort_choice == "1":
        found_posts.sort(
            key=lambda post: post["likes"],
            reverse=True
        )
    elif sort_choice == "2":
        found_posts.sort(
            key=lambda post: post["likes"]
        )
    elif sort_choice == "3":
        found_posts.sort(
            key=lambda post: post["date"],
            reverse=True
        )
    elif sort_choice == "4":
        found_posts.sort(
            key=lambda post: post["date"]
        )
    else:
        print("Invalid choice. Choose 1, 2, 3, or 4.")
        return

    photo_count = sum(
        1 for post in found_posts
        if post["media_type"].lower() == "photo"
    )

    video_count = sum(
        1 for post in found_posts
        if post["media_type"].lower() == "video"
    )

    print("\n========== SEARCH SUMMARY ==========")
    print("Total posts found:", len(found_posts))
    print("Photos found:", photo_count)
    print("Videos found:", video_count)
    print("====================================")

    for post in found_posts:
        print("\n--------------------")
        print("Post ID:", post["id"])
        print("Date:", post["date"])
        print("Caption:", post["caption"])
        print("Hashtags:", post["hashtags"])
        print("Type:", post["media_type"])
        print("Likes:", post["likes"])


def view_history():
    print("\n========== SEARCH HISTORY ==========")

    if not search_history:
        print("No search history yet.")
    else:
        for index, search in enumerate(search_history, start=1):
            print(f"{index}. {search}")

    print("====================================")


    
def clear_history():
    global search_history

    if not search_history:
        print("Search history is already empty.")
        return

    confirmation = input(
        "Are you sure you want to clear history? (yes/no): "
    ).strip().lower()

    if confirmation == "yes":
        search_history = []
        save_history(search_history)
        print("Search history cleared successfully.")

    elif confirmation == "no":
        print("Clear history cancelled.")

    else:
        print("Invalid choice. Enter yes or no.")



def remove_history_item():
    if not search_history:
        print("Search history is empty.")
        return

    view_history()

    choice = input(
        "Enter the number to remove (0 to cancel): "
    ).strip()

    if not choice.isdigit():
        print("Please enter a valid number.")
        return

    index = int(choice)

    if index == 0:
        print("Removal cancelled.")
        return

    if index < 1 or index > len(search_history):
        print("Invalid history number.")
        return

    removed_search = search_history.pop(index - 1)
    save_history(search_history)

    print(f"Removed '{removed_search}' from search history.")



def search_by_date_range():
    start_input = input("Enter start date (YYYY-MM-DD): ").strip()
    end_input = input("Enter end date (YYYY-MM-DD): ").strip()

    try:
        start_date = datetime.strptime(
            start_input, "%Y-%m-%d"
        ).date()

        end_date = datetime.strptime(
            end_input, "%Y-%m-%d"
        ).date()

    except ValueError:
        print("Invalid date. Use YYYY-MM-DD, for example 2022-01-01.")
        return

    if start_date > end_date:
        print("Start date cannot be after end date.")
        return

    matching_posts = []

    for post in posts:
        post_date = datetime.strptime(
            post["date"], "%Y-%m-%d"
        ).date()

        if start_date <= post_date <= end_date:
            matching_posts.append(post)

    matching_posts.sort(key=lambda post: post["date"], reverse=True)

    if not matching_posts:
        print("No posts found in this date range.")
        return

    print("\n========== DATE RANGE RESULTS ==========")
    print("Total posts found:", len(matching_posts))

    for post in matching_posts:
        print("\n--------------------")
        print("Post ID:", post["id"])
        print("Date:", post["date"])
        print("Caption:", post["caption"])
        print("Hashtags:", post["hashtags"])
        print("Type:", post["media_type"])
        print("Likes:", post["likes"])





while True:
    print("\n========== INSTAFIND ==========")
    print("1. Search posts")
    print("2. View search history")
    print("3. Clear search history")
    print("4. Remove one search from history")
    print("5. Search posts by date range")
    print("6. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        search_posts()
    elif choice == "2":
        view_history()
    elif choice == "3":
        clear_history()
    elif choice == "4":
        remove_history_item()
    elif choice == "5":
        search_by_date_range()
    elif choice == "6":
        print("Thank you for using InstaFind!")
        break
    else:
        print("Invalid choice. Please choose 1, 2, 3, 4, 5, or 6.")



