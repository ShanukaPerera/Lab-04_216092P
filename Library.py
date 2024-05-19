print("Hello World")
book = "Oliver Twist"
print(book)

from book import book
from member import Member
book_1 = book ("A" , "A B Perera", 1000)
book_2 = book ("B" , "C D Silva", 2000)
memeber_1 = Member ("Kavindu" , 216015)
memeber_2 = Member ("Pasan" , 216020)

print(book_1.name)
print(book_2.price)
print(member_1.member_id)
print(member_2.member_id)
