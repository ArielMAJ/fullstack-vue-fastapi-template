# front-back-integration-template

## Table of Contents

- [About](#about)
- [Requirements to run the project](#requirements-to-run-the-project)
- [How to run the project](#how-to-run-the-project)
- [Compatibility](#compatibility)
- [Contributing](#contributing)
- [Author](#author)
- [License](#license)

## About

A head start template for fullstack projects with integrated Vue front-end (bun/NodeJS) and FastAPI back-end (Python).

## Requirements to run the project

- `make` 4.3;
  - `sudo apt install build-essential` on Ubuntu (build-essential might be needed for `pyenv`); or
  - `sudo apt install make` on Ubuntu; or
  - `brew install make` on macOS; or
  - `choco install make` on Windows;
- Python 3.9.18;
  - Current Vercel supported version (but, if you're using more recent versions, it should probably work locally);
  - I personally recommend using [pyenv](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation) for Python version management;
- Node.js v20.11.0;
  - I personally recommend using [nvm](https://github.com/nvm-sh/nvm?tab=readme-ov-file#installing-and-updating) for Node.js version management;
- Bun 1.0.26: install [here](https://bun.sh/);

## How to run the project

1. Clone the repository with:
   1. `git clone git@github.com:ArielMAJ/front-back-integration-template.git` (needs SSH key setup); or
   2. `git clone https://github.com/ArielMAJ/front-back-integration-template.git` (no need for SSH key setup);
   3. Download it if you don't have git and doesn't want to install it;
2. Change directory: `cd front-back-integration-template`;
3. Create `.env`'s from the `.env.example` files (you can just copy them as they are):
   ```bash
   make default-dot-envs
   ```
4. Install the dependencies:
   ```bash
   make install
   ```
5. Run the backend in a terminal:
   ```bash
   make run-api
   ```
6. Run the frontend in another terminal:
   ```bash
   make run-vue
   ```
7. Access the frontend at `http://localhost:8080/`.
8. Access the backend docs at `http://localhost:3000/docs` or `http://localhost:3000/redoc`.

## Compatibility

- Linux: works and is the primary development platform;
- WSL: should work;
- Windows: should work. The inital development stages were in Windows, but later migrated to Linux;
- MacOS: not tested.

## Contributing

Any and everyone is welcome to test this tool locally and leave feedback in the discussions/issues page. If you have some free time and are interested in it, please do. I would love to hear your thoughts and suggestions.

If you want to contribute to the project in any way, feel free to start issues, discussions and open pull requests. Check the [CONTRIBUTING](CONTRIBUTING.md) file for more information.

## Author

- [@ArielMAJ](https://ariel.artadevs.tech/): ariel.maj@hotmail.com

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
