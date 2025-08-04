
# What is Pydantic?
# Pydantic is a Python library for data validation and settings management using Python type annotations. It is widely used in FastAPI to define request and response schemas.

# Key Features:
# Data parsing and validation using Python types.
# Automatic error messages for invalid data.
# Serialization and deserialization of data.



# define a pydantic model
from pydantic import BaseModel, ValidationError

# model
class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True  # Default value

# Creating an instance
user = User(id=1, name="Alice", email="alice@example.com")
print(user)
print(user.model_dump())  # Convert to dictionary

# Pydantic automatically validates types:
try:
    User(id="abc", name="Test", email="test@example.com")
except ValidationError as e:
    print(e)
# Raises ValidationError because id should be int

# Nested Models
from typing import List

class Address(BaseModel):
    city: str
    zipcode: str

class UserWithAddress(BaseModel):
    name: str
    addresses: List[Address]

user = UserWithAddress(
    name="Charlie",
    addresses=[{"city": "NYC", "zipcode": "10001"}]
)
print(user)

# Pydantic will coerce types if possible:
user = User(id="2", name="Dave", email="dave@example.com")
print(user.id)  # 2 (int)


# Using Pydantic with FastAPI
# FastAPI uses Pydantic models for request bodies, query parameters, and responses.

# Field used to provide extra information about a field, either for the model schema or complex validation. Some arguments apply only to number fields (int, float, Decimal) and some apply only to str

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Item(BaseModel):
    name: str = Field(..., min_length=3)
    price: float = Field(..., gt=0, )

@app.post("/items/")
async def create_item(item: Item):
    return item
