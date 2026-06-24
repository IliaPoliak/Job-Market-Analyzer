from fastapi import APIRouter
from database.database import SessionLocal
from database.models import JobPosting, Skill
from sqlalchemy import func


router = APIRouter(tags=["Analytics"])


@router.get("/relevant_skills")
def get_relevant_skills():
    
    db = SessionLocal()
    
    # Query to get skills with their counts
    skills_with_counts = db.query(
        Skill.name.label('skill'),
        Skill.category.label('category'),
        func.count(JobPosting.id).label('count')
    ).join(
        JobPosting.skills
    ).group_by(
        Skill.id
    ).order_by(
        func.count(JobPosting.id).desc()
    ).all()
    
    db.close()
    
    # Convert to list of dictionaries for JSON response
    result = [
        {"skill": skill, "category": category, "count": count} 
        for skill, category, count in skills_with_counts
    ]
    
    return result


@router.get("/most_hiring_companies")
def get_most_hiring_companies():
    
    db = SessionLocal()
    
    # Query to get companies and counts
    companies_with_counts = db.query(
        JobPosting.employer.label('company'),
        func.count(JobPosting.id).label('count')
    ).group_by(
        JobPosting.employer
    ).order_by(
        func.count(JobPosting.id).desc()
    ).all()
    
    db.close()
    
    # Convert to list of dictionaries for JSON response
    result = [
        {"company": company, "count": count} 
        for company, count in companies_with_counts
    ]
    
    return result
