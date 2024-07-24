#!/usr/bin/env python3
"""LFUCache module"""

from base_caching import BaseCaching
from collections import defaultdict, OrderedDict


class LFUCache(BaseCaching):
    """LFUCache is a caching system that uses LFU algorithm for item replacement."""

    def __init__(self):
        """Initialize the LFU cache."""
        super().__init__()
        self.frequency = defaultdict(int)
        self.usage_order = OrderedDict()

    def put(self, key, item):
        """Add an item in the cache."""
        if key is not None and item is not None:
            # Update existing item frequency
            if key in self.cache_data:
                self.frequency[key] += 1
                self.usage_order.move_to_end(key)

            else:
                # Check if cache size exceeds limit
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    # Find the least frequently used key
                    min_freq = min(self.frequency.values())
                    lfu_keys = [k for k in self.frequency if self.frequency[k] == min_freq]
                    # Use LRU among the LFU
                    for k in self.usage_order:
                        if k in lfu_keys:
                            print(f"DISCARD: {k}")
                            del self.cache_data[k]
                            del self.frequency[k]
                            self.usage_order.pop(k)
                            break

                # Add the new item
                self.cache_data[key] = item
                self.frequency[key] = 1
                self.usage_order[key] = True

    def get(self, key):
        """Get an item by key."""
        if key in self.cache_data:
            self.frequency[key] += 1
            self.usage_order.move_to_end(key)
            return self.cache_data[key]
        return None
