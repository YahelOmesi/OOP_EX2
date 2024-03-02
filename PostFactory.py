from ImagePost import ImagePost
from SalePost import SalePost
from TextPost import TextPost


class PostFactory:
    @staticmethod
    def create_post(post_user, post_type, *args):
        if post_type == "Text":
            return TextPost(post_user, *args)
        elif post_type == "Image":
            return ImagePost(post_user, *args)
        elif post_type == "Sale":
            return SalePost(post_user, *args)
        else:
            raise ValueError("Invalid post type")
