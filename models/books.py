from sqlmodel import SQLModel, Field, Relationship
from typing import Optional

class Book(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    author: str = Field(index=True)
    price: int
    isSold: bool = Field(default=False)
    # foreign key to the user role
    user_id: int = Field(foreign_key="user.id")
    owner: Optional["User"] = Relationship(back_populates="books")


# request body for creating a new book
class BookCreate(SQLModel):
    title: str
    author: str
    price: int
    user_id: int

# response body for returning book data
class BookRead(SQLModel):
    id: int
    title: str
    author: str
    price: int
    isSold: bool
    user_id: int

from models.users import User
Book.model_rebuild()
