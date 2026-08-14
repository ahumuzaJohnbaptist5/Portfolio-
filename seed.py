from app import create_app, db
from models import Project, Skill, Experience

app = create_app()

def seed_database():
    with app.app_context():
        # Clear existing data to avoid duplicates (optional but recommended when updating)
        db.drop_all()
        db.create_all()

        # 1. Add Your REAL Projects
        p1 = Project(
            title="VAL APP",
            description="A successful backend application for value-added services. Built with scalable architecture and robust API design.",
            technologies="Python, Flask, REST API, Database Management",
            github_link="https://github.com/ahumuzaJohnbaptist5/VAL_APP",
            image_url="", # Add '/static/images/gallery/val_app.png' later if you have a screenshot
            demo_link="#"
        )
        
        p2 = Project(
            title="Print Hub",
            description="A comprehensive printing solution platform. Successfully deployed and serving users with efficient document management.",
            technologies="Python, Flask, PostgreSQL, Web Development",
            github_link="https://github.com/ahumuzaJohnbaptist5/print_hub",
            image_url="", # Add '/static/images/gallery/print_hub.png' later if you have a screenshot
            demo_link="#"
        )

        p3 = Project(
            title="Gura",
            description="A successful and impactful project demonstrating strong software development skills and problem-solving abilities.",
            technologies="Python, Flask, PostgreSQL, Web Development",
            github_link="https://github.com/ahumuzaJohnbaptist5/Gura",
            image_url="", # Add '/static/images/gallery/gura.png' later if you have a screenshot
            demo_link="#"
        )
        
        p4 = Project(
            title="Professional Portfolio",
            description="This very website! A dynamic, database-driven portfolio built to showcase my skills, projects, and experience to potential employers and investors.",
            technologies="Python, Flask, PostgreSQL, HTML, Tailwind CSS",
            github_link="https://github.com/ahumuzaJohnbaptist5/Portfolio-",
            image_url="/static/images/gallery/headshot.jpeg",
            demo_link="http://127.0.0.1:5000"
        )

        db.session.add_all([p1, p2, p3, p4])

        # 2. Add Skills
        skills_data = [
            ("Python", "Languages", 85),
            ("JavaScript", "Languages", 75),
            ("Flask", "Frameworks", 85),
            ("PostgreSQL", "Databases", 80),
            ("HTML/Tailwind CSS", "Frontend", 90),
            ("REST API", "Backend", 80),
            ("Git/GitHub", "Tools", 85)
        ]
        
        for name, category, proficiency in skills_data:
            db.session.add(Skill(name=name, category=category, proficiency=proficiency))

        # 3. Add Experience
        e1 = Experience(
            title="Full-Stack Developer",
            organization="Freelance / Personal Projects",
            duration="2025 - Present",
            description="Successfully developed and deployed multiple web applications including VAL APP, Print Hub, and Gura. Built scalable backend systems and responsive frontend interfaces.",
            type="contract"
        )
        
        e2 = Experience(
            title="Computer Science Student",
            organization="Kabale University",
            duration="August 2025 - Present",
            description="Second-year student pursuing Bachelor's degree in Computer Science. Actively working on real-world projects and contributing to software development.",
            type="education"
        )

        e3 = Experience(
                    title="Computer Technician",
                    organization="JBRO Computer Solutions",
                    duration="March 2025 - Present",
                    description="I graduated from ACCT Kabale as a computer technican as an accupational skill accredited by UVITAB. Actively doing computer maintenance and support, printing, printer servicing and my others.",
                    type="education"
                )
        
        db.session.add_all([e1, e2])

        # Commit to database
        db.session.commit()
        print("✅ Database seeded successfully with REAL projects: VAL APP, Print Hub, Gura, and Portfolio!")

if __name__ == '__main__':
    seed_database()