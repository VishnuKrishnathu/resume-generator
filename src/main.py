import re
from crewai import Crew
from tasks import ResumeEnhancerTasks
from agents import ResumeEnhancerAgents
from textwrap import dedent
from read_latex import get_latext_content
import subprocess
from os import path, system


def main():
    print("## Welcome to the Resume Enhancer")
    print("------------------------")
    # meeting_participants = input(
    #     "What are the emails for the participants (other than you) in the meeting?\n"
    # )
    # meeting_context = input("What is the context of the meeting?\n")
    # meeting_objective = input("What is your objective for this meeting?\n")

    tasks = ResumeEnhancerTasks()
    agents = ResumeEnhancerAgents()

    user_skills = [
        "AWS",
        "AWS CodeBuild",
        "AWS Lambda",
        "Elasticbeanstalk",
        "ExpressJS",
        "ReactJS",
        "NextJS",
        "NextJS",
        "ECS",
        "AWS Fargate",
        "API Gateway",
        "Typescript",
        "Javascript",
        "Google Cloud Run",
        "Google Cloud Build",
        "NodeJS",
        "Crew AI",
        "Langchain"
    ]

    # create agents
    resume_enhance_agent = agents.resume_enhance_agent()

    professional_experience = dedent(f"""\
I have created CI/CD pipelines using Github Actions,
Google cloud build, AWS CodeBuild. I have create a code
compiler which can handle upto 3k concurrent request. I have
implemented designs made by UI/UX designers.
I have created backend APIS in NodeJS, Express JS, Nest JS, Typescript as MongoDB the primary database.
I have created frontend applications using ReactJS, NextJS, tailwindcss.
I have managed a team of 5 developers to meet the deadlines.
I have created cron job in python which does a semantic similarity between paragraphs.
I have created a compiler than can compiler programming languages in python.
Had discussions with the operations team and helped them in automated the operations workflow using tech.
I have created AI agents using crew ai with OpenAI APIs and RAG approach which will generate the content used for test evaluations.
    """)

    # create tasks
    research_task = tasks.resume_enhance_task(
        resume_enhance_agent,
        job_description=dedent("""\
            What youll get to do
Develop robust, scalable, and secure full-stack applications using modern frameworks and technologies.
Collaborate with product managers, designers, and other engineers to create customer-focused solutions.
Build and maintain front-end components, APIs, and backend services that power GoDaddy s platform.
Write clean, maintainable, and testable code while following best practices in software development.
Optimize applications for performance, usability, and scalability.
Debug and resolve technical issues to ensure smooth operation of GoDaddy s products.
Contribute to architectural decisions and help shape the technical direction of our platforms.
Your experience should include...
Proven experience developing full-stack applications and working with both frontend and backend technologies.
Experience with JavaScript, React, Angular, HTML, CSS, Node.js, Java, Python, Ruby on Rails
Experience with Node.js, Python, Java.
Knowledge of building RESTful APIs.
Cloud Expertise: Experience deploying applications to cloud platforms like AWS.
Knowledge/Experience with CI/CD pipelines and DevOps practices.
Weve got your back... We offer a range of total rewards that may include paid time off, retirement savings (e.g., 401k, pension schemes), bonus/incentive eligibility, equity grants, participation in our employee stock purchase plan, competitive health benefits, and other family-friendly benefits including parental leave. GoDaddy s benefits vary based on individual role and location and can be reviewed in more detail during the interview process.
                                """),
        professional_experience=professional_experience,
        user_skills=user_skills)

    crew = Crew(
        agents=[resume_enhance_agent],
        tasks=[research_task],
    )

    result = crew.kickoff()

    return result.raw


def find_available_filename(base_name, extension=".tex"):
    # Check if base file exists
    filename = f"{base_name}{extension}"
    if not path.exists(filename):
        return filename

    # Iterate through numbers until an available filename is found
    counter = 1
    while True:
        filename = f"{base_name}_{counter}{extension}"
        if not path.exists(filename):
            return filename
        counter += 1


if __name__ == "__main__":
    file_path = find_available_filename("gen_resumes/Vishnu_Krishnathu")
    new_file = open(file_path, "w")

    proffessional_experience_enhanced = main().replace('\\', '\\\\')

    content = get_latext_content(proffessional_experience_enhanced)
    new_file.write(content)

    new_file.close()

    out_file_path = find_available_filename(
        "resume_pdfs/Vishnu_Krishnathu", ".pdf")

    system(
        f"pdflatex -halt-on-error -output-directory=resume_pdfs {file_path}")
