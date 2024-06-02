import reflex as rx
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from proj.db.database import Student, Job
from typing import List, TypedDict

engine = create_engine('sqlite:///app.db')
Session = sessionmaker(bind=engine)

class StudentDict(TypedDict):
    id: int
    first_name: str
    last_name: str
    class_name: str

class JobDict(TypedDict):
    id: int
    title: str
    description: str
    qualifications: str
    location: str
    salary: str

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
        session = Session()
        new_student = Student(
            first_name=self.first_name,
            last_name=self.last_name,
            class_name=self.class_name
        )
        session.add(new_student)
        session.commit()
        session.close()
        self.first_name = ''
        self.last_name = ''
        self.class_name = ''
        self.show_form = False
        self.get_students()

    def get_students(self):
        session = Session()
        students = session.query(Student).all()
        self.students = [
            {"id": student.id, "first_name": student.first_name, "last_name": student.last_name, "class_name": student.class_name}
            for student in students
        ]
        session.close()
        print("Students fetched from database")

    def on_load(self):
        session = Session()
        session.commit()
        self.get_students()

class RekrutacjeState(rx.State):
    show_form: bool = False
    title: str = ''
    description: str = ''
    qualifications: str = ''
    location: str = ''
    salary: str = ''
    jobs: List[JobDict] = []
    errors: dict = {}

    def toggle_form(self):
        self.show_form = not self.show_form

    def handle_change(self, field: str, value: str):
        setattr(self, field, value)

    def validate_form(self):
        self.errors = {}
        if not self.title:
            self.errors['title'] = 'Tytuł jest wymagany.'
        if not self.description:
            self.errors['description'] = 'Opis obowiązków jest wymagany.'
        if not self.qualifications:
            self.errors['qualifications'] = 'Wymagania kwalifikacyjne są wymagane.'
        if not self.location:
            self.errors['location'] = 'Lokalizacja jest wymagana.'
        if not self.salary:
            self.errors['salary'] = 'Wynagrodzenie jest wymagane.'
        return len(self.errors) == 0

    def submit_form(self):
        if self.validate_form():
            session = Session()
            new_job = Job(
                title=self.title,
                description=self.description,
                qualifications=self.qualifications,
                location=self.location,
                salary=self.salary,
            )
            session.add(new_job)
            session.commit()
            session.close()
            self.title = ''
            self.description = ''
            self.qualifications = ''
            self.location = ''
            self.salary = ''
            self.show_form = False
            self.get_jobs()

    def get_jobs(self):
        session = Session()
        jobs = session.query(Job).all()
        self.jobs = [
            {
                "id": job.id,
                "title": job.title,
                "description": job.description,
                "qualifications": job.qualifications,
                "location": job.location,
                "salary": job.salary
            }
            for job in jobs
        ]
        session.close()
        print("Jobs fetched from database")

    def on_load(self):
        session = Session()
        session.commit()
        self.get_jobs()

