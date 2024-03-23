from setuptools import find_packages, setup


setup(
name="mcqgenerator",
version="0.0.1",
author="Anuj Pathare",
author_email="anujpathare@gmail.com",
packages=find_packages(),
install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2","pandas"]
)