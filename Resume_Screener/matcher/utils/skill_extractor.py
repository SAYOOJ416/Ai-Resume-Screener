import spacy 

nlp = spacy.load("en_core_web_sm")

SKILLs_DB =  [ "python", "java", "javascript", "c++", "c#", "ruby", "php", "swift", 
    "kotlin", "go", "rust", "typescript", "r", "matlab", "scala",
    
    # Web Frameworks
    "django", "flask", "fastapi", "react", "angular", "vue.js", "node.js",
    "express.js", "next.js", "spring boot", "asp.net", "laravel",
    
    # Databases
    "sql", "mysql", "postgresql", "mongodb", "redis", "cassandra", 
    "oracle", "sqlite", "dynamodb", "elasticsearch",
    
    # Cloud & DevOps
    "aws", "azure", "gcp", "docker", "kubernetes", "jenkins", "terraform",
    "ansible", "ci/cd", "github actions", "gitlab ci",
    
    # Data Science & ML
    "machine learning", "deep learning", "nlp", "computer vision",
    "tensorflow", "pytorch", "scikit-learn", "pandas", "numpy",
    "data analysis", "data visualization", "tableau", "power bi",
    
    # Frontend
    "html", "css", "sass", "bootstrap", "tailwind css", "jquery",
    "webpack", "responsive design", "ui/ux",
    
    # Tools & Others
    "git", "github", "gitlab", "jira", "agile", "scrum", "rest api",
    "graphql", "microservices", "linux", "bash", "shell scripting",
    "testing", "unit testing", "selenium", "jest", "pytest"]


def extract_skills_spacy(text):
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if not token.is_stop]

    found = set()

    for skill in SKILLs_DB:
        words = skill.split()
        if all(word in tokens for word in words):
            found.add(skill)

    return found

