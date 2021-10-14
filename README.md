## Usage

1. Install Python 3
    * **Linux**: `sudo apt install python3 python3-dev python-venv` (or equivalent for your package manager)
    * **macOS**: `brew install python` ([Homebrew](https://brew.sh)) or `xcode-select --install` 
    * **Windows**: `choco install python` ([Chocolatey](https://chocolatey.org/install)) or [Download the installer](https://www.python.org/downloads/windows/)
1. Use `venv` to isolate your environment
    ```bash
    python -m venv env
    source env/bin/activate # Linux and macOS
    .\env\bin\activate # Windows
    ```
1. Install the dependencies
    ```bash
    pip install -r requirements.txt
    ```
1. Run the script
    ```bash
    ./generate.py
    ```