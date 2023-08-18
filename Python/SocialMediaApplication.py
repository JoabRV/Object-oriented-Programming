class User:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
        self.friends = []

    def add_friend(self, friend):
        self.friends.append(friend)


class Post:
    def __init__(self, author, content):
        self.author = author
        self.content = content
        self.comments = []

    def add_comment(self, comment):
        self.comments.append(comment)


class Comment:
    def __init__(self, author, text):
        self.author = author
        self.text = text


# Using the classes
user1 = User("Alice", 25, "New York")
user2 = User("Bob", 30, "Los Angeles")
user1.add_friend(user2)

post = Post(user1, "Hello, world!")
comment = Comment(user2, "Hello, Alice!")
post.add_comment(comment)
