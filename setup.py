from setuptools import setup , setuptools 

# reading long description from file 
with open("README.md", "r") as fh:
    long_description = fh.read()

# specify requirements of your package here 
REQUIREMENTS = ['requests'] 

# some more details 
CLASSIFIERS = [ 
	'Development Status :: 4 - Beta', 
	'Intended Audience :: Developers', 
	'Topic :: Filesystem', 
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
	version='1.0.0', 
	description='extract dir given its root path', 
    long_description_content_type="text/markdown",
	long_description=long_description, 
	url='https://github.com//dirman', 
	author='sonu sharma', 
	author_email='meetsonusharma07@gmail.com', 
	license='MIT', 
	packages=setuptools.find_packages(), 
	classifiers=CLASSIFIERS, 
	install_requires=REQUIREMENTS, 
	keywords='os path dir'
	) 
