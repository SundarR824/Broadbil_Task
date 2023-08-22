from app.db.database import DatabaseManager


def groups(group_name):
    try:
        db_manager = DatabaseManager()
        db_manager.connect()
        query = f"INSERT INTO groups (group_name) VALUES ('{group_name}')"
        db_manager.execute_insert_query(query)
        db_manager.close_connection()
        return "Record added in groups table"
    except Exception as err:
        print(err)
        return None


def marks(student_id, subject_id, date_time, mark):
    try:
        db_manager = DatabaseManager()
        db_manager.connect()
        query = f"INSERT INTO marks (student_id, subject_id, date_time, mark) VALUES ({student_id}, {subject_id}, '{date_time}', {mark})"
        db_manager.execute_insert_query(query)
        db_manager.close_connection()
        return "Record added in marks table"
    except Exception as err:
        print(err)
        return None


def students(first_name, last_name, group_id):
    try:
        db_manager = DatabaseManager()
        db_manager.connect()
        query = f"INSERT INTO students (first_name, last_name, group_id) VALUES ('{first_name}', '{last_name}', {group_id})"
        db_manager.execute_insert_query(query)
        db_manager.close_connection()
        return "Record added in students table"
    except Exception as err:
        print(err)
        return None


def subjects(title):
    try:
        db_manager = DatabaseManager()
        db_manager.connect()
        query = f"INSERT INTO subjects (title) VALUES ('{title}')"
        db_manager.execute_insert_query(query)
        db_manager.close_connection()
        return "Record added in subjects table"
    except Exception as err:
        print(err)
        return None


def teacher(subject_id, group_id):
    try:
        db_manager = DatabaseManager()
        db_manager.connect()

        query = f"INSERT INTO teacher (group_name) VALUES ({subject_id}, {group_id})"
        db_manager.execute_insert_query(query)
        db_manager.close_connection()
        return "Record added in groups table"
    except Exception as err:
        print(err)
        return None


def get_mark(student_id: int):
    db_manager = DatabaseManager()
    db_manager.connect()

    query = f"SELECT m.mark, s.first_name, s.last_name, sub.title AS subject FROM marks m JOIN students s " \
            f"ON m.student_id = s.student_id JOIN subjects sub ON m.subject_id = sub.subject_id WHERE m.student_id = " \
            f"{student_id};"
    res = db_manager.execute_select_query(query)
    heading = ('Mark', 'first_name', 'last_name', 'Subject')
    rest = [dict(zip(heading, i)) for i in res]

    db_manager.close_connection()

    return rest


def get_students(teacher_id: int):
    db_manager = DatabaseManager()
    db_manager.connect()

    query = (f"select count(DISTINCT st.student_id), t.teacher_id, sub.title from students st JOIN teacher t on "
             f"st.group_id = t.group_id JOIN subjects sub on t.subject_id = sub.subject_id where t.tea"
             f"cher_id= {teacher_id} group by t.group_id")

    res = db_manager.execute_select_query(query)
    heading = ('number_of_students', 'teacher', 'subject')
    rest = [dict(zip(heading, i)) for i in res]

    db_manager.close_connection()

    return rest


def get_students_by_group(group_id: int):
    db_manager = DatabaseManager()
    db_manager.connect()

    query = f"select s.student_id, s.first_name, s.last_name, s.group_id from students s where s.group_id = {group_id}"
    res = db_manager.execute_select_query(query)
    heading = ('student_id', 'first_name', 'last_name', 'group_id')
    rest = [dict(zip(heading, i)) for i in res]
    db_manager.close_connection()

    return rest


def get_mark_list(student_id: int):
    db_manager = DatabaseManager()
    db_manager.connect()

    query = f"SELECT sub.title AS subject, m.mark FROM marks m JOIN subjects sub ON m.subject_id = sub.subject_id " \
            f"WHERE m.student_id = {student_id};"

    res = db_manager.execute_select_query(query)
    heading = ('subject', 'mark', 'student_id')
    rest = [dict(zip(heading, i)) for i in res]

    db_manager.close_connection()

    return rest


def get_all():
    db_manager = DatabaseManager()
    db_manager.connect()

    query = f"SELECT s.*, g.group_name AS group_name FROM students s JOIN groups g ON s.group_id = g.group_id;"
    res = db_manager.execute_select_query(query)

    heading = ('student_id', 'first_name', 'last_name', 'group_id', 'group_name')
    rest = [dict(zip(heading, i)) for i in res]
    db_manager.close_connection()
    return rest


def update_student(first_name, last_name, group_id, student_id):
    try:
        db_manager = DatabaseManager()
        db_manager.connect()
        query = f"UPDATE students SET first_name = '{first_name}', last_name = '{last_name}', group_id = {group_id}" \
                f" WHERE student_id = {student_id};"
        db_manager.execute_insert_query(query)
        db_manager.close_connection()
        return "Student record updated"
    except Exception as err:
        print(err)
        return None


def delete_group(group_id):
    return_msg = f"Record Deleted from groups table"
    try:
        db_manager = DatabaseManager()
        db_manager.connect()
        query = f"DELETE FROM groups where group_id = {group_id}"
        db_manager.execute_insert_query(query)
        db_manager.close_connection()
    except Exception as err:
        return_msg = err
    return return_msg


def delete_subject(subject_id):
    try:
        db_manager = DatabaseManager()
        db_manager.connect()
        query = f"DELETE FROM subjects where subject_id = {subject_id}"
        db_manager.execute_insert_query(query)
        db_manager.close_connection()
        return "Record Deleted from groups table"
    except Exception as err:
        print(err)
        return None


def delete_student(student_id):
    try:
        db_manager = DatabaseManager()
        db_manager.connect()
        query = f"DELETE FROM students where student_id = {student_id}"
        db_manager.execute_insert_query(query)
        db_manager.close_connection()
        return "Record Deleted from student table"
    except Exception as err:
        print(err)
        return None
