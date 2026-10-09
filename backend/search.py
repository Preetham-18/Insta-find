
import json

with open("data/posts.json", "r", encoding="utf-8") as file:
    posts = json.load(file)

search = input("Enter keyword, hashtag, or year: ").lower()
media_filter = input("Show all, photo, or video: ").lower()

for post in posts:
    caption = post["caption"].lower()
    hashtags = " ".join(post["hashtags"]).lower()
    date = post["date"]
    media_type = post["media_type"].lower()

    matches_search = (
        search in caption
        or search in hashtags
        or search in date
    )

    matches_media = (
        media_filter == "all"
        or media_type == media_filter
    )

    if matches_search and matches_media:
        print("\n--------------------")
        print("Post ID:", post["id"])
        print("Date:", post["date"])
        print("Caption:", post["caption"])
        print("Hashtags:", post["hashtags"])
        print("Type:", post["media_type"])
        print("Likes:", post["likes"])