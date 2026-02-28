def analyze_resume(resume_text):
    resume_text = resume_text.lower()

    # Skill Categories
    technical_skills = [
        "python", "java", "c++", "sql", "flask",
        "django", "machine learning", "data science",
        "html", "css", "javascript"
    ]

    soft_skills = [
        "communication", "leadership", "teamwork",
        "problem solving", "adaptability"
    ]

    education_keywords = [
        "b.tech", "bachelor", "master", "m.tech",
        "phd", "degree", "university", "college"
    ]

    experience_keywords = [
        "intern", "experience", "worked at",
        "project", "developed", "built"
    ]

    found_technical = []
    found_soft = []
    found_education = []
    found_experience = []

    # Check technical skills
    for skill in technical_skills:
        if skill in resume_text:
            found_technical.append(skill)

    # Check soft skills
    for skill in soft_skills:
        if skill in resume_text:
            found_soft.append(skill)

    # Check education
    for word in education_keywords:
        if word in resume_text:
            found_education.append(word)

    # Check experience
    for word in experience_keywords:
        if word in resume_text:
            found_experience.append(word)

    # Improved scoring logic
    score = (
        len(found_technical) * 8 +
        len(found_soft) * 5 +
        len(found_experience) * 7 +
        len(found_education) * 5
    )

    if score > 100:
        score = 100

    suggestions = []

    if len(found_technical) < 4:
        suggestions.append("Add more technical skills relevant to your field.")

    if len(found_soft) < 2:
        suggestions.append("Include soft skills like communication or leadership.")

    if len(found_experience) == 0:
        suggestions.append("Mention internships, projects, or work experience.")

    if len(found_education) == 0:
        suggestions.append("Clearly mention your education background.")

    if score >= 70:
        suggestions.append("Strong profile! Add measurable achievements (numbers, results).")

    return {
        "score": score,
        "technical_skills": found_technical,
        "soft_skills": found_soft,
        "education": found_education,
        "experience": found_experience,
        "suggestions": suggestions
    }