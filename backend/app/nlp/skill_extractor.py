import re
from typing import List, Set, Dict

# Comprehensive technical & soft skills taxonomy
SKILL_TAXONOMY = {
    # Programming Languages
    "python": "Python", "typescript": "TypeScript", "javascript": "JavaScript", "java": "Java",
    "c++": "C++", "cpp": "C++", "c#": "C#", "golang": "Go", "go": "Go", "rust": "Rust",
    "ruby": "Ruby", "php": "PHP", "swift": "Swift", "kotlin": "Kotlin", "sql": "SQL",
    "html": "HTML5", "css": "CSS3", "r": "R", "scala": "Scala", "bash": "Bash/Shell",

    # Frontend & Web Frameworks
    "react": "React", "react.js": "React", "next.js": "Next.js", "nextjs": "Next.js",
    "vue": "Vue.js", "vue.js": "Vue.js", "angular": "Angular", "svelte": "Svelte",
    "tailwind": "Tailwind CSS", "tailwindcss": "Tailwind CSS", "bootstrap": "Bootstrap",
    "redux": "Redux", "graphql": "GraphQL", "webpack": "Webpack", "vite": "Vite",

    # Backend & API Frameworks
    "fastapi": "FastAPI", "django": "Django", "flask": "Flask", "node.js": "Node.js",
    "nodejs": "Node.js", "express": "Express.js", "nest.js": "NestJS", "nestjs": "NestJS",
    "spring": "Spring Boot", "springboot": "Spring Boot", "asp.net": "ASP.NET",
    "rest api": "REST APIs", "restful": "REST APIs", "gRPC": "gRPC", "microservices": "Microservices",

    # Databases & Caching
    "mongodb": "MongoDB", "postgresql": "PostgreSQL", "postgres": "PostgreSQL",
    "mysql": "MySQL", "sqlite": "SQLite", "redis": "Redis", "cassandra": "Cassandra",
    "elasticsearch": "Elasticsearch", "dynamodb": "DynamoDB", "neo4j": "Neo4j",
    "pinecone": "Pinecone", "chromadb": "ChromaDB", "weaviate": "Weaviate",

    # Cloud & DevOps Infrastructure
    "aws": "AWS", "amazon web services": "AWS", "azure": "Azure", "gcp": "Google Cloud (GCP)",
    "google cloud": "Google Cloud (GCP)", "docker": "Docker", "kubernetes": "Kubernetes",
    "k8s": "Kubernetes", "terraform": "Terraform", "ansible": "Ansible",
    "ci/cd": "CI/CD Pipelines", "jenkins": "Jenkins", "github actions": "GitHub Actions",
    "git": "Git", "linux": "Linux", "nginx": "Nginx", "kafka": "Apache Kafka",

    # AI, Machine Learning & Data Science
    "machine learning": "Machine Learning", "deep learning": "Deep Learning",
    "artificial intelligence": "AI", "tensorflow": "TensorFlow", "pytorch": "PyTorch",
    "scikit-learn": "Scikit-Learn", "sklearn": "Scikit-Learn", "pandas": "Pandas",
    "numpy": "NumPy", "opencv": "OpenCV", "nlp": "Natural Language Processing (NLP)",
    "langchain": "LangChain", "langgraph": "LangGraph", "llm": "LLMs",
    "transformers": "Hugging Face Transformers", "mlops": "MLOps", "spacy": "spaCy",

    # Testing & Architecture
    "unit testing": "Unit Testing", "pytest": "PyTest", "jest": "Jest",
    "system design": "System Design", "agile": "Agile/Scrum", "jira": "Jira"
}

def extract_skills_from_text(text: str) -> List[str]:
    """Dynamically extracts recognized skills from raw text using boundary regex matching."""
    if not text:
        return []

    text_lower = text.lower()
    found_skills: Set[str] = set()

    for keyword, canonical_name in SKILL_TAXONOMY.items():
        # Match as whole word / token
        pattern = r'(?:\b|_)' + re.escape(keyword) + r'(?:\b|_)'
        if re.search(pattern, text_lower):
            found_skills.add(canonical_name)

    return sorted(list(found_skills))

def extract_key_phrases(text: str, top_n: int = 15) -> List[str]:
    """Extracts prominent technical nouns and multi-word phrases from text."""
    if not text:
        return []
    
    # Remove special chars except +, #, ., /
    cleaned = re.sub(r'[^a-zA-Z0-9\s\+#\./\-]', ' ', text)
    words = [w.strip() for w in cleaned.split() if len(w.strip()) > 2]
    
    stop_words = {
        "and", "the", "for", "with", "that", "this", "from", "have", "will", "your",
        "about", "work", "team", "building", "experience", "required", "preferred",
        "responsibilities", "requirements", "candidate", "role", "looking", "must"
    }

    filtered_words = [w for w in words if w.lower() not in stop_words]
    
    freq: Dict[str, int] = {}
    for w in filtered_words:
        w_norm = w.title()
        freq[w_norm] = freq.get(w_norm, 0) + 1

    sorted_phrases = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return [phrase for phrase, count in sorted_phrases[:top_n]]
