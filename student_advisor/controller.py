import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")


def get_db_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

def add_trial_student(name, birth_date, level='LK'):
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = """
        INSERT INTO students (name, birth_date, level, status)
        VALUES (%s, %s, %s, 'trial')
    """
    cursor.execute(sql, (name, birth_date, level))
    student_id = cursor.lastrowid
    conn.commit()
    cursor.close()
    conn.close()
    return student_id


def list_trial_students():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    sql = "SELECT * FROM students WHERE status='trial' ORDER BY id DESC"
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result


def update_trial_status(student_id, status):
    """
    status: 'active', 'completed', 'cancel'
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "UPDATE students SET status=%s WHERE id=%s"
    cursor.execute(sql, (status, student_id))
    conn.commit()
    cursor.close()
    conn.close()

def list_joined_students():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    sql = "SELECT * FROM students WHERE status='active' ORDER BY id DESC"
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def list_classrooms():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    sql = """
        SELECT c.id, c.name, m.name AS module_name, t.term_label, u.name AS teacher_name
        FROM classes c
        JOIN modules m ON c.module_id = m.id
        JOIN terms t ON c.term_id = t.id
        JOIN users u ON c.teacher_id = u.id
        ORDER BY c.id DESC
    """
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result
