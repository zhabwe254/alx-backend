
#!/usr/bin/env python3
"""FIFOCache module"""

from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """FIFOCache is a caching system that uses FIFO algorithm for item replacement."""

    def __init__(self):
        """Initialize the FIFO cache."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item in the cache."""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key, _ = self.cache_data.popitem(last=False)
                print(f"DISCARD: {discarded_key}")

            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key."""
        return self.cache_data.get(key, None)
