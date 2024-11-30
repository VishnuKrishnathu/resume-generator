from textwrap import dedent
from crewai import Task


class ResumeEnhancerTasks():
    def resume_enhance_task(self, agent, professional_experience, user_skills: list[str], job_description):
        return Task(
            description=dedent(f"""\
            Analyse users professional experience and prepare 4 bullet points
            considering the Job description. The enhanced professional experience
            should not include any extra skillset other than the skills from the users resume.
            The enhanced professional experience should have majority of the keywords from the job description.
            The output should be in latex code with only the \item argument, no introduction only code. No documentation in the output.

            Professional Experience: {professional_experience}
            User's resume skillsets: {", ".join(user_skills)}
            Job description: {job_description}
            """),
            expected_output=dedent(f"""\
            A detailed report summarizing key findings about each participant
            and company, highlighting information that could be relevant for the meeting."""),
            agent=agent,
            async_execution=True
        )
