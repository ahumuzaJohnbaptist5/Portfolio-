from app import create_app, db
from extensions import db
from models import Project, Skill, Experience

app = create_app()

def seed_database():
    with app.app_context():
        # Clear existing data (optional, but good for restarting)
        db.drop_all()
        db.create_all()

        # 1. Add Projects
        p1 = Project(
            title="Student Management System",
            description="A web application to manage student records, grades, and attendance for Kabale University.",
            technologies="Python, Flask, PostgreSQL, HTML, Tailwind CSS",
            github_link="https://github.com/yourusername/project1",
            demo_link="#"
        )
        p2 = Project(
            title="NGO Donation Tracker",
            description="A platform designed for NGOs to track donations, allocate resources, and generate impact reports.",
            technologies="Flask, JavaScript, PostgreSQL, Chart.js",
            github_link="https://github.com/yourusername/project2",
            demo_link="#"
        )
        db.session.add_all([p1, p2])

        # 2. Add Skills
        s1 = Skill(name="Python", category="Languages", proficiency=85)
        s2 = Skill(name="JavaScript", category="Languages", proficiency=75)
        s3 = Skill(name="Flask", category="Frameworks", proficiency=80)
        s4 = Skill(name="PostgreSQL", category="Databases", proficiency=70)
        s5 = Skill(name="HTML/Tailwind", category="Frontend", proficiency=90)
        db.session.add_all([s1, s2, s3, s4, s5])

        # 3. Add Experience
        e1 = Experience(
            title="Freelance Web Developer",
            organization="Self-Employed",
            duration="Aug 2025 - Present",
            description="Building responsive web applications for local businesses using Flask and Tailwind CSS.",
            type="contract"
        )
        e2 = Experience(
            title="IT Support Intern",
            organization="Local Tech Hub",
            duration="Jan 2025 - May 2025",
            description="Assisted in network troubleshooting and hardware maintenance for university computer labs.",
            type="internship"
        )
        db.session.add_all([e1, e2])

        # Commit to database
        db.session.commit()
        print("✅ Database seeded successfully with projects, skills, and experience!")

if __name__ == '__main__':
    seed_database()