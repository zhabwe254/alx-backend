#!/usr/bin/env python3
"""LIFOCache module"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache is a caching system that uses LIFO algorithm for item replacement."""

    def __init__(self):
        """Initialize the LIFO cache."""
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache."""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Discard the last inserted item
                last_key = next(reversed(self.cache_data))
                print(f"DISCARD: {last_key}")
                del self.cache_data[last_key]

            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key."""
        return self.cache_data.get(key, None)
