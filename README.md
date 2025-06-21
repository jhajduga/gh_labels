

# 🎯 GitHub LabelSync

> A powerful but simple CLI tool to manage and synchronize your GitHub labels using a TOML file and the GitHub CLI.

![Python](https://img.shields.io/badge/Python-3.11+-blue)
![GitHub CLI](https://img.shields.io/badge/gh--cli-required-red)
![Loguru](https://img.shields.io/badge/logging-loguru-green)

---

## 🚀 Features

- 🔄 Full sync of GitHub labels from `TOML` files
- 🔥 Interactive confirmation before changes
- 🧪 Dry-run mode for safe previewing
- 🗑️ Optional deletion of existing labels
- 🧾 Automatic backup of current label state
- 🎨 Colorful console logs and structured logs to file
- 🧠 Global exception handling for better debugging

---

## 📦 Installation

### 🐍 pip

```bash
pip install loguru tomli-w
````

**Python 3.11 or newer is required** due to use of `tomllib`.

### 🐍 Conda

```bash
conda create -n labelsync python=3.11 -y
conda activate labelsync
conda install conda-forge::loguru
conda install conda-forge::tomli-w
```


---

## ⚙️ Requirements

* Python 3.11+
* GitHub CLI (`gh`) installed and authenticated:

```bash
gh auth login
```

---

## 📝 Usage

### 🧪 Basic usage

```bash
python sync_labels.py --repo your-user/your-repo
```

This will:

1. Back up current labels to a timestamped `.toml` file
2. Delete existing labels
3. Create new labels from `labels.toml`

### 🛠 Options

| Flag            | Description                                   |
| --------------- | --------------------------------------------- |
| `--repo`        | (required) GitHub repo in format `owner/repo` |
| `--file`        | Custom TOML file (default: `labels.toml`)     |
| `--skip-delete` | Skip deleting existing labels                 |
| `--dry-run`     | Simulate actions without changing anything    |
| `--log-level`   | Console log level (`DEBUG`, `INFO`, etc.)     |

### 📦 Example

```bash
python sync_labels.py \
  --repo jhajduga/gh_labels \
  --file my_labels.toml \
  --skip-delete \
  --log-level DEBUG
```

---

## 📄 Example label file in TOML Format

This project includes an example TOML file located at:

```bash
examples/labels.toml
````

It contains a predefined set of labels commonly used in this tool's development, including categories like:

* `feature`, `refactor`, `logging`, `cli`
* `backup`, `dry-run`, `config`
* community flags like `good first issue`, `help wanted`

Each label entry includes a `name`, `description`, and `color` field.

```toml
[[label]]
name = "logging"
description = "Changes to logging, logger setup, or output formatting."
color = "008672"
```

You can customize and reuse this file in your own repository syncs.


---

## 🧠 Advanced features

* 📁 `labels_sync.log` contains full stack traces on failure
* 💥 Global exception hook logs unexpected crashes
* 💅 `logger_setup.py` can be reused in your own tools

---

## 📤 Future plans

* 🧰 Turn into a real CLI package (`labelsync`)
* 🐍 Add `setup.py` / `pyproject.toml`
* 🌐 Upload to PyPI and Conda
* 📤 Export labels from a repo to TOML (planned)

