# Pagination Project

This project implements various pagination techniques in Python, including simple pagination, hypermedia pagination, and deletion-resilient hypermedia pagination.

## Files

1. `0-simple_helper_function.py`: Contains a helper function `index_range` for calculating pagination indexes.
2. `1-simple_pagination.py`: Implements simple pagination for a CSV dataset.
3. `2-hypermedia_pagination.py`: Extends the simple pagination to include hypermedia metadata.
4. `3-hypermedia_del_pagination.py`: Implements deletion-resilient hypermedia pagination.

## Requirements

- Python 3.7+
- Ubuntu 18.04 LTS
- pycodestyle 2.5.*

## Setup

1. Ensure you have Python 3.7+ installed on your Ubuntu 18.04 LTS system.
2. Place the `Popular_Baby_Names.csv` file in the same directory as the Python scripts.

## Usage

Each file can be run independently. Here are some examples:

### 0-simple_helper_function.py

```bash
./0-main.py
1-simple_pagination.py
bashCopy./1-main.py
2-hypermedia_pagination.py
bashCopy./2-main.py
3-hypermedia_del_pagination.py
bashCopy./3-main.py
Code Style
This project follows the pycodestyle style guide (version 2.5.*). You can check your code style by running:
bashCopypycodestyle *.py
Documentation
All modules and functions are documented. You can view the documentation using Python's built-in help() function or by running:
bashCopypython3 -c 'print(__import__("my_module").__doc__)'
python3 -c 'print(__import__("my_module").my_function.__doc__)'
Type Annotations
All functions and methods use type annotations to improve code readability and catch potential type-related errors.
Author
GIDEON MARK ZION HABWE
License
This project is licensed under the MIT License - see the LICENSE file for details.
Copy
This README provides an overview of your project, lists the files included, outlines the requirements, and gives instructions on how to set up and use the code. It also mentions the coding style used, documentation practices, and the use of type annotations.

