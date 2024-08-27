"""Check numpy version."""
__author__ = "Dr. Saad Laouadi"
__copyright__ = "All rights reserved to the author"

import sys
import numpy as np


def print_np_version():
    """Print numpy version."""
    print(np.__version__)

if __name__ == "__main__":
    print_np_version()
    print(sys.executable)
