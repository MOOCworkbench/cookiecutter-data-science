Commands
========

The Makefile contains the central entry points for common tasks related to this project.

List of commands
^^^^^^^^^^^^^^^^^^

* `make test_environment` tests your environment and makes sure all the requirements are met (for example if the correct Python version is installed)
* `make create_environment` will create a separate environment for this experiment, which ensures no dependency conflicts arise.
* `make requirements` will install the dependencies of this project with pip.
* `make clean` removes temporary Python files
* `make test` runs all the tests in this experiment
* `make documentation` rebuilds the documentation in this experiment. Run this command if you have added a new *.py file in the src/ folder.
