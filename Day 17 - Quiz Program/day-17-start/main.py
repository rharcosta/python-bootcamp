# PascalCase: Class name - camelCase - snake_case: every thing else

class User:
    # pass: just to ignore Python errors when creating empty actions

    # function to initialize the variables
    # everytime an object is created, the class is initialized
    def __init__(self, user_id, username):
        # print("New user being created...")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):  # self is me. User is the other person
        self.following += 1  # I started following someone
        user.followers += 1  # the user received a follow


user_1 = User("001", "Rubia")
# user_1.id = "001"
# user_1.username = "rubia"
print(user_1.followers)

user_2 = User("002", "Pedro")
# user_2.id = "002"
# user_2.username = "pedro"
print(user_2.username)

# attributes: what the user HAS
# methods: what the user DOES

user_1.follow(user_2)  # user_1 started following user_2
print(user_1.following)  # user_1 is following one person
print(user_1.followers)  # user_1 doesn't have followers
print(user_2.following)  # user_2 is not following anyone
print(user_2.followers)  # user_2 have one follower
