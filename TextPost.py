from Post import Post


class TextPost(Post):
    def __init__(self, user, text):
        super().__init__(user)
        self._text = text

    def publish(self):
        print(super().get_creator().get_username() + " published a post:\n" + '"' + self._text + '"')
        print()

    def __str__(self):  # Print the TextPost object
        return (f"{super().get_creator().get_username()} published a post:\n"
                f"\"{self._text}\"\n")
