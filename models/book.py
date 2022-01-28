class Book:

    def __init__(self, title, publisher_id, author, genre, stock, cost_price, sale_price, markup, blurb, id = None):
        self.title = title
        self.publisher_id = publisher_id
        self.author = author
        self.genre = genre
        self.stock = stock
        self.cost_price = cost_price
        self.sale_price = sale_price
        self.markup = markup
        self.blurb = blurb
        self.id = id