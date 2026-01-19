from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from student_advisor.controller import (
    add_trial_student, list_trial_students, update_trial_status,
    list_joined_students, list_classrooms
)

student_advisor_bp = Blueprint('student_advisor',__name__,url_prefix='/student_advisor', template_folder='templates')

@student_advisor_bp.route("/dashboard", methods=["GET","POST"])
def dashboard():
    return render_template("student_advisor/dashboard.html")

@student_advisor_bp.route('/trial/add', methods=['GET', 'POST'])
def trial_add():
    if request.method == 'POST':
        name = request.form['name']
        birth_date = request.form['birth_date']
        level = request.form.get('level', 'LK')
        add_trial_student(name, birth_date, level)
        return render_template('student_advisor/trial_list_partial.html', students=list_trial_students())
    # GET request
    return render_template('student_advisor/trial_add.html')

@student_advisor_bp.route('/trial/list')
def trial_list():
    students = list_trial_students()
    return render_template('student_advisor/trial_list_partial.html', students=students)


@student_advisor_bp.route('/trial/update_status/<int:student_id>', methods=['POST'])
def trial_update_status(student_id):
    status = request.form['status']
    update_trial_status(student_id, status)
    # return updated table HTMX
    return render_template('student_advisor/trial_list_partial.html', students=list_trial_students())

@student_advisor_bp.route('/student/list')
def student_list():
    students = list_joined_students()
    return render_template('student_advisor/student_list.html', students=students)

@student_advisor_bp.route('/classroom/list')
def classroom_list():
    classrooms = list_classrooms()
    return render_template('student_advisor/classroom_list.html', classrooms=classrooms)
