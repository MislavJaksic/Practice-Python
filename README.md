## Practice Python

```
# Note: `.toml` project name and package have to match (practice-python; practice_python)
$: poetry install  # install all dependencies
```

More info about [poetry](https://github.com/MislavJaksic/Knowledge-Repository/tree/master/Technology/Software/BuildTool/poetry).   

### dist

```
$: pip install dist/practice_python-0.0.1-py3-none.any.whl

$: practice-python
```

### docs

```
$: poetry shell
$: cd docs
# Note: review source/conf.py and source/index.rst
$: make html
# Note: see docs in docs/build/apidocs/index.html
```

### practice_python

```
$: poetry run python ./practice_python/runner.py
```

### tests

```
$: poetry run pytest --durations=0
```

```
$: poetry run pytest --cov=practice_python --cov-report=html tests
#: Note: see coverage report in htmlcov/index.html
```

### poetry.lock

Dependencies, Python version and the virtual environment are managed by `Poetry`.

```
$: poetry search Package-Name
$: poetry add Package-Name[==Package-Version]
```

### pyproject.toml

Define project entry point and metadata.  

### setup.cfg

Configure Python libraries.  

### Linters

```
$: poetry run black .
```

### cProfile

```
$: poetry run python ./practice_python/profiler.py
```

### Build and publish

```
$: poetry build

# Note: get the token from your PiPy account
$: poetry config pypi-token.pypi PyPI-Api-Access-Token
```

```
$: poetry publish --build
```

```
https://pypi.org/project/practice-python/
```
