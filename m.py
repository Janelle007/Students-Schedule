from typing import List

class Student:
    def __init__(self, student_id: int, name: str, major: str):
        self._student_id = student_id
        self._name = name
        self._major = major
        self._courses: List['Course'] = []

    def enroll_course(self, course: 'Course') -> bool:
        if course not in self._courses:
            self._courses.append(course)
            return True
        return False

    def view_schedule(self) -> None:
        pass


class Teacher:
    def __init__(self, teacher_id: int, name: str, department: str):
        self._teacher_id = teacher_id
        self._name = name
        self._department = department
        self._assigned_courses: List['Course'] = []

    def assign_course(self, course: 'Course') -> bool:
        if course not in self._assigned_courses:
            self._assigned_courses.append(course)
            return True
        return False

    def view_courses(self) -> None:
        pass


class Course:
    def __init__(self, course_id: int, course_name: str, credits: int):
        self._course_id = course_id
        self._course_name = course_name
        self._credits = credits
        self._teacher: Teacher = None

    def assign_teacher(self, teacher: Teacher) -> bool:
        self._teacher = teacher
        return teacher.assign_course(self)

    def get_course_info(self) -> None:
        pass


class Classroom:
    def __init__(self, room_id: int, capacity: int):
        self._room_id = room_id
        self._capacity = capacity
        self._is_available = True

    def reserve_room(self) -> bool:
        if self._is_available:
            self._is_available = False
            return True
        return False

    def release_room(self) -> bool:
        self._is_available = True
        return True


class Schedule:
    def __init__(self, schedule_id: int, time_slot: str, day: str, course: Course, classroom: Classroom, teacher: Teacher):
        self._schedule_id = schedule_id
        self._time_slot = time_slot
        self._day = day
        self._course = course
        self._classroom = classroom
        self._teacher = teacher

    def create_schedule(self) -> bool:
        return True

    def update_schedule(self) -> bool:
        return True


class ScheduleSystem:
    def __init__(self):
        self._total_rooms = 0
        self._total_students = 0
        self.students: List[Student] = []
        self.classrooms: List[Classroom] = []
        self.schedules: List[Schedule] = []

    def add_student(self, student: Student) -> bool:
        self.students.append(student)
        self._total_students += 1
        return True

    def remove_student(self, student_id: int) -> bool:
        for student in self.students:
            if student._student_id == student_id:
                self.students.remove(student)
                self._total_students -= 1
                return True
        return False

    def generate_schedule(self) -> bool:
        return True

    def display_schedule(self) -> None:
        pass



if __name__ == "__main__":

    system = ScheduleSystem()

    student1 = Student(student_id=101, name="Alice Smith", major="Computer Science")
    student2 = Student(student_id=102, name="Bob Johnson", major="Math")

    course1 = Course(course_id=1, course_name="Algorithms", credits=3)
    course2 = Course(course_id=2, course_name="Databases", credits=4)

    teacher1 = Teacher(10, "Dr. Brown", "CS")

    system.add_student(student1)
    system.add_student(student2)

    course1.assign_teacher(teacher1)

    student1.enroll_course(course1)
    student1.enroll_course(course2)

    student2.enroll_course(course1)

    print(f"Student created: {student1._name}")
    print(f"Course assigned: {course1._course_name}")
    print(f"Teacher: {teacher1._name}")

    student1.view_schedule()