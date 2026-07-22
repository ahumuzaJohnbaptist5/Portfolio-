from app import db
from datetime import datetime
from extensions import db  # CHANGE THIS LINE


# --- PROJECT MODEL ---
class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    technologies = db.Column(db.String(200), nullable=False) # e.g., "Python, Flask, PostgreSQL"
    github_link = db.Column(db.String(200), default='')
    demo_link = db.Column(db.String(200), default='')
    image_url = db.Column(db.String(200), default='')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# --- SKILL MODEL ---
class Skill(db.Model):
    __tablename__ = 'skills'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False) # e.g., "Languages", "Frameworks", "Tools"
    proficiency = db.Column(db.Integer, default=80) # Percentage 0-100 for the progress bar

# --- EXPERIENCE MODEL ---
class Experience(db.Model):
    __tablename__ = 'experiences'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    organization = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.String(50), nullable=False) # e.g., "Jan 2025 - Present"
    description = db.Column(db.Text, nullable=False)
    type = db.Column(db.String(20), default='contract') # 'contract', 'internship', 'volunteer'

    # --- CONTACT MESSAGE MODEL ---
class ContactMessage(db.Model):
    __tablename__ = 'contact_messages'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(200), default='General Inquiry')
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)