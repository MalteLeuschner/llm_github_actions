import sqlite3

class DatabaseHandler:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            description TEXT,
            amount REAL
        )
        ''')

    def insert_transaction(self, date, description, amount):
        self.cursor.execute('''
        INSERT INTO transactions (date, description, amount)
        VALUES (?, ?, ?)
        ''', (date, description, amount))
        self.conn.commit()

    def query_transactions(self):
        self.cursor.execute('SELECT * FROM transactions')
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()

def main():
    db = DatabaseHandler('financial_data.db')
    db.insert_transaction('2024-07-05', 'Deposit', 1000.0)
    transactions = db.query_transactions()
    for transaction in transactions:
        print(transaction)
    db.close()

if __name__ == '__main__':
    main()

