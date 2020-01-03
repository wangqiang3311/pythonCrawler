import pymongo
client=pymongo.MongoClient()
db=client.pagers
collection=db.books
book={"author":"wbq",
"text":["c#","python"]
}
book_id=collection.insert_one(book)
print("插入后的Id: %s" %book_id)

books=[{"author":"wbq1",
"text":["web api","java"]
},
{
    "author":"wbq3311",
    "text":["lua","F#"]
}
]
collection.insert_many(books)

b=collection.find_one({"author":"wbq"})
print(b)
for book in collection.find({"author":"wbq"}):
    print(book)

count=collection.find({"author":"wbq"}).count()
print(count)

collection.delete_many({"author":"Mike"})

