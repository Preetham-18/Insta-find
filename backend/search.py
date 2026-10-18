
import json

with open("data/posts.json", "r", encoding="utf-8") as file:
    posts = json.load(file)

search_history = []


def search_posts():
    search = input(
        "Enter keyword, hashtag, or year: "
    ).strip().lower()

    if not search:
        print("Search cannot be empty.")
        return

    search_history.append(search)

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


while True:
    print("\n========== INSTAFIND ==========")
    print("1. Search posts")
    print("2. View search history")
    print("3. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        search_posts()
    elif choice == "2":
        view_history()
    elif choice == "3":
        print("Thank you for using InstaFind!")
        break
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
