from typing import List, Tuple
import sqlite3


class DatabaseHandler:
    """:
    DatabaseHandler is a class that handles database operations.
    It creates a connection to a SQLite database, creates a table for transactions,
    and provides methods to insert transactions and query existing ones.

    Args:
        db_name (str): The name of the database file.

    Returns:
        None"""

    def __init__(self, db_name: str) -> None:
        """Initializes a DatabaseHandler instance.

        Creates a connection to a SQLite database and creates a table for transactions if it doesn't exist.

        Args:
            db_name (str): The name of the database file.

        Returns:
            None"""
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self) -> None:
        """Creates a table in the database if it does not exist.

        This method creates a table named 'transactions' with columns 'id', 'date', 'description', and 'amount'
        if the table does not already exist in the database.

        Args:
            None

        Returns:
            None

        Raises:
            sqlite3.Error: If there is an error while creating the table."""
        self.cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            description TEXT,
            amount REAL
        )
        """
        )

    def insert_transaction(self, date: str, description: str, amount: float) -> None:
        """Inserts a new transaction into the database.

        Inserts a new transaction into the transactions table with the given date, description, and amount.

        Args:
            date (str): The date of the transaction.
            description (str): A brief description of the transaction.
            amount (float): The amount of the transaction.

        Returns:
            None

        Raises:
            sqlite3.Error: If there is an error executing the SQL query."""
        self.cursor.execute(
            """
        INSERT INTO transactions (date, description, amount)
        VALUES (?, ?, ?)
        """,
            (date, description, amount),
        )
        self.conn.commit()

    def query_transactions(self) -> List[Tuple]:
        """Retrieves all transactions from the database.

        This method executes a SQL query to select all transactions from the database
        and returns the result.

        Args:
            None

        Returns:
            List[Tuple]

        Raises:
            sqlite3.Error: If a database error occurs during the query."""
        self.cursor.execute("SELECT * FROM transactions")
        return self.cursor.fetchall()

    def close(self) -> None:
        """Closes the database connection.

        Args:
          self (DatabaseHandler): The database handler object.

        Returns:
          None"""
        self.conn.close()


def main() -> None:
    """Main function of the script.

    Runs the entire script, creating a database, inserting a transaction,
    querying all transactions and printing them, then closing the database.

    Args:
        None
    Returns:
        None
    Raises:
        sqlite3.Error: If there is an error while connecting to the database or
        executing a query."""
    db = DatabaseHandler("financial_data.db")
    db.insert_transaction("2024-07-05", "Deposit", 1000.0)
    transactions = db.query_transactions()
    for transaction in transactions:
        print(transaction)
    db.close()


if __name__ == "__main__":
    main()
