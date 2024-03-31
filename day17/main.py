class User:
        def __init__(self, id, username) -> None:
                self.id = id
                self.username = username
                self.followers = 0
                self.following = 0

        def follow(self, user):
                user.followers += 1
                self.following += 1


user_1 = User("001", "Ben")
user_2 = User("002", "Josh")
user_1.follow(user_2)

print(user_1.following)
print(user_2.followers)