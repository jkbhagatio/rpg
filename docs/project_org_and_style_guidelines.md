# Project Organization and Style Guidelines

The purpose of this document is to establish project repository organization and style guidelines when writing code. The code examples below are in MATLAB, but the guidelines mentioned here can be followed in any programming language.

[Richard Johnson](https://uk.mathworks.com/matlabcentral/profile/authors/22731-richard-johnson) writes, "Style guidelines are not commandments. Their goal is simply to help programmers write well." Well-written code implies code that is easy to read. Code that is easy to read is typically written in a consistent style, so new code should be as consistent as possible with the rest of the repository.


## Project Organization

Directory Structure:

- readme
- license
- docs/
	- examples/
		- data/ (optional)
- tests/
	- data/ (optional)
- changelog (optional)
- contributing (optional)
- .github/ (optional)
- .gitignore (optional)

(Python)
- <project_name>/
- setup.py (optional)
- setup.cfg (optional)
- manifest.in (optional)
- requirements.txt (optional)
- env.yml (optional)
- .travis.yml (optional)
- .flake8 (optional)
- pyproject.toml (optional)
- makefile (optional)

(C)
- src/
	- <project_name>.c
	- <project_name>.h
- bin/ (C)
- tools/ (optional)
- lib/ (optional)
- log/ (optional)
- include/ (optional)
- makefile (optional)


* Notes:
	- readme (w/ list of contents) in each subfolder


## Code Style Guidelines

A file header should briefly describe the contents within a few sentences.

Sections shuold be enclosed in comments that begin and end with `<s` and `/s>`, respectively. Nested subsections can be used, adding an `s` for each nesting; e.g., a subsubsection would begin and end with `<sss` and `/sss>`, respectively.

A function's header documentation (aka a docstring) is written as follows:

* Functions have the following sections in the given order:
	- One-line summary description, typically as a verb phrase
	- Long description (optional)
	- Inputs (optional)
	- Outputs (optional)
	- Examples (optional if included in a separate file)
	- Warnings/Exceptions (optional)
	- Additional notes (optional)
	- See also (optional)
	- Todos (optional)
* Classes have the following sections in the given order:
	- One-line summary description, typically as a noun phrase
	- Long description (optional)
	- Examples (optional if included in a separate file)
	- Warnings/Exceptions (optional)
	- Additional notes (optional)
	- See also (optional)
	- Todos (optional)

A file's body documentation should adhere to the following:

* For classes, each method, field, and event should be documented. Additional explanations should be given for methods, fields, and events that have non-default parameters. e.g.
```
properties (Dependent)
  % `Dependent` because...
  property1
end

methods (Access=protected)
  % `Access=protected` because...
  method1
end

events (ListenAccess=private)
  % `ListenAccess=private` because...
  event1
end
```
* Whitespace conventions:
	- A tab/indent is set at four spaces.
	- Whitespace between lines is used sparingly, but can be used to improve readability between blocks of code.
	- Each line contains no more than 79 characters. Whitespace should be used to align statements that span multiple lines via a hanging indent or single indent e.g.
	```
	stash = ['stash push -m "stash working changes before '...
             'scheduled git update"'];
	```
* Block quotes should be written as full sentences above the corresponding code. e.g.
  ```
  % Check that the inputs are properly defined.
  if len(varargin) ~= 1 && len(varargin) ~= 2 ...
  ```
* Inline quotes should be written as a short phrase that starts two spaces after the corresponding code. e.g.
  ```
  if len(varargin) == 1  % return input
  ```
* Variables should be documented where they are declared. e.g.
  ```
  % The Rigbox root directory
  root = getOr(dat.paths, 'rigbox');
  ```
* Code referenced in comments is surrounded by back ticks for readability e.g.
  ```
  % New signal carrying `a` with its rows flipped in the up-down direction
  b = flipud(a);
  ```
* In general, clarity > brevity. Don't be afraid to spread things out over a number of lines and to add block and in-line comments. Long variable names are often much clearer (e.g. `input_sensor_ct` instead of `inpN`).
* ["Scare quotes"](https://www.chicagomanualofstyle.org/qanda/data/faq/topics/Punctuation/faq0014.html) are generally to be avoided.

Additional conventions:

* Naming conventions:
	- Variable and function names are in lower snake_case (e.g. `exp_ref`, `infer_parameters` with a `_` in between each individual word representation)
	- Classes are in upper Snake_Case (e.g. `Alyx_Panel`)
	- use prefix 'n' for integer values e.g. `n_items`
	- use suffix 'num' for referring to a particular instance e.g. `item_num`
	- use prefix 'i' for iterator variables e.g. `i_file`
	- use suffices that indicates unit measurement when using multiple units e.g. `wheelDeg` and `wheelMm`
	- avoid reusing variable names (i.e. avoid mutation)
	- Same variable names used across files should have the same meanings, and vice versa.
	- When assigning a function's output(s), use the name(s) defined in that function's header.
* Comments are for explaining _what_ a particular chunk of code does when it may be unintuitive, not for explaining exactly _how_ the code does what it does.
* Block comments should read as a narrative.
* Avoid complex conditional expressions; replace with logical variables


