from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='project_master',
    packages=['project_master'],
    version='1.3',
    license='BSD',

    description='This Python script generates a standardized project structure for your Python projects. It creates the necessary folders and files based on your specifications.',

    author='Armen-Jean Andreasian',
    author_email='armen_andreasian@proton.me',

    url='https://github.com/Armen-Jean-Andreasian',
    keywords=['project', 'directory', 'python'],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],


    python_requires='>=3.8',

    long_description=long_description
    ,
    long_description_content_type='text/markdown',
)