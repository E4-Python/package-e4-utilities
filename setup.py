from setuptools import setup
import e4_utilities

package_data = e4_utilities.load_json('package.json')

setup(
    name=package_data['name'],
    version=package_data['version'],
    description=package_data['description'],
    url=package_data['url'],
    author=package_data['author'],
    author_email=package_data['author_email'],
    packages=package_data['packages'],
    install_requires=package_data['install_requires']
)