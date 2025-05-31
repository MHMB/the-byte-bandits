# The Byte Bandits

## installation

- install [pyenv](https://github.com/pyenv/pyenv)
- install [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)
- install [poetry](https://github.com/sdispater/poetry)
- install python 3.12.2 via pyenv

```bash
pyenv install 3.12.2
```

- create virtualenv 

```bash
pyenv virtualenv 3.12.2 the-byte-bandits_env_3.12.2
pyenv activate the-byte-bandits_env_3.12.2
```

- set pyenv local version in the root folder

```bash
pyenv local the-byte-bandits_env_3.12.2
```

- install dependencies

```bash
poetry install --no-dev
```
