from setuptools import setup, find_namespace_packages

# reading long description from file
with open("README.md", "r") as fh:
    long_description = fh.read()

# specify requirements of your package here
REQUIREMENTS = []

# some more details
CLASSIFIERS = [
	'Development Status :: 4 - Beta',
	'Intended Audience :: Developers',
	'License :: OSI Approved :: MIT License',
	'Programming Language :: Python',
	'Programming Language :: Python :: 2',
	'Programming Language :: Python :: 2.6',
	'Programming Language :: Python :: 2.7',
	'Programming Language :: Python :: 3',
	'Programming Language :: Python :: 3.3',
	'Programming Language :: Python :: 3.4',
	'Programming Language :: Python :: 3.5',
	]

# calling the setup function
setup(name='dirman',
	version='1.0.1',
	description='extract dir given its root path',
    long_description_content_type="text/markdown",
	long_description=long_description,
	url='https://github.com/sonusharma07/dirman',
	author='sonu sharma',
	author_email='meetsonusharma07@gmail.com',
	license='MIT',
	packages=find_namespace_packages(include=['dirman', 'dirman.*']),
	classifiers=CLASSIFIERS,
	install_requires=REQUIREMENTS,
	keywords='os path dir'
	)
