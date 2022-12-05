from datetime import date, time
from flask import render_template, redirect, request
from flask import Blueprint
from models.gym_class import GymClass
import repositories.gym_class_repo as gym_class_repo

classes_blueprint = Blueprint('classes', __name__)

# READ - GET - Show all upcoming
@classes_blueprint.route('/classes', methods=['GET'])
def all_classes_upcoming():
    classes = gym_class_repo.select_all(upcoming=True)
    return render_template('classes/index.html', classes = classes)

# READ - GET - Show all historical
@classes_blueprint.route('/classes/historical', methods=['GET'])
def all_classes_historical():
    classes = gym_class_repo.select_all(historical=True)
    return render_template('classes/historical.html', classes = classes)

# READ - GET - Show all inactive
@classes_blueprint.route('/classes/inactive', methods=['GET'])
def all_classes_inactive():
    classes = gym_class_repo.select_all(inactive=True)
    return render_template('classes/inactive.html', classes = classes)

# READ - GET - Show all
@classes_blueprint.route('/classes/all', methods=['GET'])
def all_classes():
    classes = gym_class_repo.select_all()
    return render_template('classes/all.html', classes = classes)

# READ - GET - Show One
@classes_blueprint.route('/classes/<int:id>', methods=['GET'])
def one_class(id):
    gym_class = gym_class_repo.select(id)
    return render_template('classes/show.html', gym_class = gym_class)

# CREATE - GET - Show form
@classes_blueprint.route('/classes/new', methods=['GET'])
def create_class_form():
    return render_template('classes/new.html')

# CREATE - POST - Process request
@classes_blueprint.route('/classes/new', methods=['POST'])
def create_class_save():
    form_data = request.form
    name = form_data['name']
    class_date = date.fromisoformat(form_data['class_date'])
    class_time = time.fromisoformat(form_data['class_time'])
    capacity = int(form_data['capacity'])
    is_active = 'active' in form_data
    gym_class = GymClass(name, class_date, class_time, capacity, is_active)
    gym_class = gym_class_repo.save(gym_class)
    return redirect(f'/classes/{gym_class.id}')

# EDIT - GET - Show form
@classes_blueprint.route('/classes/<int:id>/edit', methods=['GET'])
def one_class_edit_show(id):
    gym_class = gym_class_repo.select(id)
    return render_template('classes/edit.html', gym_class = gym_class)

# EDIT - POST - Process Request
@classes_blueprint.route('/classes/<int:id>/edit', methods=['POST'])
def one_class_edit_save(id):
    form_data = request.form
    name = form_data=['name']
    class_date = date.fromisoformat(form_data['class_date'])
    class_time = time.fromisoformat(form_data['class_time'])
    capacity = int(form_data['capacity'])
    is_active = 'active' in form_data
    gym_class = GymClass(name, class_date, class_time, capacity, is_active, id)
    gym_class_repo.save(gym_class)
    return redirect(f'/classes/{id}')

# DELETE - POST - Process Request
@classes_blueprint.route('/classes/<int:id>/delete', methods=['GET'])
def one_class_delete(id):
    gym_class_repo.delete(id)
    return redirect('/classes')