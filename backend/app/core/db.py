import logging
from typing import Optional, Dict, Any
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from app.core.config import settings

logger = logging.getLogger("CampusOS.DB")

class InMemoryDatabase:
    """In-memory database fallback for environments where MongoDB is offline."""
    def __init__(self):
        self.collections: Dict[str, Dict[str, Any]] = {}

    def get_collection(self, name: str):
        if name not in self.collections:
            self.collections[name] = {}
        return InMemoryCollection(self.collections[name])

class InMemoryCollection:
    def __init__(self, store: Dict[str, Any]):
        self.store = store

    async def insert_one(self, document: Dict[str, Any]):
        doc_id = document.get("id") or document.get("_id") or str(len(self.store) + 1)
        doc = {**document, "_id": doc_id, "id": doc_id}
        self.store[str(doc_id)] = doc
        class InsertResult:
            inserted_id = doc_id
        return InsertResult()

    async def find_one(self, query: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        for item in self.store.values():
            match = True
            for k, v in query.items():
                if item.get(k) != v:
                    match = False
                    break
            if match:
                return item
        return None

    async def update_one(self, query: Dict[str, Any], update: Dict[str, Any], upsert: bool = False):
        doc = await self.find_one(query)
        if doc:
            if "$set" in update:
                doc.update(update["$set"])
        elif upsert:
            new_doc = query.copy()
            if "$set" in update:
                new_doc.update(update["$set"])
            await self.insert_one(new_doc)

    def find(self, query: Dict[str, Any] = None):
        query = query or {}
        results = []
        for item in self.store.values():
            match = True
            for k, v in query.items():
                if item.get(k) != v:
                    match = False
                    break
            if match:
                results.append(item)
        class AsyncCursor:
            def __init__(self, data):
                self.data = data
            def __aiter__(self):
                self.iter = iter(self.data)
                return self
            async def __anext__(self):
                try:
                    return next(self.iter)
                except StopIteration:
                    raise StopAsyncIteration
            async def to_list(self, length: int = 100):
                return self.data[:length]
        return AsyncCursor(results)

class DatabaseManager:
    client: Optional[AsyncIOMotorClient] = None
    db: Any = None
    is_connected: bool = False

    async def connect(self):
        try:
            self.client = AsyncIOMotorClient(settings.MONGODB_URL, serverSelectionTimeoutMS=2000)
            # Ping to verify connection
            await self.client.admin.command('ping')
            self.db = self.client[settings.DATABASE_NAME]
            self.is_connected = True
            logger.info(f"Connected to MongoDB at {settings.MONGODB_URL}")
        except Exception as e:
            logger.warning(f"MongoDB connection failed ({e}). Falling back to In-Memory DB Store.")
            self.db = InMemoryDatabase()
            self.is_connected = False

    async def disconnect(self):
        if self.client:
            self.client.close()
            logger.info("MongoDB client closed")

db_manager = DatabaseManager()

def get_db():
    return db_manager.db
