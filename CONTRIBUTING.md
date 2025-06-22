
# 🤝 Contributing to LabelSync

Thank you for considering contributing to **LabelSync**! Whether it's fixing a bug, improving documentation, or adding a new feature — all contributions are welcome.

---

## 📦 Getting Started

1. **Fork** the repository on GitHub
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/your-username/labelsync.git
   cd labelsync
   ```

3. **Create a virtual environment** using Conda or Python:

   ```bash
   # Using Conda
   conda env create -f environment.yml
   conda activate labelsync

   # OR using pip
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
4. **Install the project in editable mode**:

   ```bash
   pip install -e .
   ```

---

## 🧪 Running Tests

Use `pytest` to run the test suite:

```bash
pytest tests/
```

Lint the code with:

```bash
flake8 labelsync/
```

We (Why do I refer to myself as we?) encourage you to run both before submitting a pull request!

---

## ✨ Feature Ideas

You are welcome to open issues for ideas or suggestions. Planned features include:

* `labelsync export`: save current GitHub labels to a TOML file
* `labelsync validate`: check structure and correctness of TOML input
* PyPI/conda-forge packaging
* More unit tests and edge-case coverage

---

## 🧷 Creating Issues & Labeling Them

If you're opening an issue — thanks for helping improve the project!

Here’s how to make your issue extra helpful:

### 🧾 What to include

- A **clear title** and summary of the problem or feature request
- Steps to reproduce (for bugs)
- Expected vs actual behavior
- If relevant: screenshots, CLI commands used, traceback logs, etc.

### 🏷️ Labeling your issue

Yes, we have a tool for managing labels — so we *do* care about them! 😄  
Please help by **applying appropriate labels** when opening an issue or pull request.

Examples:

- Use `bug` for something broken 🐞
- Use `enhancement` for feature suggestions 💡
- Use `question` if you're unsure how something works ❓
- Use `good first issue` for small, self-contained improvements 🐣

> Not sure which label fits? No worries — just open the issue and we’ll sort it out.

### 🙋 Need Help?

Use the `help wanted` label if you're stuck or need a second pair of eyes!

---

## 📄 Submitting a Pull Request

1. Make your changes in a new branch:

   ```bash
   git checkout -b fix/something-interesting
   ```

2. Commit with a meaningful message:

   ```bash
   git commit -m "fix: correct label color handling"
   ```

3. Push and open a pull request on GitHub.

Please keep your PR focused on a single change (bug fix, feature, etc.).

---

## 👕 Code Style

Follow the existing formatting. We aim for:

* **PEP8** style guide (checked with `flake8`)
* **Descriptive log messages** (with `loguru`)
* **Inline comments and docstrings** for functions and modules

---

## 🔐 Security & Access

Currently, the repository is public but limited in scope. If needed, you may contact the maintainer privately with security-sensitive concerns.

---

## 🙌 Thank You!

Your time, ideas, and energy help make LabelSync better for everyone.
We're (Again... I keep referring to myself as us.... Well, never mind - let's carry on!) happy you're here. 🐙
