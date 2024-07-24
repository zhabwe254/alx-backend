#!/usr/bin/env python3
"""LRUCache module"""

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """LRUCache is a caching system that uses LRU algorithm for item replacement."""

    def __init__(self):
        """Initialize the LRU cache."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item in the cache."""
        if key is not None and item is not None:
            # Move existing key to the end
            if key in self.cache_data:
                self.cache_data.move_to_end(key)

            # Check if cache size exceeds limit
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key, _ = self.cache_data.popitem(last=False)
                print(f"DISCARD: {discarded_key}")

            # Add the item
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key."""
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None
