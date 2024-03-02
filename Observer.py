from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from User import User


class Observer:

    def notify_user(self, user_to_notify: User, notifier: User, msg: str, need_print: bool = False,
                    extra_msg: str = ""):
        if user_to_notify == notifier:  # We don't want to update ourselves
            return

        user_to_notify.update(msg, need_print, extra_msg)

    def notify_followers(self, user: User, msg: str, need_print: bool = False):
        for follower in user.get_followers():  # For each follower from the follower list
            self.notify_user(follower, user, msg, need_print)
