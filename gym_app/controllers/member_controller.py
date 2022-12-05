from flask import render_template, redirect, request
from flask import Blueprint
from models.member import Member
import repositories.member_repo as member_repo

members_blueprint = Blueprint('members', __name__)

# READ - Show All
@members_blueprint.route('/members', methods=['GET'])
def all_members():
    members = member_repo.select_all()
    return render_template('members/index.html', members = members)

# READ - Show One
@members_blueprint.route('/members/<int:id>', methods=['GET'])
def one_member(id):
    member = member_repo.select(id)
    return render_template('members/show.html', member = member)

# CREATE - GET - Show form
@members_blueprint.route('/members/new', methods=['GET'])
def create_member_form():
    return render_template('members/new.html')

# CREATE - POST - Process request
@members_blueprint.route('/members/new', methods=['POST'])
def create_member_save():
    form_data = request.form
    first_name = form_data['first_name']
    last_name = form_data['last_name']
    is_premium = form_data['is_premium']
    is_active = form_data['is_active']
    member = Member(first_name, last_name, is_premium, is_active)
    member = member_repo.save(member)
    return redirect(f'/members/{member.id}')

# EDIT - GET - Show form
@members_blueprint.route('/members/<int:id>/edit', methods=['GET'])
def one_member_edit_show(id):
    member = member_repo.select(id)
    return render_template('members/edit.html', member = member)

# EDIT - POST - Process request
@members_blueprint.route('/members/<int:id>/edit', methods=['POST'])
def one_member_edit_save(id):
    form_data = request.form
    first_name = form_data['first_name']
    last_name = form_data['last_name']
    is_premium = form_data['is_premium']
    is_active = form_data['is_active']
    member = Member(first_name, last_name, is_premium, is_active, id)
    member_repo.update(member)
    return redirect(f'/members/{id}')

# DELETE - POST - Process request
@members_blueprint.route('/members/<int:id>/delete', methods=['POST'])
def one_member_delete(id):
    member_repo.delete(id)
    return redirect('/members')