from setuptools import setup
import json

data = json.load(open('package.json', 'r', encoding='utf-8'))

setup(
    name=data['name'],
    version=data['version'],
    description=data['description'],
    url=data['url'],
    author=data['author'],
    author_email=data['author_email'],
    packages=data['packages'],
    install_requires=data['install_requires']
)