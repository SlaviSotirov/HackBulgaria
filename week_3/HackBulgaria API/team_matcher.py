import requests
import random


class Matcher:

    def __init__(self):
        self.api_link = "https://hackbulgaria.com/api/students/"
        self.students = None
        self.request = None
        self.courses = []

    def get_request(self):
        self.request = requests.get(self.api_link, verify=False)

    def is_ok(self):
        return self.request.status_code == 200

    def get_students(self):
        if self.is_ok():
            self.students = self.request.json()

    def list_courses(self):
        for student in self.students:
            for course in student["courses"]:
                if course["name"] not in self.courses:
                    self.courses.append(course["name"])

    def print_list_courses(self):
        for course in self.courses:
            print("{} - {}".format(self.courses.index(course), course))

    def match_teams(self, course_id, team_size, group_time):
        temp_team = []
        for student in self.students:
            for course in student["courses"]:
                if course["group"] == group_time and course["name"] == self.courses[course_id] and student["available"]:
                    temp_team.append(student["name"])
        random.shuffle(temp_team)
        i = 0
        for student in temp_team:
            if i >= team_size:
                print("------------------------")
                i = 0
            i += 1
            print(student)

    def get_input(self):
        command = input("Enter command>")
        return(command)

    def handle_input(self):
        to_exit = False
        while not to_exit:
            option = self.get_input()
            opt = option.split(" ")
            if opt[0] == "asd":
                self.match_teams(int(opt[1]), int(opt[2]), int(opt[3]))
            elif opt[0] == "print":
                self.print_list_courses()
            elif opt[0] == "exit":
                to_exit = True


def main():
    match = Matcher()
    match.get_request()
    match.get_students()
    match.list_courses()
    match.handle_input()
if __name__ == '__main__':
    main()
