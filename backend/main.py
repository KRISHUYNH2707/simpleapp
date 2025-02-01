from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import get_db
from models import Item
import pyodbc

app = FastAPI()

# Create a table if it doesn't exist
def create_table():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='items' AND xtype='U')
        CREATE TABLE items (
            id INT IDENTITY(1,1) PRIMARY KEY,
            name NVARCHAR(50) NOT NULL,
            description NVARCHAR(255)
        )
    """)
    conn.commit()

# Create table on startup
create_table()

origins = [
    "http://localhost:5173",  # Allow frontend to make requests
]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Set allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allow all headers
)

# API to get all items



@app.get("/items")
def get_items():
    conn = get_db()
    print(conn)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items")
    rows = cursor.fetchall()
    return [{"id": row.id, "name": row.name, "description": row.description} for row in rows]

# API to add a new item
@app.post("/items")
def add_item(item: Item):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO items (name, description) VALUES (?, ?)", item.name, item.description)
    conn.commit()
    return {"message": "Item added successfully"}

# API to delete an item by ID
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM items WHERE id = ?", item_id)
    conn.commit()
    return {"message": "Item deleted successfully"}

@app.get("/test-cors")
def test_cors():
    return {"message": "CORS is enabled"}