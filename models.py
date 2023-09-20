from mongoengine import Document
from mongoengine.fields import ListField, StringField, ReferenceField


class Author(Document):
    fullname = StringField(max_length=150)
    born_date = StringField(max_length=50)
    born_location = StringField(max_length=100)
    description = StringField()
    meta = {"collection": 'authors'}


class Quote(Document):
    tags = ListField(StringField(max_length=40))
    author = ReferenceField(Author)
    quote = StringField()
    meta = {"collection": 'quotes'}
