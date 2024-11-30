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
iamneo is seeking a passionate and talented Full Stack Developer to join our mission of building cutting-edge Generative AI web applications. You'll play a pivotal role in crafting the entire application experience, from the user interface to the powerful engine behind it. This is an opportunity to push boundaries, collaborate with a dynamic team, and leave your mark on the future of ed-tech.
Responsibilities:
Lead the execution and delivery of large, complex projects from beginning to end, independently or collaboratively.
Ensure the timely delivery of all project deliverables.
Act as a key participant in technical discussions within the team, serving as the go-to person for guidance and issue resolution.
Understand and leverage key business and engineering metrics related to performance, quality, and availability, working with the team to continuously enhance them.
Proactively engage in code reviews, architecture discussions, and the establishment of coding standards and best practices.
Mentored junior engineers, providing guidance on coding, code reviews, and overall professional development.
Requirements:
3 to 6 years of extensive experience in end-to-end software product development.
Strong problem-solving skills and tech savvy.
Proficient in Requirement/Design/Code Review and Inspection practices.
Excellent written and oral communication skills.
Solid understanding of enterprise-scale technologies and the development of large-scale services.
Ability to evaluate architectural options and make appropriate recommendations for implementation.
Passion for constantly exploring the latest technologies relevant to our products and platforms.
Ability to engage with potential leads and customers to conduct demonstrations and troubleshoot any technical challenges in the product.
Hands-on experience with Chat GPT, LLAMA, and other AI, understanding of GPU memory management., building custom ETL scripts, using Logstash, Elastic Search
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
