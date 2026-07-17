from backend.database.vector_store import vector_store

collection = vector_store.get_collection()

print("Collection:", collection.name)
print("Documents:", collection.count())