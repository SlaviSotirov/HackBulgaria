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

    # def select_query(self, fields):
    #     query = "SELECT IN (?)"

    def select_employees(self):
        query = 'SELECT id, name, position FROM employees'
        result = self.cursor.execute(query).fetchall()
        return result

    def select_monthly_spending(self):
        query = 'SELECT SUM(monthly_salary) FROM employees'
        result = self.cursor.execute(query).fetchall()
        return result

    def select_yearly_spending(self):
        query = 'SELECT SUM(yearly_bonus) FROM employees'
        bonuses = (self.cursor.execute(query).fetchall(), )
        query = 'SELECT SUM(monthly_salary) FROM employees'
        salaries = (self.cursor.execute(query).fetchall(), )
        result = bonuses[0][0] + salaries[0][0]
        return int(result[0]) + int(result[1])

    def delete_query(self, id):
        query = 'DELETE FROM employees WHERE id=?'
        self.cursor.execute(query, (id,))
        self.conn.commit()

    def update_query(self, values):
        query = 'UPDATE employees SET name=?, monthly_salary=?, yearly_bonus=?, position=? WHERE id=?'
        self.cursor.execute(query, values)
        self.conn.commit()

