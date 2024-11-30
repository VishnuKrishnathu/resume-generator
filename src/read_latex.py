import os
import re


def get_latext_content(professional_experience: str):
    resume_path = os.path.abspath("resume_latex/resume.tex")
    resume_file = open(resume_path, "r")
    resume_file_content = resume_file.read()
    professional_experience = "\n" + professional_experience + "\n"

    pattern = r'% id\{proffessional_experience\}(.*?)% endid\{proffessional_experience\}'

    new_text = re.sub(
        pattern,
        f'% id{{proffessional_experience}}{
            professional_experience}% endid{{proffessional_experience}}',
        resume_file_content,
        flags=re.DOTALL
    )

    return new_text
