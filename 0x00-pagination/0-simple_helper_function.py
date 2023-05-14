#!/usr/bin/env python3
"""   function named index_range
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Returns a tuple  
    """
    return ((page - 1) * page_size, page * page_size)