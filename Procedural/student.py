# student.py
def create_student(name, student_id, grade):
    return {
        'name': name,
        'id': student_id,
        'grade': grade
    }

def get_name(student):
    return student['name']

def get_id(student):
    return student['id']

def get_grade(student):
    return student['grade']
