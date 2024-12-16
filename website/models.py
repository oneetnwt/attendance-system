from . import db
from flask_login import UserMixin
from datetime import datetime

current_time = datetime.now()
noon = current_time.replace(hour=12, minute=0, second=0, microsecond=0)

class Student(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    studentID = db.Column(db.String(10), unique = True)
    name = db.Column(db.String(), unique = True)
    if current_time < noon:
        am = current_time  # Update AM attendance
    else:
        pm = current_time  # Update PM attendance


