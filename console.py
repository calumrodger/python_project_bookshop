import pdb
from models.book import Book
from models.publisher import Publisher

import repositories.book_repository as book_repository
import repositories.publisher_repository as publisher_repository

book_repository.delete_all()
publisher_repository.delete_all()

publisher1 = Publisher("Penguin", "London", True)
publisher2 = Publisher("Faber", "London", True)
publisher3 = Publisher("Canongate", "Edinburgh", True)
publisher4 = Publisher("SPAM Press", "Glasgow", True)
publisher5 = Publisher("Wild Hawthorn Press", "Edinburgh", False)

book1 = Book('A Little Larger than the Entire Universe', publisher1, 'Fernando Pessoa', 'poetry', 3, 7.00, 10.99, 'The definitive English translation of the iconic Portugeuse poet.')
book2 = Book('One Hundred Years of Solitude', publisher1, 'Gabriel Garcia Marquez', 'magical realism', 5, 6.00, 10.99, 'One of the greatest novels of the twentieth century - a timeless classic.')
book3 = Book('PORTS', publisher4, 'Calum Rodger', 'poetry', 2, 3.00, 5.00, 'Classic twentieth century poems reimagined as videogame instructions.')
book4 = Book('Rapel', publisher5, 'Ian Hamilton Finlay', 'concrete poetry', 1, 50.00, 150.00, 'Scottish poet''s first concrete poetry collection - ultra rare!')

publisher_repository.save(publisher1)
publisher_repository.save(publisher2)
publisher_repository.save(publisher3)
publisher_repository.save(publisher4)
publisher_repository.save(publisher5)

print(publisher_repository.select_all())

book_repository.save(book1)
book_repository.save(book2)
book_repository.save(book3)
book_repository.save(book4)

print(book_repository.select_all())
book_repository.sell_copy(book2)
publisher_repository.delete_publisher(publisher2)
book_repository.delete_book(book4)

print(book_repository.select_all())
print(publisher_repository.select_all())

# book_repository.delete_all()
# publisher_repository.delete_all()



pdb.set_trace()