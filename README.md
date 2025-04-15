videos with manim

- dev dependencies
    - poetry

- install poetry
    - pipx install poetry

- install pipx
    - https://pipx.pypa.io/stable/installation/
        - ubuntu:
            - apt-get install pipx
            - pipx ensurepath
        - arch:
            - pacman -S python-pipx
            - pipx ensurepath

- pyenv
    - pyenv install 3.12.9
    - pyenv virtualenv 3.12.9 manim-vids
    - pyenv activate manim-vids

- poetry install --no-root 
    - to install dependencies of this project but not this project itself
