# Caching Project

This project implements various caching systems in Python. Each caching system inherits from a base class `BaseCaching` and implements different caching algorithms.

## Files

- `base_caching.py`: Contains the base class `BaseCaching`.
- `0-basic_cache.py`: Implements a basic caching system with no limit.
- `1-fifo_cache.py`: Implements a First-In-First-Out (FIFO) caching system.
- `2-lifo_cache.py`: Implements a Last-In-First-Out (LIFO) caching system.
- `3-lru_cache.py`: Implements a Least Recently Used (LRU) caching system.
- `4-mru_cache.py`: Implements a Most Recently Used (MRU) caching system.

## Requirements

- All files are interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All files end with a new line
- The first line of all files is exactly `#!/usr/bin/env python3`
- Code uses the pycodestyle style (version 2.5)
- All files are executable
- All modules, classes, and functions have documentation

## Usage

Each caching system can be used as follows:

```python
# Example for BasicCache
from 0-basic_cache import BasicCache

my_cache = BasicCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
print(my_cache.get("A"))  # Output: Hello
print(my_cache.get("B"))  # Output: World
Similar usage applies to other caching systems (FIFOCache, LIFOCache, LRUCache, MRUCache).
Testing
Test files are provided for each caching system:

0-main.py
1-main.py
2-main.py
3-main.py
4-main.py

Run these files to test the corresponding caching system.
Author:
Gideon Habwe
