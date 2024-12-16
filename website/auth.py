from flask import Blueprint, render_template, request, redirect, flash, url_for
from .models import Student
from . import db
from datetime import datetime

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        studentID = request.form.get('studentID')
        name = request.form.get('name')

        if len(studentID) != 10:
            flash('Student ID must be a 10-digit number', category = 'error')
        else:
            new_student = Student(studentID = studentID, name = name)
            db.session.add(new_student)
            db.session.commit()
            flash('Registered Successfully', category = 'success')
            return redirect(url_for('auth.login'))

    return render_template('register.html')

@auth.route('/log', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        studentID = request.form.get('studentID')

        if not studentID:
            flash("Student ID is required", category='error')
        elif not studentID.isdigit() or len(studentID) != 10:
            flash("Student ID must be a 10-digit number", category='error')
        else:
            # Check if student exists in the database
            student = Student.query.filter_by(studentID=studentID).first()
            if student:
                current_time = datetime.now()
                noon = current_time.replace(hour=12, minute=0, second=0, microsecond=0)

                if current_time < noon:  # AM Login
                    flash("Logged in during AM", category='success')
                    student.am = current_time  # Update AM login time
                else:  # PM Login
                    flash("Logged in during PM", category='success')
                    student.pm = current_time  # Update PM login time

                # Save changes to the database
                db.session.commit()
                return redirect('/')
            else:
                flash("Student ID does not exist", category='error')

    return render_template('log.html')