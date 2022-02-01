import pdb
from models.book import Book
from models.publisher import Publisher

import repositories.book_repository as book_repository
import repositories.publisher_repository as publisher_repository

book_repository.delete_all()
publisher_repository.delete_all()

publisher1 = Publisher("Penguin", "London", True)
publisher2 = Publisher("Faber", "London", True)
publisher3 = Publisher("Carcanet", "Manchester", True)
publisher4 = Publisher("SPAM Press", "Glasgow", True)
publisher5 = Publisher("Migrant", "Ventura", False)
publisher6 = Publisher("Pee Pal Tree Press", "Leeds", True)
publisher7 = Publisher("Shearsman", "Bristol", True)
publisher8 = Publisher("HVTN Press", "Birmingham", True)
publisher9 = Publisher("Chambers", "Edinburgh", True)
publisher10 = Publisher("Tapsalteerie", "Alford", True)
publisher11 = Publisher("Broken Sleep", "Talgarreg", True)
publisher12 = Publisher("Blue Diode", "Leith", True)
publisher13 = Publisher("University of California Press", "L.A.", True)
publisher14 = Publisher("DABA", "New York", True)
publisher15 = Publisher("sorry house", "New York", False)


book1 = Book('A Little Larger Than the Entire Universe: Selected Poems', publisher1, 'Fernando Pessoa', 'visionary', 3, 7.00, 10.99, 'The definitive English translation of the iconic Portugeuse poet.', "https://i.imgur.com/jsnrud2.jpg")
book2 = Book('I Have More Souls Than One', publisher1, 'Fernando Pessoa', 'visionary', 3, 7.00, 10.99, "Sublime slim volume of Pessoa's works. Includes 'Tobacconist'!", "https://i.imgur.com/7b2GIuB.jpg")
book3 = Book('On Love and Barley - Haiku of Basho', publisher1, 'Basho', 'haiku', 3, 7.00, 10.99, "The master at work.", "https://i.imgur.com/b3GKqlJ.jpg")
book4 = Book('Selected Poems 1923-1958', publisher2, 'e.e. cummings', 'modernist', 5, 6.00, 10.99, "America's most funnest modernist.", "https://i.imgur.com/N7U6SYQ.jpg")
book5 = Book('Aimed at Nobody', publisher2, 'W.S. Graham', 'modernist', 3, 7.00, 10.99, "A B-side compilation if you will.", "https://i.imgur.com/E0S0jnA.jpg")
book6 = Book('Selected Poems: in Five Sets', publisher2, 'Laura Riding', 'modernist', 3, 7.00, 10.99, "What's she like, eh.", "https://i.imgur.com/b1u6kK6.jpg")
book7 = Book('Venus as a Bear', publisher3, 'Vahni Capildeo', 'lyric', 3, 7.00, 10.99, "Capildeo's lyric apogee.", "https://i.imgur.com/Pcnz1IQ.jpg")
book8 = Book('The Lost Lunar Baedeker', publisher3, 'Mina Loy', 'avant-garde', 3, 7.00, 10.99, "The revolutionary Dada spirit - electrifying stuff.", "https://i.imgur.com/y5GR01c.jpg")
book9 = Book('PORTS', publisher4, 'Calum Rodger', 'lyric', 2, 3.00, 5.00, "Classic twentieth century poems reimagined as videogame instructions.", "https://i.imgur.com/cvI5RBr.jpg")
book10 = Book('The Dancers Inherit the Party', publisher5, 'Ian Hamilton Finlay', 'lyric', 2, 3.00, 5.00, "Super-rare!", "https://i.imgur.com/gOQtR3W.jpg")
book11 = Book('Utter', publisher6, 'Vahni Capildeo', 'lyric', 2, 3.00, 5.00, "Early collection from Capildeo - playful but dark.", "https://i.imgur.com/13HcmKw.jpg")
book12 = Book('Urn & Drum', publisher7, 'Lila Matsumoto', 'lyric', 2, 3.00, 5.00, "What's it like to be like an object? These are poems.", "https://i.imgur.com/wkzUvUe.jpg")
book13 = Book('The Continued Closure of the Blue Door', publisher8, 'Vik Shirley', 'surrealist', 2, 3.00, 5.00, "Hilarious and gnarly prose poems.", "https://i.imgur.com/8DCRaNX.jpg")
book14 = Book("The Honour'd Shade: An Anthology of New Scottish Poetry", publisher9, 'Norman MacCaig', 'Scots language', 2, 3.00, 5.00, "In some respects an embarrassing inheritance, but it has its moments.", "https://i.imgur.com/GtxgRCM.jpg")
book15 = Book("makar/unmakar: twelve contempoary poets in scotland", publisher10, 'Calum Rodger', 'avant-garde', 2, 3.00, 5.00, "The best avant-'radge' poetry in Scotland today.", "https://i.imgur.com/SwkRSsN.jpg")
book16 = Book("Hit Points: An Anthology of Video Game Poetry", publisher11, 'Matthew Haigh', 'video game', 2, 3.00, 5.00, "Poetry meets videogames - lovely stuff.", "https://i.imgur.com/FCssc8F.jpg")
book17 = Book("A Decade of Cu ts", publisher12, 'Nicky Melville', 'concrete', 2, 3.00, 5.00, "Amazing retrospective of the Edinburgh poet.", "https://i.imgur.com/1veQxry.jpg")
book18 = Book("Selections", publisher13, 'Ian Hamilton Finlay', 'concrete', 2, 3.00, 5.00, "The perfect introduction to this seminal poet.", "https://i.imgur.com/PHpoI4H.jpg")
book19 = Book('EECCHHOOEESS', publisher14, 'n.h. pritchard', 'concrete', 3, 7.00, 10.99, "Stunning re-publication of an overlooked classic of American concrete poetry.", "https://i.imgur.com/bvR2mrP.jpg")
book20 = Book('i will never be beautiful enough to make us beautiful together', publisher15, 'Mira Gonzalez', 'alt lit', 3, 7.00, 10.99, "So-called 'alt' poetics at its zenith - peak millennial.", "https://i.imgur.com/i9srcHh.jpg")




publisher_repository.save(publisher1)
publisher_repository.save(publisher2)
publisher_repository.save(publisher3)
publisher_repository.save(publisher4)
publisher_repository.save(publisher5)
publisher_repository.save(publisher6)
publisher_repository.save(publisher7)
publisher_repository.save(publisher8)
publisher_repository.save(publisher9)
publisher_repository.save(publisher10)
publisher_repository.save(publisher11)
publisher_repository.save(publisher12)
publisher_repository.save(publisher13)
publisher_repository.save(publisher14)
publisher_repository.save(publisher15)

print(publisher_repository.select_all())

book_repository.save(book1)
book_repository.save(book2)
book_repository.save(book3)
book_repository.save(book4)
book_repository.save(book5)
book_repository.save(book6)
book_repository.save(book7)
book_repository.save(book8)
book_repository.save(book9)
book_repository.save(book10)
book_repository.save(book11)
book_repository.save(book12)
book_repository.save(book13)
book_repository.save(book14)
book_repository.save(book15)
book_repository.save(book16)
book_repository.save(book17)
book_repository.save(book18)
book_repository.save(book19)
book_repository.save(book20)


# print(book_repository.select_all())
# book_repository.sell_copy(book2)
# publisher_repository.delete_publisher(publisher2)
# book_repository.delete_book(book4)

# print(book_repository.select_all())
# print(publisher_repository.select_all())

# book_repository.delete_all()
# publisher_repository.delete_all()



pdb.set_trace()