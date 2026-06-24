from database.database import engine, SessionLocal
from database.models import Base, JobPosting, Skill, job_skill
from config.skills import PROGRAMMING_LANGUAGES, WEB_FRONTEND, WEB_BACKEND, DATABASES, CLOUD_AND_DEVOPS, DATA_AND_ML, MOBILE, TESTING, APIS_AND_PROTOCOLS, VERSION_CONTROL_AND_COLLABORATION, ARCHITECTURE_AND_PATTERNS, SECURITY, SOFT_SKILLS
from logger.logging_utils import start_timing, finish_timing


def save_to_db(data):

    skills, job_postings = _prepare_data(data)

    _save(skills, job_postings)    
    

def _save(skills, job_postings):

    start = start_timing("SAVING TO DATABASE")

    # Connect
    Base.metadata.create_all(engine) 
    
    # Start session
    session = SessionLocal() 

    # Delete tables
    session.execute(job_skill.delete())
    session.query(JobPosting).delete()
    session.query(Skill).delete()

    # Add new data to tables
    session.add_all(skills)
    session.add_all(job_postings)

    # Commit changes
    session.commit()
    
    # End Session
    session.close()    

    finish_timing(start)


def _prepare_data(data):

    start = start_timing("PREPARING DATA FOR DATABASE SAVING")
    
    skills_array, skills_dict = _prepare_skills() 
    
    job_postings = _prepare_job_postings(data, skills_dict)
    
    finish_timing(start)

    return skills_array, job_postings 


def _prepare_skills():

    skills_array = []
    skills_dict = {}

    category_mapping = {
        "Programming Languages": PROGRAMMING_LANGUAGES,
        "Web Frontend": WEB_FRONTEND,
        "Web Backend": WEB_BACKEND,
        "Databases": DATABASES,
        "Cloud and DevOps": CLOUD_AND_DEVOPS,
        "Data and ML": DATA_AND_ML, 
        "Mobile": MOBILE, 
        "Testing": TESTING, 
        "APIs and Protocols": APIS_AND_PROTOCOLS, 
        "Version Control and Collaboration": VERSION_CONTROL_AND_COLLABORATION, 
        "Architecture and Patterns": ARCHITECTURE_AND_PATTERNS, 
        "Security": SECURITY, 
        "Soft Skills": SOFT_SKILLS
    }

    for category_name, skill_list in category_mapping.items():
        for skill_name in skill_list:
            
            skill_object = Skill(name=skill_name, category=category_name)

            skills_array.append(skill_object)
            skills_dict[skill_name] = skill_object

    return skills_array, skills_dict


def _prepare_job_postings(data, skills_dict):
    
    job_postings = []

    for index, row in data.iterrows():

        posting = JobPosting(
                title=row["Title"], 
                link=row["Link"], 
                offer_id=row["Offer ID"], 
                employer=row["Employer"], 
                job_location=row["Job Location"], 
                salary=row["Salary"], 
                when_posted=row["When Posted"], 
                description=row["Description"]
            )

        for skill_name in row["Skills"]:
            skill_object = skills_dict[skill_name]

            if skill_object:
                posting.skills.append(skill_object)

        job_postings.append(posting)

    return job_postings
