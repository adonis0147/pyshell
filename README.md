# PyShell

```
    ____        _____ __         ____
   / __ \__  __/ ___// /_  ___  / / /
  / /_/ / / / /\__ \/ __ \/ _ \/ / /
 / ____/ /_/ /___/ / / / /  __/ / /
/_/    \__, //____/_/ /_/\___/_/_/
      /____/
```

A interactive shell powered by [prompt-toolkit](https://python-prompt-toolkit.readthedocs.io/en/master/).

# Development

1. Install [uv](https://docs.astral.sh/uv/).

```shell
curl -LsSf https://astral.sh/uv/install.sh | bash

export PATH="${HOME}/.local/bin:${PATH}"
```

2. Clone the project.

```shell
git clone https://github.com/adonis0147/pyshell

cd pyshell
```

3. Set the environment up.

```shell
uv sync
```

4. Use the virtual environment.

```shell
source .venv/bin/activate

pyshell
```
