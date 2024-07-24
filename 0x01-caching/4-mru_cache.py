#!/usr/bin/env python3
"""MRUCache module"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUCache is a caching system that uses MRU algorithm for item replacement."""

    def __init__(self):
        """Initialize the MRU cache."""
        super().__init__()
        self.most_recent_key = None

    def put(self, key, item):
        """Add an item in the cache."""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if self.most_recent_key:
                    print(f"DISCARD: {self.most_recent_key}")
                    del self.cache_data[self.most_recent_key]

            self.cache_data[key] = item
            self.most_recent_key = key

    def get(self, key):
        """Get an item by key."""
        if key in self.cache_data:
            self.most_recent_key = key
            return self.cache_data[key]
        return None
