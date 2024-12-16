from flask import Blueprint, render_template
from .models import Student

views = Blueprint('views', __name__)

@views.route('/')
def home():
    students = Student.query.all()
    return render_template('attendance.html', student=students)
