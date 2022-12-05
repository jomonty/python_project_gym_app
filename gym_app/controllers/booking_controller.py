from datetime import date, time
from flask import render_template, redirect, request
from flask import Blueprint
from models.booking import Booking
import repositories.booking_repo as booking_repo
import repositories.gym_class_repo as gym_class_repo
import repositories.member_repo as member_repo

bookings_blueprint = Blueprint('bookings', __name__)

# READ - GET - Show all bookings
@bookings_blueprint.route('/bookings', methods=['GET'])
def all_bookings():
    bookings = booking_repo.select_all()
    bookings.sort(key=lambda x: x.create_date, reverse=True)
    return render_template('bookings/index.html', bookings = bookings)

# DELETE - GET - Process request
@bookings_blueprint.route('/bookings/<int:id>/delete', methods=['GET'])
def one_booking_delete(id):
    booking_repo.delete(id)
    return redirect(request.referrer)

@bookings_blueprint.route('/bookings/new', methods=['GET'])
def new_booking_handler():
    class_names = gym_class_repo.select_distinct_classes()
    class_names.sort()
    return render_template('bookings/class_choice.html', class_names = class_names)

@bookings_blueprint.route('/bookings/new/<string:class_name>', methods=['GET'])
def new_booking_class(class_name):
    gym_classes = gym_class_repo.select_all_upcoming_by_name(class_name)
    gym_class_status = {}
    for gym_class in gym_classes:
        gym_class_status[gym_class.id] = booking_repo.is_class_full(gym_class)
    return render_template('bookings/new_by_class.html', gym_classes = gym_classes, class_name = class_name, gym_class_status = gym_class_status)
    
@bookings_blueprint.route('/bookings/new/<int:id>', methods=['GET'])
def new_booking_member(id):
    gym_class = gym_class_repo.select(id)
    members = booking_repo.select_members_for_booking(gym_class)
    return render_template('bookings/new_by_member.html', gym_class = gym_class, members = members)

@bookings_blueprint.route('/bookings/new', methods=['POST'])
def new_booking_save():
    form_data = request.form
    member = member_repo.select(form_data['member_id'])
    gym_class = gym_class_repo.select(form_data['gym_class_id'])
    booking = Booking(gym_class, member)
    booking_repo.save(booking)
    return redirect('/bookings')
