from pydantic import BaseModel

# Pydantic model for request/response validation
class Item(BaseModel):
    name: str
    description: str