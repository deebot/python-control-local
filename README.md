# python-controls-local

Python package created to verify the Backstage project template

Created with the engineering **modular Python** starter, version **1.2.0**.
Python import name: `python_controls_local`. Replace the greeting example
with your project code. Selected capabilities:


- `ruff-lint`

- `ruff-format`

- `pytest`

- `packaging`

- `sphinx`



Owner **group:default/engineering**, lifecycle **experimental**, catalog type
**library**. These are catalog labels, not deployment approvals.

## OpenProject


**No** was selected: no OpenProject project was created or linked. The Backstage
Work items tab remains unmapped until this project is deliberately onboarded.


## Local development

Use Python 3.12 or newer. Create an isolated environment and install the selected
development tools:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python -m compileall -q src

ruff check src tests


ruff format --check src tests


PYTHONPATH=src python -m pytest


python -m build --no-isolation


PYTHONPATH=src sphinx-build -W --keep-going -b html docs docs/_build/html

```


Run `ruff format src tests` to fix formatting locally; CI checks without changing files.



## CI behavior


**CI is disabled.** No workflows were generated and Forgejo Actions is disabled.
Pushes and PRs do not run automated jobs. All selected local commands above remain available.
Enabling CI later requires reviewed workflows AND enabling Actions in Forgejo.


## PR traceability


Disabled: no traceability workflow or OpenProject CI token was installed.


## GitHub mirror


Requested destination: [GitHub](https://github.com/deebot/python-controls-local). **Initially awaiting setup.**
Follow [.engineering/github-mirror.md](.engineering/github-mirror.md): add the public deploy key with write access, then run the activation command.
No automatic pushes are enabled until the destination has been checked and the first sync succeeds.
Forgejo remains the primary source. The Git mirror does not copy tickets, accounts, CI artifacts or application settings.


## Maintaining this project

`.engineering-template.json` records the template source commit and initial
capabilities. These files now belong to this project. Updating the template does
not rewrite this repository. Add or change capabilities through reviewed Git
changes; there is no automatic add-capability or upgrade operation yet.

## Links

- [Repository](https://192.168.10.20/deep/python-controls-local)

- [Backstage project](https://192.168.10.20:10443/catalog/default/component/python-controls-local)
- [Template source](https://192.168.10.20/deep/project-templates)
- [Template operations guide](https://192.168.10.20/deep/engineering-infra/src/branch/main/docs/project-template.md)
