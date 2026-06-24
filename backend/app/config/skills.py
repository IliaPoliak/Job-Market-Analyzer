PROGRAMMING_LANGUAGES = {
    "Python": [], 
    "JavaScript": [], 
    "TypeScript": [], 
    "Java": [], 
    "Kotlin": [], 
    "Scala": [], 
    "Go": ["Golang"],
    "Rust": [], 
    "C++": [], 
    "C#": [], 
    "Ruby": [], 
    "PHP": [],
    "Swift": [], 
    "R": [], 
    "MATLAB": [], 
    "Perl": [],
    "Bash": [], 
    "Shell": [], 
    "PowerShell": [], 
    "Groovy": [], 
    "Lua": [], 
    "Haskell": [], 
    "Elixir": [], 
    "Clojure": [],
    "Dart": [], 
    "Objective-C": [], 
    "Assembly": [], 
    "COBOL": [], 
    "Fortran": [],
}

WEB_FRONTEND = {
    "React": [], 
    "Vue": [], 
    "Angular": [], 
    "Svelte": [], 
    "Next.js": [], 
    "Nuxt": [], 
    "Gatsby": [], 
    "Remix": [],
    "HTML": [], 
    "CSS": [], 
    "Sass": ["SCSS"],
    "Less": [], 
    "Tailwind": ["Tailwind CSS"], 
    "Bootstrap": [], 
    "jQuery": [],
    "Webpack": [], 
    "Vite": [], 
    "Rollup": [], 
    "Babel": [], 
    "Storybook": [], 
    "Apollo": [],
}

WEB_BACKEND = {
    "Node.js": [], 
    "Express": ["Express.js"], 
    "FastAPI": [], 
    "Flask": [], 
    "Django": [], 
    "Spring": [], 
    "Spring Boot": [],
    "Ruby on Rails": [], 
    "Laravel": [], 
    "ASP.NET": [], 
    "NestJS": [], 
    "Hapi": [], 
    "Koa": [], 
    "Gin": [], 
    "Fiber": [],
    "Actix": [], 
    "Rocket": [], 
    "Phoenix": [], 
    "Sinatra": [],
}

DATABASES = {
    "SQL": [], 
    "MySQL": [], 
    "PostgreSQL": [], 
    "SQLite": [], 
    "Oracle": [], 
    "MSSQL": [], 
    "SQL Server": [],
    "MongoDB": [], 
    "Redis": [], 
    "Cassandra": [], 
    "DynamoDB": [], 
    "Elasticsearch": [], 
    "Neo4j": [], 
    "CouchDB": [],
    "InfluxDB": [], 
    "Snowflake": [], 
    "BigQuery": [], 
    "Amazon Redshift": [], 
    "Supabase": [], 
    "Firebase": [],
    "MariaDB": [], 
    "CockroachDB": [],
}

CLOUD_AND_DEVOPS = {   
    "AWS": ["Amazon Web Services"], 
    "Microsoft Azure": [], 
    "Google Cloud": [], 
    "GCP": [],
    "Docker": [], 
    "Kubernetes": [], 
    "Terraform": [], 
    "Ansible": [], 
    "Puppet": [], 
    "Chef": [],
    "Jenkins": [], 
    "GitHub Actions": [], 
    "GitLab CI": [], 
    "CircleCI": [], 
    "Travis CI": [], 
    "ArgoCD": [], 
    "Helm": [],
    "Prometheus": [], 
    "Grafana": [], 
    "Datadog": [], 
    "Splunk": [], 
    "New Relic": [], 
    "NGINX": [], 
    "Apache": [], 
    "Linux": [],
}

