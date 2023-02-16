# Example Python project

![Tests status](https://github.com/AndreFCruz/python-proj-boilerplate/actions/workflows/python-package.yml/badge.svg)
![PyPI publishing status](https://github.com/AndreFCruz/python-proj-boilerplate/actions/workflows/python-publish.yml/badge.svg)
![PyPI version](https://badgen.net/pypi/v/my-project-andre)
![OSI license](https://badgen.net/pypi/license/my-project-andre)
<!-- ![Python compatibility](https://badgen.net/pypi/python/my-project-andre) -->

> Generate cool badges with [badgen](https://badgen.net), [shields](https://shields.io), or the 
> standard [GitHub workflow badges](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/adding-a-workflow-status-badge).

This repo contains boilerplate configs for python projects, including:
- vanilla `setup.py` to bundle and install a python package;
- publishing package to PyPI on CI;
- running tests on CI;
- general folder structure.


## Publishing to PyPI locally

Python reference [here](https://packaging.python.org/en/latest/tutorials/packaging-projects/), and twine reference [here](https://twine.readthedocs.io/en/stable/).

0. Install necessary dependencies.
```
pip3 install setuptools twine build
```

1. Generate distribution archives (bundle package).
```
python3 -m build
```

2. Upload the distribution archives to [test-pypi](https://test.pypi.org) as follows.
```
python3 -m twine upload --repository testpypi dist/*
```

3. If everything looks OK, upload the distribution archives to the official PyPI repo.
```
python3 -m twine upload dist/*
```

> **Note**
> When prompted for credentials use `__token__` for the username and your [generated 
api token](https://pypi.org/help/#apitoken) as the password.


## Installing

After publishing your project, you can now install it with pip as follows (optionally, add the test-pypi url):

```
pip3 install my-project-andre [--index-url https://test.pypi.org/simple/]
```

Substitute `my-project-andre` with whatever unique project name you chose in [setup.py](https://github.com/AndreFCruz/python-proj-boilerplate/blob/main/setup.py#L62).
