from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from User import User

from abc import ABC, abstractmethod
from Observer import Observer


class Post(ABC):
    # static field that will update the users
    observer = Observer()

    def __init__(self, user_post: User):
        self._like = set()
        self._comment = []
        self._user_post = user_post

        Post.observer.notify_followers(user_post, f"{user_post.get_username()} has a new post")

    def like(self, user: User):
        self._like.add(user.get_username())
        Post.observer.notify_user(self._user_post, user, f"{user.get_username()} liked your post", True)

    def comment(self, user: User, comment: str):
        self._comment.append(user.get_username() + ":" + comment)
        Post.observer.notify_user(self._user_post, user, f"{user.get_username()} commented on your post", True,
                                  f": {comment}")

    def get_creator(self):
        return self._user_post

    @abstractmethod
    def publish(self):
        pass
