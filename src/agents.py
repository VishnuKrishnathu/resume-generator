from textwrap import dedent
from crewai import Agent
# from tools import ExaSearchToolSet


class ResumeEnhancerAgents():

    def resume_enhance_agent(self):
        return Agent(
            role="Resume Enhancer",
            goal="Analyse user's resume and job description to include keywords from the job description",
            tools=[],
            backstory=dedent(f"""As a resume enhancer, your mission is to analyse the job description
                and users resume to embed keywords from the job description into the professional experience.
                The enhanced job description will help the user to get through the company's Application Tracking System"""),
            verbose=True
        )

    # def student_agent(self):
    #     return Agent(
    #         role="Interviewee",
    #         goal="According to the description of the company",
    #         tools=[],
    #         backstory=dedent(f"""As a resume enhancer, your mission is to analyse the job description
    #             and users resume to embed keywords from the job description into the professional experience.
    #             The enhanced job description will help the user to get through the company's Application Tracking System"""),
    #         verbose=True
    #     )