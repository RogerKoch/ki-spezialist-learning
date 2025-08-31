"""
Setup-Konfiguration für das KI-Spezialist Learning Projekt
"""

from setuptools import setup, find_packages
import os

# Version aus __init__.py lesen
def get_version():
    version_file = os.path.join('shared', '__init__.py')
    with open(version_file) as f:
        for line in f:
            if line.startswith('__version__'):
                return line.split('=')[1].strip().strip('"').strip("'")
    return '1.0.0'

# Long description aus README lesen
def get_long_description():
    with open('README.md', 'r', encoding='utf-8') as f:
        return f.read()

# Requirements aus Datei lesen
def get_requirements():
    with open('requirements.txt', 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name='ki-spezialist-learning',
    version=get_version(),
    author='Roger Koch',
    author_email='koch23roger@gmail.com',
    description='Comprehensive hands-on learning project for AI APIs',
    long_description=get_long_description(),
    long_description_content_type='text/markdown',

    url='https://github.com/RogerKoch/ki-spezialist-learning',
    project_urls={
        'Bug Reports': 'https://github.com/RogerKoch/ki-spezialist-learning/issues',
        'Source': 'https://github.com/RogerKoch/ki-spezialist-learning',
        'Documentation': 'https://github.com/RogerKoch/ki-spezialist-learning/blob/main/docs/',
    },
    packages=find_packages(exclude=['tests*', 'experiments*', 'playground*']),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Education',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.13',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.13',
    install_requires=get_requirements(),
    extras_require={
        'dev': [
            'pytest>=7.4.0',
            'pytest-cov>=4.1.0',
            'black>=23.9.0',
            'flake8>=6.0.0',
            'mypy>=1.6.0',
            'pre-commit>=3.4.0',
        ],
        'docs': [
            'sphinx>=7.2.0',
            'sphinx-rtd-theme>=1.3.0',
            'mkdocs>=1.5.0',
        ],
        'jupyter': [
            'jupyter>=1.0.0',
            'ipykernel>=6.25.0',
            'matplotlib>=3.7.0',
            'seaborn>=0.12.0',
        ],
        'web': [
            'fastapi>=0.103.0',
            'uvicorn>=0.23.0',
            'jinja2>=3.1.0',
            'aiofiles>=23.2.0',
        ]
    },
    entry_points={
        'console_scripts': [
            'ki-setup=scripts.setup_environment:main',
            'ki-test=scripts.run_all_tests:main',
            'ki-report=scripts.generate_progress_report:main',
        ],
    },
    include_package_data=True,
    package_data={
        'shared': ['templates/*.json', 'configs/*.yaml'],
        'data': ['templates/*', 'sample_data/*'],
    },
    zip_safe=False,
    keywords=[
        'artificial-intelligence',
        'api-integration',
        'machine-learning',
        'openai',
        'claude',
        'education',
        'learning',
        'python',
    ],
)