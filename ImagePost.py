from Post import Post
from matplotlib import image, pyplot as plt


class ImagePost(Post):

    def __init__(self, user, image_url):
        super().__init__(user)
        self.image_url = image_url

    def display(self):
        img = image.imread(self.image_url)
        plt.imshow(img)
        plt.show()
        print("Shows picture")

    def publish(self):
        print(super().get_creator().get_username() + " posted a picture\n")

    def __str__(self):  # Print the ImagePost object
        return f"{super().get_creator().get_username()} posted a picture\n"
