from app import create_app, db
from models import Project, Skill, Experience

app = create_app()

def seed_database():
    with app.app_context():
        # Clear existing data to avoid duplicates
        db.drop_all()
        db.create_all()

        # 1. Add Your REAL Projects
        p1 = Project(
            title="VAL APP",
            description="A backend application for value-added services with scalable architecture and robust API design.",
            technologies="Python, Flask, REST API, PostgreSQL",
            github_link="",
            demo_link="https://val-site-puce.vercel.app/shopping.html",  # <-- LIVE LINK ADDED
            image_url=""
        )
        
        p2 = Project(
            title="Print Hub",
            description="An online printing platform making document services more convenient and accessible for students.",
            technologies="Python, Flask, PostgreSQL, Web Development",
            github_link="",
            demo_link="https://printhubug.com",
            image_url=""
        )

        p3 = Project(
            title="GURA",
            description="A marketplace connecting computer technicians, repair shops, and customers to find trusted technology services.",
            technologies="Python, Flask, PostgreSQL, Marketplace",
            github_link="",
            demo_link="https://gura-bp8d.onrender.com/",  # <-- LIVE LINK ADDED
            image_url=""
        )

        p4 = Project(
            title="Professional Portfolio",
            description="This very website! A dynamic, database-driven portfolio built to showcase my skills, projects, and experience.",
            technologies="Python, Flask, PostgreSQL, HTML, Tailwind CSS",
            github_link="",
            image_url="/static/images/gallery/headshot.jpeg",
            demo_link="https://ahumuza-portfolio.onrender.com/"  # <-- LIVE LINK ADDED
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
            description="Successfully developed and deployed multiple web applications including VAL APP, Print Hub, and Gura.",
            type="contract"
        )
        
        e2 = Experience(
            title="Computer Science Student",
            organization="Kabale University",
            duration="August 2025 - Present",
            description="Second-year student pursuing Bachelor's degree in Computer Science.",
            type="education"
        )
        
        db.session.add_all([e1, e2])

        # Commit to database
        db.session.commit()
        print("✅ Database seeded successfully with REAL projects: VAL APP, Print Hub, Gura, and Portfolio!")

if __name__ == '__main__':
    seed_database()