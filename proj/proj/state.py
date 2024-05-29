import reflex as rx
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from proj.db.database import Student
from typing import List, TypedDict


engine = create_engine('sqlite:///app.db')
Session = sessionmaker(bind=engine)


class StudentDict(TypedDict):
    id: int
    first_name: str
    last_name: str
    class_name: str
class UczniowieState(rx.State):
    show_form: bool = False
    first_name: str = ''
    last_name: str = ''
    class_name: str = ''
    students: List[StudentDict] = []


    def toggle_form(self):
        self.show_form = not self.show_form

    def handle_first_name_change(self, value: str):
        self.first_name = value

    def handle_last_name_change(self, value: str):
        self.last_name = value

    def handle_class_name_change(self, value: str):
        self.class_name = value

    def submit_form(self):
        # Save the new student to the database
        session = Session()
        new_student = Student(
            first_name=self.first_name,
            last_name=self.last_name,
            class_name=self.class_name
        )
        session.add(new_student)
        session.commit()
        session.close()
        # Clear the form
        self.first_name = ''
        self.last_name = ''
        self.class_name = ''
        # Hide the form
        self.show_form = False
        self.get_students()

    def get_students(self):
        session = Session()
        students = session.query(Student).all()
        self.students = [
            {"id": student.id, "first_name": student.first_name, "last_name": student.last_name,
             "class_name": student.class_name}
            for student in students
        ]
        session.close()
        print("Students fetched from database")

    def on_load(self):
        session = Session()
        session.commit()
        self.get_students()