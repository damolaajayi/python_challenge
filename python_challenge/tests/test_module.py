import unittest
from python_challenge import is_val_in_tree

lst1 = [3, [7, [1, None, None], [8, None, None]], [5, None, [4, None, None]]]
lst2_8 = [2, None, None]
lst2_6 = [24, None, None]
lst2_7 = [18, None, None]
lst2_4 = [4, lst2_8, None]
lst2_3 = [12, None, lst2_4]
lst2_2 = [10, None, lst2_3]
lst2_1 = [15, lst2_2, None]
lst2_5 = [6, lst2_6, lst2_7]
lst2 = [9, lst2_1, lst2_5]
lst3_1 = [4, None, None]
lst3_2 = [9, None, None]
lst3_3 = [21, None, None]
lst3_4 = [17, None, None]
lst3_5 = [25, None, None]
lst3_6 = [18, lst3_5, None]
lst3_7 = [20, lst3_3, lst3_4]
lst3_8 = [91, lst3_2, None]
lst3_9 = [75, None, lst3_1]
lst3_10 = [45, None, None]
lst3_11 = [71, None, None]
lst3_12 = [34, None, None]
lst3_13 = [11, None, None]
lst3_14 = [10, lst3_6, lst3_13]
lst3_15 = [3, lst3_7, lst3_12]
lst3_16 = [26, lst3_8, lst3_11]
lst3_17 = [1, lst3_9, lst3_10]
lst3_18 = [66, lst3_14, lst3_17]
lst3_19 = [52, lst3_16, lst3_15]
lst3 = [97, lst3_18, lst3_19]


class BinaryTestCase(unittest.TestCase):
    def test_val_in_tree(self):
        self.assertEqual(is_val_in_tree(lst1, 5), True)
        self.assertEqual(is_val_in_tree(lst1, 9), False)
        self.assertEqual(is_val_in_tree(lst2, 51), False)
