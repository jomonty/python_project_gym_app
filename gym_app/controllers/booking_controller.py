from datetime import date, time
from flask import render_template, redirect, request
from flask import Blueprint
from models.booking import Booking
import repositories.booking_repo as booking_repo
import repositories.gym_class_repo as gym_class_repo

bookings_blueprint = Blueprint('bookings', __name__)

# READ - GET - Show all bookings
@bookings_blueprint.route('/bookings', methods=['GET'])
def all_bookings():
    bookings = booking_repo.select_all()
    bookings.sort(key=lambda x: x.create_date, reverse=True)
    return render_template('bookings/index.html', bookings = bookings)

# DELETE - GET - Process request
@bookings_blueprint.route('/booking/<int:id>/delete', methods=['GET'])
def one_booking_delete(id):
    booking_repo.delete(id)
    return redirect('/bookings')

@bookings_blueprint.route('/bookings/new', methods=['GET'])
def new_booking_handler():
    class_names = gym_class_repo.select_distinct_classes()
    class_names.sort()
    return render_template('bookings/new_base.html', class_names = class_names)

@bookings_blueprint.route('/bookings/new', methods=['POST'])
def new_booking_class():
    form_data = request.form
    class_name = form_data['class_name']
    return render_template('bookings/new.html', class_name = class_name)



# CREATE - GET - Show booking view of class
# Display class info, full/not full, if class is premium
# Shows list of members available to book (search?) by premium/not premium
# button request - managed through GET

# Header
# Class Info
# Member booking
# Members booked as cards
