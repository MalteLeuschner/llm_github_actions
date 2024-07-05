from typing import Tuple, List
import sqlite3



class DatabaseHandler:

    def __init__(self, db_name: str) -> None:

        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self) -> None:

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
