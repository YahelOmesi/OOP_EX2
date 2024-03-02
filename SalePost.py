from Post import Post


class SalePost(Post):

    def __init__(self, user, product: str, price, location: str):
        super().__init__(user)
        self._product = product
        self._price = price
        self._location = location
        self._isAvailable = True

    def publish(self):
        print(f"{super().get_creator().get_username()} posted a product for sale:\n"
              f"For sale! {self._product}, price: {self._price}, pickup from: {self._location}")
        print()

    # We will not allow you to use the discount if an incorrect password is entered
    def discount(self, numOfDiscount: int, password):
        if password != self._user_post.get_password():
            raise ValueError("The password is incorrect, The discount cannot be made")

        self._price = self._price - (numOfDiscount * self._price) / 100
        print("Discount on " + self._user_post.get_username() + " product! the new price is: " + str(self._price))

    # We will not allow you to use the sold if an incorrect password is entered
    def sold(self, password):
        if password != self._user_post.get_password():
            raise ValueError("Incorrect password. The product cannot be sold.")

        self._isAvailable = False
        print(self._user_post.get_username() + "'s product is sold")

    def __str__(self):  # Print the ImagePost object
        return (f"{super().get_creator().get_username()} posted a product for sale:\n"
                f"Sold! {self._product}, price: {self._price}, pickup from: {self._location}\n")
