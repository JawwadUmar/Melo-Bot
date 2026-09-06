KEY_SKILLS = [
    # Programming Languages
    "Java",
    "Python",
    "Go",
    "Golang",
    "C++",
    "JavaScript",
    "TypeScript",
    "Groovy",

    # Backend & Frameworks
    "Spring Boot",
    "Spring Batch",
    "FastAPI",
    "Dropwizard",
    "Node.js",
    "Express",
    "Gin",
    "JPA",
    "Hibernate",
    "Spring JDBC",

    # AI / LLM / Machine Learning
    "Generative AI",
    "Artificial Intelligence",
    "Machine Learning",
    "LLM",
    "LLM Engineering",
    "AI Agents",
    "AI Agent Workflows",
    "LangChain",
    "LangGraph",
    "RAG",
    "Prompt Engineering",
    "Model Context Protocol",
    "MCP",
    "Amazon Bedrock",

    # Distributed Systems & Streaming
    "Apache Kafka",
    "Kafka",
    "Avro",
    "Confluent Schema Registry",
    "Event-Driven Architecture",
    "Microservices",
    "ETL",
    "Data Pipelines",

    # Databases
    "PostgreSQL",
    "MySQL",
    "MongoDB",
    "Redis",
    "SQL",
    "JPA",
    "Hibernate",

    # Cloud & AWS
    "AWS",
    "AWS Lambda",
    "AWS EC2",
    "AWS S3",
    "AWS ECS",
    "AWS KMS",
    "AWS EventBridge",
    "AWS SNS",
    "AWS SQS",
    "AWS CloudTrail",
    "Google Cloud",
    "Google Cloud Run",

    # Frontend
    "React",
    "Angular",
    "HTML",
    "CSS",

    # DevOps & Infrastructure
    "Docker",
    "CI/CD",
    "GitLab CI/CD",
    "GitHub Actions",
    "Datadog",
    "Cloud-Native",

    # Testing
    "JUnit",
    "Spock",
    "Gherkin",

    # Computer Vision / OCR
    "OCR",
    "Pytesseract",
    "Azure Computer Vision",
    "AWS Textract",

    # Architecture & CS
    "System Design",
    "Data Structures",
    "Algorithms",
    "Object-Oriented Programming",
    "OOP",
    "Design Patterns",

    # APIs & Security
    "REST APIs",
    "JWT",
    "Authentication",
    "Authorization",

    # Browser Automation
    "Playwright",
    "Browser Automation",
]

KEY_SKILLS_SET = {skill.lower().strip() for skill in KEY_SKILLS}


from app.config.setting import SKILL_MATCH_THRESHOLD


def skillMatch(skills: list[str])->bool:
    if not skills:
        return True
    
    cleaned_incoming_skills = [s.lower().strip() for s in skills if s and s.strip()]
    if not cleaned_incoming_skills:
        return True

    match_count = sum(1 for skill in cleaned_incoming_skills if skill in KEY_SKILLS_SET)

    if match_count == len(cleaned_incoming_skills):
        return True

    return match_count >= SKILL_MATCH_THRESHOLD

    