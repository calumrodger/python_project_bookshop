class Book:

    def __init__(self, title, publisher, author, genre, stock, cost_price, sale_price, blurb, image = None, id = None):
        self.title = title
        self.publisher = publisher
        self.author = author
        self.genre = genre
        self.stock = stock
        self.cost_price = cost_price
        self.sale_price = sale_price
        self.blurb = blurb
        self.image = image
        self.id = id

        