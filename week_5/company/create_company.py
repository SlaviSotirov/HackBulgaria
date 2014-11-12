from query_handler import QueryHandler


class CompanyHandler:
    NAME = "name"
    MONTHLY_SALARY = "monthly_salary"
    YEARLY_BONUS = "yearly_bonus"
    POSITION = "position"

    def __init__(self, db_name):
        self.query_handler = QueryHandler(db_name)
        self.query_handler.start_up()

    def add_employee(self, name, salary, bonus, position):
        values = (name, salary, bonus, position)
        self.query_handler.insert_query(values)

    def list_employees(self):
        employees = self.query_handler.select_employees()
        for employee in employees:
            print("{} - {} - {}".format(employee[0], employee[1], employee[2]))

    def monthly_spending(self):
        total = self.query_handler.select_monthly_spending()
        print("The company is spending {} every month".format(total[0][0]))

    def yearly_spending(self):
        total = self.query_handler.select_yearly_spending()
        print("The company is spending {} every year".format(total))

    def delete_employee(self, id):
        self.query_handler.delete_query(id)

    def update_employee(self, id, name, salary, bonus, position):
        values = (name, salary, bonus, position, id)
        self.query_handler.update_query(values)


def main():
    company = CompanyHandler("employees.db")
    # company.add_employee("DaBe", 5000, 100, "Pro")
    # company.add_employee("Nebe", 10, 20, "Noob")
    company.list_employees()
    #company.delete_employee(2)
    #company.add_employee("Nebe", 10, 20, "Noob")
    company.update_employee(5, "Kondio", 200, 300, "Mega Noob")
    company.list_employees()

    # company.monthly_spending()
    # company.yearly_spending()
    # company.query_handler.close_db()

if __name__ == '__main__':
    main()
