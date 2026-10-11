
import json

with open("data/posts.json", "r", encoding="utf-8") as file:
    posts = json.load(file)

search = input("Enter keyword, hashtag, or year: ").strip().lower()

if not search:
    print("Search cannot be empty.")

else:
    media_filter = input("Show all, photo, or video: ").strip().lower()

    if media_filter not in ["all", "photo", "video"]:
        print("Invalid media type. Choose all, photo, or video.")

    else:
        likes_input = input("Minimum likes (0 for all): ").strip()

        if not likes_input.isdigit():
            print("Please enter a valid non-negative number.")

        else:
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

            if found_posts:
                for post in found_posts:
                    print("\n--------------------")
                    print("Post ID:", post["id"])
                    print("Date:", post["date"])
                    print("Caption:", post["caption"])
                    print("Hashtags:", post["hashtags"])
                    print("Type:", post["media_type"])
                    print("Likes:", post["likes"])

                print("\nTotal posts found:", len(found_posts))

            else:
                print("No matching posts found.")
