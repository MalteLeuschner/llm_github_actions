from typing import Tuple, List
import sqlite3


class DatabaseHandler:
    """
    Database handler class.

    This class handles the interaction with the SQLite database. It creates a table for
    transactions, inserts transactions, queries transactions, and closes the database
    connection.

    Args:
        db_name (str): The name of the database file.

    Returns:
        None
    """

    def __init__(self, db_name: str) -> None:
        """Initializes a DatabaseHandler object.

        Creates a connection to a SQLite database and initializes a cursor object.

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
            sqlite3.Error: If a database error occurs during table creation."""
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
        """Inserts a transaction into the database.

        This method executes a SQL query to insert a transaction into the database.

        Args:
            date (str): The date of the transaction.
            description (str): A description of the transaction.
            amount (float): The amount of the transaction.

        Returns:
            None

        Raises:
            sqlite3.Error: If a database error occurs during query execution."""
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
            sqlite3.Error: If a database error occurs during query execution."""
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
    """Main function.

    Runs the entire program, creating a database handler, inserting a transaction,
    querying all transactions, and printing them.

    Args:
        None
    Returns:
        None
    Raises:
        None"""
    db = DatabaseHandler("financial_data.db")
    db.insert_transaction("2024-07-05", "Deposit", 1000.0)
    transactions = db.query_transactions()
    for transaction in transactions:
        print(transaction)
    db.close()


if __name__ == "__main__":
    main()
