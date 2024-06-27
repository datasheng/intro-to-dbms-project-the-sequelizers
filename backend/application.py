import mysql.connector
from flask import Flask, request, Response
import os
from dotenv import load_dotenv

load_dotenv()
application = Flask(__name__)

mydb = mysql.connector.connect(
  host=os.getenv("DB_HOST"),
  user=os.getenv("DB_USER"),
  password=os.getenv("DB_PASSWORD"),
  port=os.getenv("DB_PORT"),
)

mycursor = mydb.cursor(dictionary=True)
mycursor.execute("USE " + os.getenv("DB_NAME") + ";")

def SELECT_FROM_WHERE(s, f, w="1=1"):
    try:
        mycursor.execute("SELECT " + s + " FROM " + f + " WHERE " + w + ";")
        arr = []
        for row in mycursor:
            arr += [row]
        return arr
    except:
        return {"error": "There was an error"}

@application.route('/get_courses', methods=['GET'])
def get_courses():
    query = request.args.get('q')
    id = request.args.get('id')
    if id:
        return SELECT_FROM_WHERE("*", "course", "course_id = " + id)
    elif query:
        return SELECT_FROM_WHERE("*", "course", "CONCAT(course_subject, course_level, name) LIKE '%" + query.replace(" ", "%") + "%'")
    return SELECT_FROM_WHERE("*", "course")

@application.route('/get_professors', methods=['GET'])
def get_professors():
    query = request.args.get('q')
    id = request.args.get('id')
    if id:
        return SELECT_FROM_WHERE("*", "professor", "id = " + id)
    elif query:
        return SELECT_FROM_WHERE("*", "professor", "name LIKE '%" + query.replace(" ", "%") + "%'")
    return SELECT_FROM_WHERE("*", "professor")

@application.route('/get_sections', methods=['GET'])
def get_sections():
    section_id = request.args.get('section')
    course_id = request.args.get('course')
    professor_id = request.args.get('professor')
    where = "1=1"
    if section_id:
        where = "section_id = " + section_id
    elif course_id:
        where =  "section.course_id = " + course_id
    elif professor_id:
        where = "professor_id = " + professor_id
    sections =  SELECT_FROM_WHERE("DISTINCT(section.section_id), course.name AS course_name, section.course_id, course.credits, CONCAT(course_subject, ' ', course.course_level) AS course_code, section.end_date, section.instruction_mode, section.start_date", "course INNER JOIN section ON course.course_id = section.course_id", where)

    for i in range(len(sections)):
        sections[i]["days"] = SELECT_FROM_WHERE("day, start_time, end_time", "section", "section_id = " + str(sections[i]["section_id"]))
        sections[i]["rooms"] = list(map(lambda x: x["room"], SELECT_FROM_WHERE("DISTINCT(room)", "section", "section_id = " + str(sections[i]["section_id"]))))
        sections[i]["professors"] = SELECT_FROM_WHERE("DISTINCT(professor.name), professor.id", "professor INNER JOIN section ON section.professor_id = professor.id", "section_id = " + str(sections[i]["section_id"]))
    return sections

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8000)))

