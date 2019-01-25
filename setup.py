import os

from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-mdbook',
    version='0.2.0',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',  # example license
    description='Provide a view for serving and updating books created with mdBook',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/9999years/django-mdbook',
    author='Rebecca Turner',
    author_email='637275@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Development Status :: 4 - Beta',
    ],
    install_requires=[
        'django~=2.0.0',
        'toml~=0.10.0',
        'cached_property~=1.5.0',
    ]
)
