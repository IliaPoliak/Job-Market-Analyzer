from sqlalchemy.orm import declarative_base, relationship 
from sqlalchemy import Column, Integer, String, Text, ForeignKey, Table


Base = declarative_base()


job_skill = Table(
    "job_skill",
    Base.metadata,

    Column(
        "job_posting_id",
        ForeignKey("job_postings.id"),
        primary_key=True
    ),

    Column(
        "skill_id",
        ForeignKey("skills.id"),
        primary_key=True
    )
)


class JobPosting(Base):
    
    __tablename__ = "job_postings"

    id = Column(Integer, primary_key=True)

    # Job Title
    title = Column(String)

    # Link to the job posting
    link = Column(String)

    # Unique id from the website
    offer_id = Column(String)

    employer = Column(String)
    job_location = Column(String)
    salary = Column(String)
    when_posted = Column(String)

    description = Column(Text)

    skills = relationship(
        "Skill",
        secondary=job_skill,
        back_populates="job_postings"
    )


class Skill(Base):

    __tablename__ = "skills"

    id = Column(Integer, primary_key=True)

    name = Column(String, unique=True)

    category = Column(String)

    job_postings = relationship(
        "JobPosting",
        secondary=job_skill,
        back_populates="skills"
    )
