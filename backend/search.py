import json

with open("data/posts.json", "r", encoding="utf-8") as file:
    posts = json.load(file)

search = input("Enter search: ").lower()

for post in posts:

    caption = post["caption"].lower()
    hashtags = " ".join(post["hashtags"]).lower()

    if search in caption or search in hashtags:
        print("\n--------------------")
        print("Post ID:", post["id"])
        print("Date:", post["date"])
        print("Caption:", post["caption"])
        print("Hashtags:", post["hashtags"])
        print("Type:", post["media_type"])
        print("Likes:", post["likes"])