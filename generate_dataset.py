import json
import random
from datetime import datetime, timedelta

# Profesional dan kompleks KEYWORDS
KEYWORDS = [
    'Artificial Intelligence', 'Blockchain Technology', 'Data Analytics', 'Quantum Computing',
    'Cloud Architecture', 'Cybersecurity Protocols', 'Internet of Things', 'Augmented Reality',
    '5G Networks', 'Autonomous Systems', 'Robotic Process Automation', 'Edge Computing',
    'Natural Language Processing', 'Predictive Analytics', 'Supply Chain Optimization',
    'Digital Twin Technology', 'Biometric Authentication', 'Cryptographic Algorithms',
    'Smart Contracts', 'Decentralized Finance', 'Machine Learning Models', 'Data Governance',
    'Digital Transformation', 'Regulatory Compliance', 'Virtual Reality', 'Sustainable Technologies',
    'Human-Computer Interaction', 'Digital Ecosystem', 'Advanced Robotics', 'Privacy Engineering',
    'Neural Networks', 'Ethical AI', 'Operational Resilience', 'Strategic Innovation',
    'User-Centered Design', 'Predictive Maintenance', 'Cyber-Physical Systems', 'Quantum Cryptography',
    'Distributed Ledger Technology', 'Industry 4.0', 'Data Privacy Regulations', 'AI-Powered Automation',
    'Global Supply Chains', 'Digital Identity', 'High-Performance Computing', 'Autonomous Vehicles',
    'Smart Infrastructure', 'Zero Trust Security', 'Data Sovereignty', 'Cognitive Computing'
]

# Profesional dan kompleks TOPICS
TOPICS = [
    'Enterprise Risk Management', 'Strategic Decision Making', 'Operational Efficiency',
    'Customer-Centric Innovation', 'Regulatory Compliance Strategies', 'Market Penetration Analysis',
    'Digital Product Development', 'Agile Transformation', 'Corporate Sustainability',
    'Data-Driven Decision Making', 'Cybersecurity Risk Mitigation', 'Global Market Expansion',
    'Digital Customer Experience', 'Supply Chain Resilience', 'Technological Disruption',
    'Data Monetization Strategies', 'Human Capital Management', 'Cross-Functional Collaboration',
    'Regulatory Technology (RegTech)', 'Business Process Automation', 'Corporate Governance',
    'Change Management', 'Cloud Security Strategies', 'Digital Talent Acquisition',
    'AI Ethics and Governance', 'Customer Retention Strategies', 'Product Lifecycle Management',
    'Innovative Business Models', 'Operational Risk Management', 'Financial Performance Optimization',
    'Technology Adoption and Integration', 'Organizational Agility', 'Customer Experience Enhancement',
    'Global Compliance Frameworks', 'Digital Marketing Strategies', 'Emerging Technology Adoption',
    'Corporate Social Responsibility', 'Business Intelligence and Analytics', 'Cyber Threat Intelligence',
    'Mergers and Acquisitions', 'Innovation Management', 'Blockchain Implementation',
    'Data Privacy and Protection', 'Strategic Workforce Planning', 'Digital Supply Chain Transformation',
    'IT Governance', 'Smart Manufacturing', 'Talent Development Programs', 'Operational Resilience'
]

# Profesional dan kompleks JOB_TITLES
JOB_TITLES = [
    'Chief Technology Officer', 'Data Science Lead', 'Cybersecurity Analyst', 'Digital Transformation Consultant',
    'Blockchain Solutions Architect', 'Machine Learning Engineer', 'Cloud Infrastructure Manager',
    'AI Ethics Officer', 'Data Privacy Officer', 'Product Innovation Director', 'Chief Information Security Officer',
    'Business Intelligence Analyst', 'Corporate Strategy Consultant', 'Digital Marketing Director',
    'Supply Chain Operations Manager', 'Regulatory Affairs Specialist', 'Corporate Sustainability Officer',
    'Chief Data Officer', 'Human Resources Technology Manager', 'Operations Research Analyst',
    'Agile Coach', 'Global Compliance Manager', 'Digital Product Manager', 'Risk Management Specialist',
    'Chief Operating Officer', 'Customer Experience Strategist', 'Financial Technology Consultant',
    'Emerging Technology Specialist', 'Corporate Governance Advisor', 'IT Governance Specialist',
    'Talent Acquisition Manager', 'RegTech Implementation Specialist', 'Cloud Security Engineer',
    'Digital Ecosystem Architect', 'Smart Infrastructure Engineer', 'Innovation Lab Director',
    'Cyber Threat Analyst', 'Strategic Workforce Planner', 'Business Process Automation Engineer',
    'AI Research Scientist', 'Data Governance Analyst', 'Digital Identity Architect',
    'Chief Innovation Officer', 'Operational Risk Consultant', 'Global Expansion Strategist',
    'Quantum Computing Researcher', 'Biometric Security Engineer', 'High-Performance Computing Specialist'
]

