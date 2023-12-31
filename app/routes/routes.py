from flask import Blueprint, request, jsonify, make_response
from app.db.database import DatabaseManager
from app.configs import DDLandDMLConfigs
from app.db.db_queries import *
from flasgger import Swagger
from app import app
import pathlib
from flask_jwt_extended import (
    jwt_required, create_access_token, get_jwt_identity
)


current_file_path = pathlib.Path(__file__).parent.parent
bp = Blueprint('routes', __name__)

valid_username = 'john'
valid_password = 'password123'

ddl_file_path = DDLandDMLConfigs.DDL_FILE_PATH
dml_file_path = DDLandDMLConfigs.DML_FILE_PATH

table_keys = {
    "groups": groups,
    "marks": marks,
    "students": students,
    "subjects": subjects,
    "teacher": teacher
}
delete_tbl_keys = {"delete_group": delete_group, "delete_subject": delete_subject, "delete_student": delete_student}
swagger = Swagger(app)


@bp.route('/login', methods=['POST'])
def login():
    """
    User Login
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            username:
              type: string
            password:
              type: string
    responses:
      200:
        description: Access token generated successfully
        examples:
            application/json:
                {"access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"}
      401:
        description: Invalid credentials
    """
    username = request.json.get('username')
    password = request.json.get('password')

    if username != valid_username or password != valid_password:
        return jsonify({'message': 'Invalid credentials'}), 401

    access_token = create_access_token(identity=username)
    return make_response(jsonify({'access_token': access_token}), 200)


@bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    """
        Protected Route
        ---
        security:
          - JWT: []
        responses:
          200:
            description: Protected route accessed successfully
            examples:
                application/json:
                    {"message": "Protected route. User: NAME_OF_USER"}
          401:
            description: Missing or invalid JWT token
        """
    current_user = get_jwt_identity()
    return jsonify({'message': f'Protected route. User: {current_user}'}), 200


@bp.route('/', methods=['GET'])
@jwt_required()
def home_page():
    """
        Home Page
        ---
        security:
          - JWT: []
        responses:
          200:
            description: Tables Create Successfully
          401:
            description: Missing or invalid JWT token
    """
    try:
        db_manger = DatabaseManager()
        db_manger.connect()
        db_manger.execute_ddl(ddl_file_path)
        db_manger.execute_dml(dml_file_path)
        resp = {"message": "Table has been created successfully!!.."}
        db_manger.close_connection()
    except Exception as err:
        resp = {"message": "An error occurred", "error": str(err)}
    return make_response(jsonify(resp))


@bp.route('/find_by_id/mark/<int:id_num>', methods=['GET'])
@jwt_required()
def find_mark(id_num):
    """
        Find Mark for Student
        ---
        security:
          - JWT: []

        responses:
          200:
            description: Success
            examples:
                application/json:
                    {"message": {"number_of_students": 3}}
          401:
            description: Missing or invalid JWT token
        """
    try:
        db_rec = get_mark(id_num)
        resp = {"message": db_rec}
    except Exception as err:
        resp = {"message": "An Error occurred", "error": str(err)}

    return make_response(jsonify(resp))


@bp.route('/find_by_id/mark_list/<int:student_id>', methods=['GET'])
@jwt_required()
def find_mark_list(student_id):
    """
        Find Mark List for particular ID
        ---
        security:
          - JWT: []

        responses:
          200:
            description: Success
            examples:
                application/json:
                    {"message": {"mark": 90,"subject": "Science"}}
          401:
            description: Missing or invalid JWT token
        """
    try:
        db_rec = get_mark_list(student_id)
        resp = {"message": db_rec}
    except Exception as err:
        resp = {"message": "An Error occurred", "error": str(err)}

    return make_response(jsonify(resp))


