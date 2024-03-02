from PostFactory import PostFactory


class User:

    def __init__(self, username, password):
        if len(password) < 4 or len(password) > 8:
            raise ValueError("password must be between 4 and 8 characters")

        self._username = username
        self._password = password

        self._num_of_posts = 0
        self._followers = set()  # Prevents duplicate followers
        self._notification = []  # List of strings

    def follow(self, user_to_follow: "User"):
        user_to_follow._followers.add(self)
        print(self._username + " started following " + user_to_follow._username)

    def unfollow(self, user_to_unfollow: "User"):
        user_to_unfollow._followers.remove(self)
        print(self._username + " unfollowed " + user_to_unfollow._username)

    def publish_post(self, post_type, *args):
        post_user = self
        post = PostFactory.create_post(post_user, post_type, *args)  # creating the appropriate post
        post.publish()
        self._num_of_posts += 1
        return post

    def print_notifications(self):
        print(self._username + "'s notifications:")
        for notification in self._notification:
            print(str(notification))

    def get_username(self) -> str:
        return self._username

    def get_password(self) -> str:
        return self._password

    def get_followers(self) -> set:
        return self._followers

    def update(self, msg: str, need_print: bool = False, extra_msg: str = ""):
        self._notification.append(msg)
        if need_print:
            print(f"notification to {self._username}: {msg}{extra_msg}")

    def __str__(self):  # Print the User object
        return (f"User name: {self._username}, Number of posts: {self._num_of_posts}, Number of followers: "
                f"{len(self._followers)}")
