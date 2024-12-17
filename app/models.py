from sqlmodel import SQLModel, Field, Relationship
from datetime import date
from typing import List
from app.db import engine


class Expenses(SQLModel, table=True):
    """
    Represents the Expenses table in the database.

    Attributes:
        id (int): Primary key for the table.
        amount (float): The amount spent.
        category (str): Category of the expense (e.g., food, travel).
        date (date): The date of the expense.
    """
    # Primary key column for Expenses
    id: int = Field(primary_key=True)
    
    # Column for the expense amount
    amount: float
    
    # Column for the category with a maximum length of 200 characters
    category: str = Field(max_length=200)
    
    # Column to store the date of the expense
    date: date


# Function to create database tables
def create_db_tables():
    """
    Creates all the tables in the database based on SQLModel metadata.

    Uses the engine provided to connect and create the required tables.
    """
    SQLModel.metadata.create_all(engine)
