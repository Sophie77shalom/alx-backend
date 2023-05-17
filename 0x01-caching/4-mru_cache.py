#!/usr/bin/python3
"""  class MRUCache that inherits from BaseCaching
"""

from collections import deque

BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """ Create a class MRUCache 
     
    """

    def __init__(self):
        """ Init
        """
        super().__init__()
        self.queue = deque()

    def put(self, key, item):
        """ Must assign to the dictionary  
         
        """
        if key and item:
            if key in self.cache_data:
                self.queue.remove(key)
            elif self.is_full():
                self.evict()
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Must return the value in self.cache_data  
        """
        if key in self.cache_data:
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache_data.get(key)

    def is_full(self):
        """ If the number of items in self.cache_data is higher that
        BaseCaching.MAX_ITEMS
        """
        return len(self.cache_data) >= self.MAX_ITEMS

    def evict(self):
        """ you must print DISCARD:  
        new line
        """
        popped = self.queue.pop()
        del self.cache_data[popped]
        print("DISCARD: " + str(popped))