# InstaFind 🔎

**AI-powered social media archive search engine**

InstaFind is a project designed to make it easier to find old social media posts from a large personal archive.

Imagine having **thousands of photos and videos** on a social media account. Finding one old post by continuously scrolling can be difficult and time-consuming.

InstaFind aims to solve this problem by allowing users to search their archived posts using **keywords, dates, hashtags, media type, and eventually AI-powered semantic search**.

---

## 🎯 Problem

Social media platforms can contain thousands of old posts.

For example, if you want to find:

> "That old college farewell post"

you may have to scroll through hundreds or thousands of posts to find it.

InstaFind aims to provide a faster way to search these posts.

---

## 💡 Solution

InstaFind will allow users to search their personal social media archive.

The project will gradually support:

* 🔍 Keyword search
* 📅 Date-based search
* #️⃣ Hashtag search
* 🎥 Media type filtering
* ❤️ Likes-based information
* 🤖 AI-powered semantic search
* 🖼️ Image-based search

---

## 🛠️ Technologies

### Current

* Python
* JSON
* Git & GitHub

### Planned

* HTML
* CSS
* JavaScript
* Flask / FastAPI
* SQLite
* MySQL / PostgreSQL
* Machine Learning
* Sentence Transformers
* Embeddings
* FAISS / Vector Search

---

## 📂 Project Structure

```text
Insta find/
│
├── data/
│   └── posts.json
│
├── backend/
│   └── search.py
│
└── Readme.md
```

---

## 📊 Current Dataset

The current sample dataset contains **20 social media posts**.

Each post contains:

* Post ID
* Username
* Date
* Caption
* Hashtags
* Media type
* Likes

Example:

```json
{
  "id": 1,
  "username": "preetham",
  "date": "2023-05-15",
  "caption": "College farewell memories ❤️",
  "hashtags": ["college", "farewell", "friends"],
  "media_type": "photo",
  "likes": 245
}
```

---

## 🔍 Current Search

The current version supports **basic caption keyword search**.

Example:

```text
Enter search: college
```

The program checks every post and displays posts whose captions contain the searched word.

Example output:

```text
--------------------
Post ID: 1
Date: 2023-05-15
Caption: College farewell memories ❤️
Type: photo
Likes: 245
```

---

## 🚀 Development Progress

### Day 1 — Project Setup ✅

* Created InstaFind project
* Created GitHub repository
* Added initial README
* Created project structure
* Added sample dataset

### Day 2 — Dataset ✅

* Created sample social media archive
* Added 20 posts
* Added captions, hashtags, dates, media types and likes

### Day 3 — Basic Search ✅

* Loaded posts from JSON
* Created Python search program
* Added caption keyword search
* Displayed matching posts

### Upcoming

* **Day 4:** Improve search functionality
* **Day 5:** Hashtag search
* **Day 6:** Date filtering
* **Day 7:** Media type filtering
* Later: Web interface
* Later: Database
* Later: AI semantic search
* Later: Image search

---

## 🧠 Future AI Features

The long-term goal is to make InstaFind more intelligent.

Instead of requiring an exact keyword, users should eventually be able to search naturally.

For example:

```text
Search:
"college memories with friends"
```

The system should understand the meaning of the query and find relevant posts even when the exact words are not present.

This will be implemented using:

* Text embeddings
* Semantic similarity
* Sentence Transformers
* Vector databases/search
* Image embeddings

---

## 🎯 Final Goal

The final goal of InstaFind is to create a **smart personal social media archive search engine** that can quickly find old posts using both traditional filters and AI.

The project will be developed gradually from a simple Python search program into a complete AI-powered application.

---

## 📌 Project Status

**Current Stage:** Early Development 🚧

**Current Version:** Basic Caption Search

---

## 👨‍💻 Author

**Preetham KP**

AI/ML Student | Python Learner | Building InstaFind step by step
