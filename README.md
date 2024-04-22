#  proj_master : Project Structure Generator

This Python script generates a standardized project structure for your Python projects. It creates the necessary folders and files based on your specifications.

---

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Usage](#usage)
- [Parameters](#parameters)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

---

## Introduction

The Project Structure Generator is a handy tool for Python developers to quickly set up the directory structure for their projects. It automates the creation of common directories and files, saving time and ensuring consistency across projects.

---

## Features

- Supports two modes: standard mode and pro mode.
- Standard mode creates basic project structure with essential folders and files.
- Pro mode includes additional folders and files for more comprehensive projects.
- Customizable project name and directory structure.

---

## Usage

```bash
pip install proj-master
```

Let's say you want to create a new project called "MyAwesomeProject" in pro mode. You would run the following command:


```python
from proj_master import Cat

Cat.build_structure(project_name="MyAwesomeProject", developer_name="Hardy21", pro_mode=True)
```


- `project_name`: Name of the project (root directory name).
- `pro_mode`: (Optional) If set to `True`, creates a more comprehensive project structure. Default is `False`.


This will create the following directory structure:

```
MyAwesomeProject/
│
├── dev/
├── src/
├── tests/
├── utils/
├── docs/
├── data/
├── config/
├── logs/
│
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
├── requirements-dev.txt
├── setup.py
├── CHANGELOG.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── MANIFEST.in
└── pyproject.toml
```


---


## Contributing

Contributions are welcome! If you have any ideas, suggestions, or improvements, feel free to open an issue or submit a pull request.


---

## License

This project is provided under the BSD License.

For more information, please see the [LICENSE](LICENSE) file.

---