@bp.route('/find_by_id/students/<int:teacher_id>', methods=['GET'])
@jwt_required()
def find_student(teacher_id):
    """
        Find Students by id
        ---
        security:
          - JWT: []

        responses:
          200:
            description: Success
            examples:
                application/json:
                    {"message": {"number_of_students": 3}}
          401:
            description: Missing or invalid JWT token
    """
    try:
        db_rec = get_students(teacher_id)
        resp = {"message": db_rec[0]}
    except Exception as err:
        resp = {"message": "An Error occurred", "error": str(err)}

    return make_response(jsonify(resp))


@bp.route('/find_by_group/<int:group_id>', methods=['GET'])
@jwt_required()
def find_students_by_group(group_id):
    """
        Find Students by id
        ---
        security:
          - JWT: []

        responses:
          200:
            description: Success
            examples:
                application/json:
                    {"message": {"number_of_students": 3}}
          401:
            description: Missing or invalid JWT token
    """
    try:
        db_rec = get_students_by_group(group_id)
        resp = {"message": db_rec}
    except Exception as err:
        resp = {"message": "An Error occurred", "error": str(err)}

    return make_response(jsonify(resp))


@bp.route('/find_all', methods=['GET'])
@jwt_required()
def find_all():
    """
    Find All Students
    ---
    security:
        -JWT: []

    responses:
      200:
        description: Success
        examples:
            application/json:
                {"message": [
                    {"first_name": "John","group_name": 1,"last_name": "Doe","student_id": 1,"subject_title": "Group A" },
                    {"first_name": "Alice", "group_name": 1,"last_name": "Johnson","student_id": 3,"subject_title": "Group A" }]}
      401:
        description: Invalid credentials
    """

    try:
        db_rec = get_all()
        resp = {"message": db_rec}
    except Exception as err:
        resp = {"message": "An Error occurred", "error": str(err)}

    return make_response(jsonify(resp))


@bp.route('/add_details', methods=['POST'])
@jwt_required()
def add_details():
    """
    Add Details to tables
    ---
    security:
        - JWT: []

    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            first_name:
              type: string
            last_name:
              type: string
            group_id:
              type: integer
            key:
              type: string
    responses:
      200:
        description: Success
        examples:
            application/json:
                {"message": "Record added in students table"}
      401:
        description: Missing or invalid JWT token
    """
    try:
        req_json = request.json

        first_name = req_json['first_name']
        last_name = req_json['last_name']
        group_id = req_json['group_id']
        key = req_json['key']

        db_rec = table_keys[key](first_name, last_name, group_id)
        resp = {"message": db_rec}
    except Exception as err:
        resp = {"message": "An Error occurred", "error": str(err)}

    return make_response(jsonify(resp))


@bp.route('/update_details/<int:id_num>', methods=['PUT'])
@jwt_required()
def update_details(id_num):
    """
    Update Details in table
    ---
    security:
        - JWT: []
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            first_name:
              type: string
            last_name:
              type: string
            group_id:
              type: integer
    responses:
      200:
        description: Success
        examples:
            application/json:
                {"message": "Record Updated successfully"}
      401:
        description: Missing or invalid JWT token
    """
    try:
        req_json = request.json

        first_name = req_json['first_name']
        last_name = req_json['last_name']
        group_id = req_json['group_id']

        db_rec = update_student(first_name, last_name, group_id, id_num)
        resp = {"message": db_rec}
    except Exception as err:
        resp = {"message": "An Error occurred", "error": str(err)}

    return make_response(jsonify(resp))


@bp.route('/delete_details/<int:id_num>', methods=['Delete'])
@jwt_required()
def delete_details(id_num):
    """
    Delete Details from Table
    ---
    security:
        - JWT: []

    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            key:
              type: string
    responses:
      200:
        description: success
        examples:
            application/json:
                {"message": "Record Deleted successfully"}
      401:
        description: Missing or invalid JWT token
    """
    try:
        req_json = request.json

        key = req_json['key']
        db_rec = delete_tbl_keys[key](id_num)
        resp = {"message": db_rec}
    except Exception as err:
        resp = {"message": "An Error occurred", "error": str(err)}

    return make_response(jsonify(resp))

