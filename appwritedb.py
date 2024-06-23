from appwrite.client import Client
from appwrite.query import Query
from appwrite.services.databases import Databases
from appwrite.id import ID

client = Client()
client.set_endpoint('https://cloud.appwrite.io/v1')
client.set_project('PROJECT_ID')
client.set_key('API_KEY')

databases = Databases(client)
collection_id = "COLLECTION_ID"
db_id = "DATABASE_ID"

def add_history(ask, prompt, answer, user_id):
    """Asynchronously adds a document to the database."""
    print("Adding document to database...")
    databases.create_document(
        database_id=db_id,
        collection_id=collection_id,
        document_id=ID.unique(),
        data={
            "ask": ask,
            "prompt": prompt,
            "answer": answer,
            "user_id": user_id,
        }
    )
    print("Created document!")

def fetch_user_history(user_id):
    documents = databases.list_documents(
        db_id,
        collection_id,
        [
            Query.equal("user_id", user_id)
            
        ]
    )
    results=[]
    for doc in documents['documents']:
        results.append(doc)
    return results
