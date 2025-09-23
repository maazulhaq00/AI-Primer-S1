class Book:
    def __init__(self, title, author, rating, price):
        self.title = title
        self.author = author
        self.rating = rating
        self.price = price
    
    def show_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Rating: {self.rating}")
        print(f"Price: Rs. {self.price}")

class eBook(Book): # inheritance
    def __init__(self, title, author, rating, price, download_url):
        super().__init__(title, author,rating,price)
        self.download_url = download_url

    def show_details(self): # polymorphism
        super().show_details()
        print(f"Download Link: {self.download_url}")


eb1 = eBook("The Story of a town", "Maaz Ul Haq", 2.1, 23, "http://yahoo.com/abc.pdf")

eb1.show_details()


