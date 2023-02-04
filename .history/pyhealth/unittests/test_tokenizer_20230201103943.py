import unittest
import sys 
import os
current = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname(os.path.dirname(current)))

from pyhealth import tokenizer

token_space = ['A01A', 'A02A', 'A02B', 'A02X', 'A03A', 'A03B', 'A03C', 'A03D', 'A03E', \
          'A03F', 'A04A', 'A05A', 'A05B', 'A05C', 'A06A', 'A07A', 'A07B', 'A07C', \
          'A07D', 'A07E', 'A07F', 'A07X', 'A08A', 'A09A', 'A10A', 'A10B', 'A10X', \
          'A11A', 'A11B', 'A11C', 'A11D', 'A11E', 'A11G', 'A11H', 'A11J', 'A12A', \
          'A12B', 'A12C', 'A13A', 'A14A', 'A14B', 'A16A']


class Test1D(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()


if __name__ == "__main__":
    unittest.main()