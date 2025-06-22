# 🎯 GitHub LabelSync

> A powerful but simple CLI tool to manage and synchronize your GitHub labels using a TOML file and the GitHub CLI.

[![Python](https://img.shields.io/badge/Python-3.11+-blue)](https://www.python.org/downloads/release/python-3110/) 
[![GitHub CLI](https://img.shields.io/badge/gh--cli-required-red)](https://cli.github.com/) 
[![Loguru](https://img.shields.io/badge/logging-loguru-green)](https://github.com/Delgan/loguru)

---

## 🚀 Features

- 🔄 Full sync of GitHub labels from a simple `TOML` file
- 🪪 Dry-run mode for previewing what would happen
- 🗑️ Optional deletion of existing labels before creation
- 📦 Automatic backup of current labels before modification
- 🔥 Interactive confirmation prompt before applying changes
- 🧣 Logging to file (`labels_sync.log`) and colorful terminal output
- ⚙️ Easily configurable and scriptable via command-line interface

---

## 📦 Installation 
> ℹ️ **Not required** – You can also run it directly as a Python script. See [Usage](#-usage) below.

To use the `labelsync-cli` command, you must first install this project either via `pip` or with `conda`. Below are both options.

### 🐍 pip (development mode)
```bash
git clone https://github.com/your-user/labelsync.git
cd labelsync
pip install -e .
```

### 🐍 Conda (new environment)
```bash
git clone https://github.com/your-user/labelsync.git
cd labelsync
conda env create -f environment.yml
conda activate labelsync
pip install -e .  # registers the CLI command
```

### 🧰 Conda (existing environment)
```bash
conda install conda-forge::loguru
conda install conda-forge::tomli-w
pip install -e .  # only if not already installed
```

> ⚠️ Requires Python 3.11 or newer (because of built-in `tomllib` support)

Also make sure GitHub CLI (`gh`) is installed and authenticated:
```bash
gh auth login
```

---

## 🧪 Usage

You can use the tool in two ways:

### ✅ 1. As a CLI command
```bash
labelsync-cli --repo your-user/your-repo
```

### ✅ 2. As a script (no installation)
```bash
python -m labelsync.cli --repo owner/repo --file examples/labels.toml
```

Both versions support the same arguments:

### ⚖️ Options

| Flag             | Description                                                       |
|------------------|-------------------------------------------------------------------|
| `--repo`         | **(required)** GitHub repository in `owner/repo` format           |
| `--file`         | Path to TOML label file (default: `labels.toml`)                  |
| `--skip-delete`  | Keep existing labels, only add/update new ones                    |
| `--dry-run`      | Simulate changes without touching GitHub                          |
| `--log-level`    | Console log level: `DEBUG`, `INFO`, `WARNING`, or `ERROR`         |

### 🧾 Full Example

```bash
labelsync-cli \
  --repo jhajduga/labelsync \
  --file examples/labels.toml \
  --skip-delete \
  --log-level DEBUG
```

---

## 📄 Label file format (TOML)

The `labels.toml` file defines what labels should exist in the repo.

```toml
[[label]]
name = "bug"
description = "Something isn't working as expected."
color = "d73a4a"

[[label]]
name = "feature"
description = "New functionality added to the label sync tool."
color = "0e8a16"
```

A full example is included here:
```bash
examples/labels.toml
```

---

## 📂 Project structure

```
labelsync/
├── labelsync/           # Main logic and logger setup
│   ├── __init__.py
│   ├── sync.py
│   ├── logger_setup.py
│   └── cli.py
│
├── examples/            # Example TOML label set
│   └── labels.toml
│
├── tests/               # Unit tests
│   └── test_parsing.py
│
├── README.md            # This file
├── CONTRIBUTING.md      # Contribution guidelines
├── requirements.txt     # pip-based dependencies
├── environment.yml      # conda environment
└── pyproject.toml       # Project metadata & CLI definition
```

---

## 🤝 Contributing

Pull requests are welcome! See [`CONTRIBUTING.md`](CONTRIBUTING.md) for setup, coding conventions, and submission instructions.

---

## 🔧 For Developers

To run tests:
```bash
pytest tests/
```

To check the code manually:
```bash
flake8 labelsync/
```

<!-- ---

## ⚙️ Planned GitHub Actions

```yaml
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: conda-incubator/setup-miniconda@v2
        with:
          activate-environment: labelsync
          environment-file: environment.yml
      - run: pip install -e .
      - run: pytest tests/
``` -->

---

## 🔮 Coming soon

- `labelsync export` — export existing labels to TOML
- `labelsync validate` — validate TOML structure before applying
- PyPI distribution and versioning
- Conda-forge packaging support
- Better tests

---

## 📜 License

MIT License. Do what you want — just don’t blame us if your labels explode. 😅
