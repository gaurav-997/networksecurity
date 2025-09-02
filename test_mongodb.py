import certifi
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://chauhan7gaurav_db_user:Admin123@cluster0.c2n9ytd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(
    uri,
    server_api=ServerApi('1'),
    tls=True,
    tlsCAFile=certifi.where()
)

try:
    client.admin.command('ping')
    print("✅ Pinged your deployment. Successfully connected to MongoDB Atlas!")
except Exception as e:
    print("❌ Connection failed:", e)
