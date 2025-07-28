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

1. Install [Rye](https://rye.astral.sh/).

```shell
curl -sSL https://rye-up.com/get | RYE_INSTALL_OPTION="--yes" bash

rye config --set-bool behavior.use-uv=true

source "${HOME}/.rye/env"
```

2. Clone the project.

```shell
git clone https://github.com/adonis0147/pyshell

cd pyshell
```

3. Set the environment up.

```shell
rye sync
```

4. Use the virtual environment.

```shell
source .venv/bin/activate

pyshell
```
