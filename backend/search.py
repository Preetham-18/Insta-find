import json

with open("data/posts.json", "r", encoding="utf-8") as file:
     posts = json.load(file)

search = input("Enter search: ")

for post in posts:
    if search.lower() in post["caption"].lower():
        print("\n--------------------")
        print("Post ID:", post["id"])
        print("Date:", post["date"])
        print("Caption:", post["caption"])
        print("Type:", post["media_type"])
        print("Likes:", post["likes"])