import csv
from io import StringIO
import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()

db = mysql.connector.connect(
  host=os.getenv("DB_HOST"),
  user=os.getenv("DB_USER"),
  password=os.getenv("DB_PASSWORD"),
  port=os.getenv("DB_PORT"),
  autocommit=True
)

cursor = db.cursor(dictionary=True)
cursor.execute("USE " + os.getenv("DB_NAME") + ";")

def SELECT_FROM_WHERE(s, f, w="1=1"):
    try:
        cursor.execute("SELECT " + s + " FROM " + f + " WHERE " + w + ";")
        arr = []
        for row in cursor:
            arr += [row]
        return arr
    except Exception as error:
        return {"error": str(error)}

def INSERT_INTO(t, d):
    try:
        cursor.execute("INSERT INTO " + t + "(" + ", ".join(list(d.keys())) + ") VALUES ('" + "', '".join(list(map(lambda value: str(value), d.values()))) + "');")
        return {"message": "Insert Successful", "inserted": d}
    except Exception as error:
        return {"error": str(error)}

def DELETE_FROM_WHERE(t, w):
    try:
        cursor.execute("DELETE FROM " + t + " WHERE " + w + ";")
        return {"message": "Deletion Successful"}
    except Exception as error:
        return {"error": str(error)}

def UPDATE_SET_WHERE(t, s, w):
    try:
        set = list(map(lambda key: str(key + " = '" + str(s[key]) + "'"), s.keys()))
        cursor.execute("UPDATE " + t + " SET " + ", ".join(set) + " WHERE " + w + ";")
        return SELECT_FROM_WHERE("*", t, w)
    except Exception as error:
        return {"error": str(error)}


def retrieve_roster(professor_id, section_id):
    try:
        cursor.callproc('RetrieveRoster', [professor_id, section_id])
        studentInfo = []
        for result in cursor.stored_results():
            studentInfo.extend(result.fetchall())
        return studentInfo
    except Exception as error:
        print(str(error))
        return {"error": str(error)}
    

def generate_csv(data):
    string_buffer = StringIO()
    csv_writer = csv.writer(string_buffer)
    csv_writer.writerow(['Student ID', 'First Name', 'Last Name', 'Email', 'Major'])
    csv_writer.writerows(data)
    string_buffer.seek(0)
    return string_buffer.getvalue()
    
def enroll_student(student_id, section_id, status):
    try:
        args = [student_id, section_id, status]
        result_args = cursor.callproc('EnrollStudent', args)
        return {"message": result_args['@_EnrollStudent_arg3']}
    except Exception as error:
        return {"error": str(error)}
