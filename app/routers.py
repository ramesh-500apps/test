from fastapi import APIRouter, Depends
from app.models import Expenses
from sqlmodel import Session, extract, select, func
from app.db import get_db

router = APIRouter()

@router.post("/expenses")
async def create_expense(expense: Expenses, session: Session = Depends(get_db)):
    """
    Add a new expense to the database.

    Args:
        expense (Expenses): Expense data including date, amount, and description.
        session (Session): Database session dependency.

    Returns:
        str: Confirmation message.
    """
    session.add(expense)  # Add the new expense object to the session
    session.commit()  # Commit changes to persist in the database
    return "Expense added successfully."


@router.get("/expenses")
async def get_all_expenses(session: Session = Depends(get_db)):
    """
    Retrieve all expenses from the database.

    Args:
        session (Session): Database session dependency.

    Returns:
        List[Expenses]: A list of all expenses.
    """
    query = session.query(Expenses)  # Create a query for all Expenses
    expenses = session.exec(query).all()  # Execute the query and fetch all results
    return expenses


@router.get("/expenses/month/{year}/{month}")
async def get_expenses_monthly(year: int, month: int, session: Session = Depends(get_db)):
    """
    Retrieve expenses for a specific month and year.

    Args:
        year (int): The year to filter expenses.
        month (int): The month to filter expenses.
        session (Session): Database session dependency.

    Returns:
        List[Expenses]: A list of expenses for the specified month and year.
    """
    query = session.query(Expenses).where(
        extract("year", Expenses.date) == year, 
        extract("month", Expenses.date) == month
    )  # Query to filter expenses by year and month
    expenses = session.exec(query).all()  # Execute the query and fetch results
    return expenses


@router.get("/totals")
def get_total_expenses(salary: float, session: Session = Depends(get_db)):
    """
    Calculate total expenses and remaining balance based on the provided salary.

    Args:
        salary (float): The total salary to compare against expenses.
        session (Session): Database session dependency.

    Returns:
        dict: A dictionary containing total expenses and the remaining balance.
    """
    # Query to calculate the sum of all expense amounts
    total_expenses = session.exec(select(func.sum(Expenses.amount))).one()
    remaining_amount = salary - total_expenses  # Calculate the remaining balance

    return {"total_expenses": total_expenses, "remaining_amount": remaining_amount}