DATA_AND_ML = {
    "Machine Learning": [], 
    "Deep Learning": [], 
    "Natural Language Processing": ["NLP"], 
    "Computer Vision": [], 
    "Large Language Models": ["LLM"],  
    "Generative AI": [],
    "TensorFlow": [], 
    "PyTorch": [], 
    "Keras": [], 
    "scikit-learn": [], 
    "pandas": [], 
    "NumPy": [],
    "SciPy": [], 
    "Matplotlib": [], 
    "Seaborn": [], 
    "Plotly": [], 
    "Apache Spark": [], 
    "Hadoop": [],
    "Apache Kafka": [], 
    "Apache Airflow": [], 
    "dbt": [], 
    "MLflow": [], 
    "Hugging Face": [],
    "LangChain": [], 
    "OpenAI": [], 
    "XGBoost": [], 
    "LightGBM": [], 
    "statsmodels": [],
}

MOBILE = {
    "Android": [], 
    "iOS": [], 
    "React Native": [], 
    "Flutter": [], 
    "Xamarin": [], 
    "Ionic": [],
    "SwiftUI": [], 
    "Jetpack Compose": [],
}

TESTING = {
    "Jest": [], 
    "pytest": [], 
    "JUnit": [], 
    "Selenium": [], 
    "Cypress": [], 
    "Playwright": [],
    "TestNG": [], 
    "Mocha": [], 
    "Chai": [], 
    "Vitest": [], 
    "RSpec": [], 
    "PHPUnit": [],
}

APIS_AND_PROTOCOLS = {
    "RESTful API": ["REST"], 
    "gRPC": [], 
    "WebSocket": [], 
    "GraphQL": [], 
    "SOAP": [], 
    "OAuth": [],
    "JWT": [], 
    "OpenAPI": [], 
    "Swagger": [],
}

VERSION_CONTROL_AND_COLLABORATION = {
    "Git": [], 
    "GitHub": [], 
    "GitLab": [], 
    "Bitbucket": [], 
    "Jira": [], 
    "Confluence": [], 
    "Notion": [],
    "Linear": [], 
    "Figma": [],
}

ARCHITECTURE_AND_PATTERNS = {
    "Microservices": [], 
    "Event-Driven Architecture": [], 
    "Serverless": [], 
    "CI/CD": [],
    "Test-Driven Development": ["TDD"], 
    "Behavior-Driven Development": ["BDD"], 
    "Agile": [], 
    "Scrum": [], 
    "Kanban": [], 
    "DevOps": [], 
    "DevSecOps": [], 
    "Site Reliability Engineering": ["SRE"], 
}

SECURITY = {
    "Cybersecurity": [], 
    "Penetration Testing": [], 
    "OWASP": [], 
    "SSO": [], 
    "SAML": [], 
    "LDAP": [],
    "Cryptography": [], 
    "SSL": [], 
    "TLS": [], 
    "IAM": [], 
    "Zero Trust": [],
}

SOFT_SKILLS = {
    "Communication": [], 
    "Leadership": [], 
    "Problem Solving": [], 
    "Collaboration": [],
    "Stakeholder Management": [], 
    "Project Management": [],
}

# Joined skills dictionarry
SKILLS_DICT = PROGRAMMING_LANGUAGES | WEB_FRONTEND | WEB_BACKEND | DATABASES | CLOUD_AND_DEVOPS | DATA_AND_ML | MOBILE | TESTING | APIS_AND_PROTOCOLS | VERSION_CONTROL_AND_COLLABORATION | ARCHITECTURE_AND_PATTERNS | SECURITY | SOFT_SKILLS

# Joined skills array, with aliases as separate items -> ["Go", "Golang"]
SKILLS_LIST = [
    skill
    for skill, aliases in SKILLS_DICT.items()
] + [
    alias
    for aliases in SKILLS_DICT.values()
    for alias in aliases
]

# The dict of skills that contain other skills to check whether skills are not registered by mistake during  data extraction
SKILLS_THAT_CONTAIN_OTHER_SKILLS = {
    "spring": ["boot"],
	"github": ["actions"],
	"gitlab": ["ci"],
	"react": ["native"],
	"sql": ["server"],
	"apache": ["spark", "kafka", "airflow"]
}