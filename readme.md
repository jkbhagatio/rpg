# RPG

RPG is a 2d role-playing game. Currently in development. Core developer goals for this project are to: 

1. Explore game dev in Python (e.g. using Pyglet and PyGame)
2. Explore UI (e.g. using PyQt5) and low-level graphics (e.g. using OpenGL, PyOpenGL) libraries
3. Integrate python with low-level compiled code (e.g. C) 
4. Use best practices in Python packaging (e.g. adhering to PyPA, using setuptools)
5. Use best development practices in CI/CD solutions and documentation (e.g. Flake8, Black, PyTest, Tox, Travis CI, Github Actions, ReadTheDocs)
6. Use best practices in OOP Design Patterns.

## Resources

1. Python Game Dev

	- [coders legacy pygame Simple RPG tut](https://coderslegacy.com/python/pygame-rpg-game-tutorial/)
	- [wiki.python game programming in python](https://wiki.python.org/moin/GameProgramming)
	- [wiki.python game libraries](https://wiki.python.org/moin/PythonGameLibraries)
	- [wiki.python python games](https://wiki.python.org/moin/PythonGames)

2. UI & Graphics

	- [wiki.python pyqt5 tuts](https://wiki.python.org/moin/PyQt/Tutorials)
	- [pyqt5 docs](https://www.riverbankcomputing.com/static/Docs/PyQt5/)
	- [openGL docs](https://docs.gl/)

3. Python Bindings

	- [Cython docs](https://cython.readthedocs.io/en/latest/)
	- [RealPython on bindings](https://realpython.com/python-bindings-overview/)

4. Python Packaging

	- [A short, practical guide to using `setuptools`](https://godatadriven.com/blog/a-practical-guide-to-using-setup-py/)
	- [Python Packing Authority (PyPA) docs](https://packaging.python.org/)
	- [`setuptools` docs](https://setuptools.readthedocs.io/en/latest/userguide/index.html)

5. CI/CD and Documentation
	- [Pep8](https://www.python.org/dev/peps/pep-0008/)	
	- [Flake8 docs](https://flake8.pycqa.org/en/latest/)
	- [Black docks](https://github.com/psf/black)
	- [PyTest docs](https://pytest.org/)
	- [Tox docs](https://tox.readthedocs.io/en/latest/)
	- [ReadTheDocs docs](https://docs.readthedocs.io/en/rel/getting_started.html)
	- [Travis CI docs](https://docs.travis-ci.com/user/tutorial/)
	- [Github Action docs](https://docs.github.com/en/actions/learn-github-actions/introduction-to-github-actions)


6. OOP
	- [GoF's Design Patterns](https://en.wikipedia.org/wiki/Design_Patterns)
	- Design Patterns:
		- (Creational) Abstract Factory*; Factory Method*; Prototype
		- (Structural) Composite*; Decorator*; Facade; Flyweight
		- (Behavioral) State*; Chain of Responsibility; Command;  Observer; Visitor; Mediator; Visitor; Strategy; Interpreter

	- Classes:
		- Class constructor methods & dependency injection
		- Designing subclass constructors from superclass constructors
		- Composition (interface) inheritance vs. implementation inheritance
		- Multiple inheritance & mix-ins
		- Enumeration classes
		- Importing classes
		- Class destructor methods
		- Types:
			- Abstract
			- AllowedSubclasses
			- ConstructOnLoad
			- Inferior classes (for overloaded graphics functions)
			- Sealed

	- Fields:
		- Constant properties
		- Dynamic (Instance) Properties
		- Static Data
		- Property get/set methods
		- Property events/listeners ('event.proplistener')
		- Types:
			- AbortSet
			- Abstract
			- Access
			- GetAccess
			- SetAccess
			- Constant
			- Dependent
			- GetObservable
			- SetObservable
			- Hidden
			- NonCopyable
			- Transient

	- Events (& Listeners):
		- Trigger events for listeners both tied and untethered to event source ('notify')
		- Determine if any listeners currently exist for event ('event.haslistener')
		- Deactivate and reactivate listeners
		- Pass extra event data to a listener callback ('notify(obj, 'evt', evtdata)) by subclassing 'event.EventData' and adding a new property to that subclass
		- Execute listeners in a specific order
		- Have a listener recursively trigger the same event (via the 'Recursive' property of a listener object) - (but make sure the listener callback changes the object data in some way such that infinite recursion does not occur)
		- Save and restore a listener
		- Types:
			- Hidden
			- ListenAccess
			- NotifyAccess

	- Extras:
		- Save and load process for objects
		- Property initialization order dependency
		- Class introspection and metadata
		- Class arrays and class hierarchical heterogeneous arrays

## Contents

- `docs\`: documentation and examples and development guidelines
- `rpg\`: game source code
- `tests\`: unit and integration tests
- `changelog.md`: an up-to-date changelog describing latest features and their commits
- `env.yml`: dependencies file for conda
- `pyproject.toml`: specifies build tools
- `requirements.txt`: dependencies file for pip and setuptools
- `setup.py`: configures and packages the source code
- `tox.ini`: tox file for running tests on package installs across environments


## Notes for Developers

- Clone this repo and install package in editable mode:
- Using semantic versioning
- Contributing:
	- see [project organization and style guidelines](github.com/jkbhagatio/blob/master/docs/project_org_and_style_guidelines.md)
	- All work should be done on feature branches. All work should be flaked and include tests. PRs from feature branches should be sent to `dev`. On a new release, `dev` is merged into `main`. CI runs on `dev` and `main`.
	- On any merges into `dev`, the following should be updated (as necessary):	
		1. `readme.md`
		2. `docs\`
		3. root directory config files
		4. `changelog.md`
	- Github Issues and Projects should be used to track and organize development.

## Misc