# Profesional dan kompleks QUESTION_TEMPLATES
QUESTION_TEMPLATES = [
    "How can {keyword1} and {keyword2} be leveraged to drive {topic} within the role of a {job_title}?",
    "What are the potential challenges a {job_title} might face when integrating {keyword1} and {keyword2} into {topic}, and how can they be mitigated?",
    "In what ways can {keyword1} and {keyword2} transform {topic} for a {job_title}, and what are the strategic implications?",
    "How can the adoption of {keyword1} and {keyword2} enhance {topic} in the context of {job_title}'s responsibilities?",
    "What are the best practices for a {job_title} to implement {keyword1} and {keyword2} to optimize {topic}?",
    "How do {keyword1} and {keyword2} contribute to the overarching goals of {topic} in the strategic role of a {job_title}?",
    "What strategies should a {job_title} employ to successfully integrate {keyword1} and {keyword2} into {topic}, and what outcomes can be expected?",
    "How can {keyword1} and {keyword2} be utilized by a {job_title} to address key challenges in {topic} and achieve long-term objectives?"
]

# Profesional dan kompleks ANSWER_TEMPLATES
ANSWER_TEMPLATES = [
    "A {job_title} can effectively leverage {keyword1} and {keyword2} to address {issue} within {topic}. By adopting {strategy}, they can achieve {benefit}, resulting in {positive_outcome}. This approach not only enhances {aspect}, but also aligns with the organization's overall {overall_goal}.",
    "In the realm of {topic}, {keyword1} and {keyword2} are instrumental for a {job_title} in overcoming {problem}. Implementing {solution} as part of the broader {strategy} enables the achievement of {positive_outcome}, paving the way for {overall_goal}.",
    "The integration of {keyword1} and {keyword2} in {topic} by a {job_title} is crucial for driving {benefit}. Through {solution}, they can navigate {issue}, ultimately leading to {overall_goal}. This approach ensures that {aspect} is consistently improved.",
    "For a {job_title}, {keyword1} and {keyword2} offer significant advantages in enhancing {topic}. Addressing {problem} through {strategy} and focusing on {solution}, they can achieve {positive_outcome}, contributing to {overall_goal}.",
    "Utilizing {keyword1} and {keyword2} within {topic} allows a {job_title} to overcome {issue} effectively. The strategy involves {strategy}, which leads to {positive_outcome}, thereby supporting the organization's {overall_goal}.",
    "In the context of {topic}, a {job_title} can employ {keyword1} and {keyword2} to solve {problem}. The adoption of {solution} as part of a comprehensive {strategy} results in {positive_outcome}, aligning with the company's {overall_goal}.",
    "To address the challenges of {topic}, a {job_title} should leverage {keyword1} and {keyword2}. By focusing on {strategy}, they can achieve {benefit}, leading to {positive_outcome} and reinforcing the organization's {overall_goal}.",
    "{keyword1} and {keyword2} are critical for a {job_title} in optimizing {topic}. Through the implementation of {solution} and the adoption of {strategy}, they can overcome {problem}, resulting in {positive_outcome} and contributing to {overall_goal}."
]

# Function to generate a single entry
def generate_entry(index):
    keyword1, keyword2 = random.sample(KEYWORDS, 2)
    topic = random.choice(TOPICS)
    job_title = random.choice(JOB_TITLES)
    benefit = random.choice(['increased productivity', 'enhanced user satisfaction', 'cost efficiency'])
    issue = random.choice(['technical challenges', 'resource constraints'])
    solution = random.choice(['innovative solutions', 'best practices'])
    positive_outcome = random.choice(['successful outcomes', 'optimized outcomes'])
    aspect = random.choice(['team efficiency', 'project outcomes'])
    overall_goal = random.choice(['strategic growth', 'operational success'])
    strategy = random.choice(['adopting new technologies', 'improving processes'])
    problem = random.choice(['inefficiencies', 'bottlenecks'])

    question = random.choice(QUESTION_TEMPLATES).format(
        keyword1=keyword1,
        keyword2=keyword2,
        topic=topic,
        job_title=job_title
    )

    answer = random.choice(ANSWER_TEMPLATES).format(
        keyword1=keyword1,
        keyword2=keyword2,
        topic=topic,
        job_title=job_title,
        solution=solution,
        benefit=benefit,
        positive_outcome=positive_outcome,
        issue=issue,
        aspect=aspect,
        overall_goal=overall_goal,
        strategy=strategy,
        problem=problem
    )

    timestamp = (datetime(2024, 1, 1) + timedelta(days=index)).isoformat()

    return {
        "content": f"Question: {question} Answer: {answer}",
        "meta": {
            "timestamp": timestamp
        }
    }

# Function to generate multiple entries
def generate_entries(num_entries):
    return [generate_entry(i) for i in range(num_entries)]

# Main function to execute the generation
def main():
    num_entries = 10000  # Adjust the number of entries as needed
    entries = generate_entries(num_entries)
    with open('sultan.json', 'w') as file:
        json.dump(entries, file, indent=4)

if __name__ == "__main__":
    main()
