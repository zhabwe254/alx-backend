#!/usr/bin/env python3
"""MRUCache module"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUCache defines:
      - Caching system with MRU algorithm
    """

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item in the cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key not in self.cache_data:
                    discard = self.order.pop()
                    del self.cache_data[discard]
                    print(f"DISCARD: {discard}")
            
            self.cache_data[key] = item
            if key in self.order:
                self.order.remove(key)
            self.order.append(key)

    def get(self, key):
        """Get an item by key"""
        if key is not None and key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
        return self.cache_data.get(key) if key is not None else None
