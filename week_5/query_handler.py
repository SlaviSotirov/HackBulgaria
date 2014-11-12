import sqlite3


class QueryHandler:

    def __init__(self, database):
        self.database = database
        self.conn = None
        self.cursor = None

    def start_up(self):
        self.conn = sqlite3.connect(self.database)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS
                            employees(id INTEGER PRIMARY KEY, name TEXT,
                            monthly_salary REAL, yearly_bonus REAL, position TEXT)''')

    def close_db(self):
        self.conn.close()

    def insert_query(self, values):
        query = 'INSERT INTO employees (name, monthly_salary, yearly_bonus, position) VALUES (?, ?, ?, ?);'
        self.cursor.execute(query, values)
        self.conn.commit()

    def select_employees(self):
        query = 'SELECT name, position FROM employees'
        result = self.cursor.execute(query).fetchall()
        return result

    def select_monthly_spending(self):
        query = 'SELECT SUM(monthly_salary) FROM employees'
        result = self.cursor.execute(query).fetchall()
        return result

    def select_yearly_spending(self):
        query = 'SELECT SUM(yearly_bonus) FROM employees'
        result = (self.cursor.execute(query).fetchall(), )
        query = 'SELECT SUM(yearly_bonus) FROM employees'
        result = result + (self.cursor.execute(query).fetchall(), )
        print(result)
        return result
