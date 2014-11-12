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
            print("{} - {}".format(employee[0], employee[1]))

    def monthly_spending(self):
        total = self.query_handler.select_monthly_spending()
        print("The company is spending {} every year".format(total[0][0]))

    def yearly_spending(self):
        total = self.query_handler.select_monthly_spending()
        print(total)
        salaries = int(total[1][1]) * 12
        bonuses = int(total[0][0])
        print("The company is spending {} every month".format(salaries + bonuses))


def main():
    company = CompanyHandler("employees.db")
    #company.add_employee("Slavi", 100, 100, "Pro")
    #company.list_employees()
    company.monthly_spending()
    company.yearly_spending()

if __name__ == '__main__':
    main()
