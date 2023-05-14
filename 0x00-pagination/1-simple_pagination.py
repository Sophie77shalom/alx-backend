#!/usr/bin/env python3
"""  Takes two integer arguments page with default value 1
"""

import csv
from typing import List, Tuple


class Server:
    """Server class to paginate a database 
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Finds the correct indexes  
        """
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0
        csv_size = len(self.dataset())
        start, end = index_range(page, page_size)
        end = min(end, csv_size)
        if start >= csv_size:
            return []
        return self.dataset()[start:end]


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Returns a tuple  
    """
    return ((page - 1) * page_size, page * page_size)
