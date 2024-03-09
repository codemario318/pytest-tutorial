import pytest
from source.school import Classroom, Teacher, Student, TooManyStudents


@pytest.fixture
def teacher():
    return Teacher("Severus Snape")


@pytest.fixture
def students():
    return [Student("Harry Potter"), Student("Hermione Granger"), Student("Ron Weasley")]


@pytest.fixture
def classroom(teacher, students):
    course_title = "Potions"
    return Classroom(teacher, students, course_title)


def test_add_student(classroom):
    classroom.add_student(Student("Draco Malfoy"))
    assert len(classroom.students) == 4


def test_add_too_many_students(classroom):
    with pytest.raises(TooManyStudents):
        for _ in range(10):
            classroom.add_student(Student("Random Student"))


def test_remove_student(classroom):
    classroom.remove_student("Harry Potter")
    assert len(classroom.students) == 2
    assert all(student.name != "Harry Potter" for student in classroom.students)


def test_change_teacher(classroom):
    new_teacher = Teacher("Remus Lupin")
    classroom.change_teacher(new_teacher)
    assert classroom.teacher.name == "Remus Lupin"

