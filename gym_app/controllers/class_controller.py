from flask import render_template, redirect, request
from flask import Blueprint
from models.gym_class import GymClass
import repositories.gym_class_repo as gym_class_repo

classes_blueprint = Blueprint('classes', __name__)

# READ - GET - Show all
@classes_blueprint.route('/classes', methods=['GET'])
def all_classes():
    classes = gym_class_repo.select_all()
    return render_template('classes/index.html', classes = classes)

# READ - GET - Show all upcoming

# READ - GET - Show One

# CREATE - GET - Show form

# CREATE - POST - Process request

# EDIT - GET - Show form

# EDIT - POST - Process Request

# DELETE - POST - Process Request