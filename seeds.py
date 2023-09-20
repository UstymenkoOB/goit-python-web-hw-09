import json 
import connect
from models import Author, Quote


with open("authors.json", "r", encoding="utf-8") as json_file:
    authors_data = json.load(json_file)

for author_info in authors_data:
    author = Author(
        fullname=author_info["fullname"],
        born_date=author_info["born_date"],
        born_location=author_info["born_location"],
        description=author_info["description"]
    )
    author.save()


with open("quotes.json", "r", encoding="utf-8") as json_file:
    quotes_data = json.load(json_file)

for quote_info in quotes_data:
    author_name = quote_info["author"]
    author = Author.objects.get(fullname=author_name)
    quote = Quote(
        tags=quote_info["tags"],
        author=author,
        quote=quote_info["quote"]
    )
    quote.save()

print("Дані вставлено успішно.")
