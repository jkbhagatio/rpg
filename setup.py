import setuptools

# set long description to `readme.md`
with open('readme.md', 'r') as f:
	long_description = f.read()
# get dependencies from `requirements.txt`, skipping those from git repos
with open('requirements.txt', 'r') as f:
	reqs = [r.strip() for r in f.readlines() if not (r.startswith('git') or r.startswith('#'))]
	# reqs_a = 
	# reqs_a = <all reqs following '#Data Science' before \n'>

# run setup
setuptools.setup(
	name = 'RPG',
	version = 0.1.0,
	author = 'Jai Bhagat',
	author_email = 'jkbhagatio@gmail.com',
	description = '2d RPG following best practices',
	long_description = long_description,
	long_description_content_type = 'text/markdown',
	url = 'github.com/jkbhagatio/rpg',
	# project_urls = ,
	packages = setuptools.find_packages(include=['rpg', 'rpg.*']),
	# py_modules = ,
	# package_data = ,
	# include_package_data = ,
	# exclude_package_data = ,
	zip_safe = 0,
	# entry_points = ,
	install_requires = reqs,
	python_requires = '>-3.7', 
	# extras_require = {'analysis': reqs_a}, 
	platforms = ['Windows10'],
	classifiers = [
		'Development Status :: 2 - Pre-Alpha',
		'Programming Language :: Python :: 3.7',
		'Topic :: Games/Entertainment :: Role-Playing',
		'Topic :: Software Development :: Build Tools'],
	keywords = ['rpg, game'] )
