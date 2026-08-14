from flask import Blueprint, render_template, request, redirect, url_for
from models import Project, Skill, Experience, ContactMessage
from extensions import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    projects = Project.query.order_by(Project.created_at.desc()).all()
    skills = Skill.query.all()
    experiences = Experience.query.all()
    
    return render_template(
        'index.html', 
        projects=projects, 
        skills=skills, 
        experiences=experiences
    )

@main_bp.route('/contact', methods=['POST'])
def contact_submit():
    name = request.form.get('name')
    email = request.form.get('email')
    subject = request.form.get('subject')
    message = request.form.get('message')
    
    new_message = ContactMessage(
        name=name,
        email=email,
        subject=subject,
        message=message
    )
    
    db.session.add(new_message)
    db.session.commit()
    
    return redirect(url_for('main.thank_you'))

@main_bp.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')