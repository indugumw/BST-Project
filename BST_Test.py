import unittest
from Fraction import Fraction
from Binary_Search_Tree import Binary_Search_Tree
class BSTtester(unittest.TestCase):
    def setUp(self):
        self.__binary_tree = Binary_Search_Tree()
        self.__fraction_one = Fraction(1, 2)
        self.__fraction_two = Fraction(1, 3)
        self.__fraction_three = Fraction(2, 4)

    #Test in_order_traversal
    def test_empty_tree(self):
        self.assertEqual("[ ]", str(self.__binary_tree), 'Empty Tree should print "[ ]"')

    def test_insert_element_in_empty_tree(self):
        self.__bst.insert_element(1)
        self.assertEqual("[ 1 ]", str(self.__binary_tree), 'Tree should print "[ 1 ]"')
    
    def test_insert_5_elements_in_tree(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(2)
        self.__bst.insert_element(3)
        self.__bst.insert_element(4)
        self.__bst.insert_element(5)
        self.assertEqual("[ 1, 2, 3, 4, 5 ]", str(self.__bst), 'Tree should print "[ 1, 2, 3, 4, 5 ]"')

    def test_insert_2_identical_elements_in_tree(self):
        self.__bst.insert_element(2)
        with self.assertRaises(ValueError):
            self.__bst.insert_element(2)
        self.assertEqual("[ 2 ]", str(self.__bst), 'Tree should print [ 2 ]')
        
    def test_remove_from_empty_tree(self):
        with self.assertRaises(ValueError):
            self.__bst.remove_element(10)
        self.assertEqual("[ ]", str(self.__bst), 'An Empty Tree should print out "[ ]"')

    def test_remove_root_of_tree(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(2)
        self.__bst.remove_element(1)
        self.assertEqual("[ 2 ]", str(self.__bst), 'The tree should be [ 2 ]')

    def test_remove_root_of_tree_with_2_children(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(2)
        self.__bst.insert_element(3)
        self.__bst.remove_element(4)
        self.assertEqual("[ 2, 3 ]", str(self.__bst), 'The tree should be [ 2, 3 ]')

    def test_remove_5_elements_from_tree_with_10_elements(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(2)
        self.__bst.insert_element(3)
        self.__bst.insert_element(4)
        self.__bst.insert_element(5)
        self.__bst.insert_element(6)
        self.__bst.insert_element(7)
        self.__bst.insert_element(8)
        self.__bst.insert_element(9)
        self.__bst.insert_element(10)
        self.__bst.remove_element(1)
        self.__bst.remove_element(3)
        self.__bst.remove_element(5)
        self.__bst.remove_element(7)
        self.__bst.remove_element(9)
        self.assertEqual("[ 2, 4, 6, 8, 10 ]", str(self.__bst), 'The tree should print out "[ 2, 4, 6, 8, 10 ]"')

    def test_get_height_of_empty_tree(self):
        self.assertEqual("0", str(self.__bst.get_height()), 'Height of the Tree should be 0')

    def test_get_height_on_tree_with_1_element(self):
        self.__bst.insert_element(1)
        self.assertEqual("1", str(self.__bst.get_height()), 'Height of the Tree should be 1')
    
    def test_get_height_on_Tree_with_3_elements(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(2)
        self.__bst.insert_element(3)
        self.assertEqual("2", str(self.__bst.get_height()), 'Height of the Tree should be 2')
    
    def test_get_height_on_tree_with_5_elements(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(2)
        self.__bst.insert_element(3)
         self.__bst.insert_element(4)
        self.__bst.insert_element(5)
        self.assertEqual("3", str(self.__bst.get_height()), 'Height of the Tree should be 3')
    
    def test_get_height_on_Tree_with_5_elements_after_removing_3_elements(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(2)
        self.__bst.insert_element(3)
        self.__bst.insert_element(4)
        self.__bst.insert_element(5)
        self.__bst.remove_element(1)
        self.__bst.remove_element(3)
        self.__bst.remove_element(5)
        self.assertEqual("2", str(self.__bst.get_height()), 'Height of the Tree should be 2')

    def test_to_list_on_empty_tree(self):
        self.assertEqual([], self.__bst.to_list(), 'Tree should be []')

    def test_to_list_on_Tree_with_5_elements(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(10)
        self.__bst.insert_element(32)
        self.__bst.insert_element(8)
        self.__bst.insert_element(17)
        self.assertEqual([1, 8, 10, 17, 32], self.__bst.to_list(), 'Tree should print "[ 1, 8, 10, 17, 32 ]"')

    #Test pre_order_traversal
    def test_empty_tree_pre_order(self):
        self.assertEqual("[ ]", self.__bst.pre_order(), 'Empty Tree should print "[ ]"')
    
    def test_insert_element_on_empty_tree_pre_order(self):
        self.__bst.insert_element(17)
        self.assertEqual("[ 17 ]", self.__bst.pre_order(), 'Tree should print "[ 17 ]"')

    def test_insert_5_elements_on_tree_pre_order(self):
        self.__bst.insert_element(6)
        self.__bst.insert_element(4)
        self.__bst.insert_element(8)
        self.__bst.insert_element(9)
        self.__bst.insert_element(10)
        self.assertEqual("[ 6, 4, 9, 8, 10 ]", self.__bst.pre_order(), 'Tree should print "[ 6, 4, 9, 8, 10 ]"')

    def test_insert_2_identical_elements_on_tree_pre_order(self):
        self.__bst.insert_element(2)
        with self.assertRaises(ValueError):
            self.__bst.insert_element(2)
        self.assertEqual("[ 2 ]", self.__bst.pre_order(), 'Tree should be [ 2 ]')

    def test_remove_from_empty_tree_pre_order(self):
        with self.assertRaises(ValueError):
            self.__bst.remove_element(1)
        self.assertEqual("[ ]", self.__bst.pre_order(), 'Empty Tree should print "[ ]"')

    def test_remove_root_of_tree_pre_order(self):
        self.__bst.insert_element(2)
        self.__bst.insert_element(1)
        self.__bst.remove_element(2)
        self.assertEqual("[ 1 ]", self.__bst.pre_order(), 'Tree should be [ 1 ]')

    def test_remove_root_of_tree_with_2_children_pre_order(self):
        self.__bst.insert_element(6)
        self.__bst.insert_element(4)
        self.__bst.insert_element(8)
        self.__bst.remove_element(6)
        self.assertEqual("[ 8, 4 ]", self.__bst.pre_order(), 'Tree should be [ 8, 4 ]')

    def test_remove_3_elements_from_tree_with_5_elements_pre_order(self):
        self.__bst.insert_element(6)
        self.__bst.insert_element(4)
        self.__bst.insert_element(8)
        self.__bst.insert_element(9)
        self.__bst.insert_element(10)
        self.__bst.remove_element(6)
        self.__bst.remove_element(9)
        self.__bst.remove_element(10)
        self.assertEqual("[ 8, 4 ]", self.__bst.pre_order(), 'Tree should print "[ 8, 4 ]"')

    #Test post_order_traversal
    def test_empty_tree_post_order(self):
        self.assertEqual("[ ]", self.__bst.post_order(), 'Empty Tree should print "[ ]"')

    def test_insert_element_on_empty_tree_post_order(self):
        self.__bst.insert_element(38)
        self.assertEqual("[ 38 ]", self.__bst.post_order(), 'Tree should print "[ 38 ]"')

    def test_insert_5_elements_on_tree_post_order(self):
        self.__bst.insert_element(6)
        self.__bst.insert_element(4)
        self.__bst.insert_element(8)
        self.__bst.insert_element(9)
        self.__bst.insert_element(10)
        self.assertEqual("[ 4, 8, 10, 9, 6 ]", self.__bst.post_order(), 'Tree should print "[ 4, 8, 10, 9, 6 ]"')

    def test_insert_2_identical_elements_on_tree_post_order(self):
        self.__bst.insert_element(21)
        with self.assertRaises(ValueError):
            self.__bst.insert_element(21)
        self.assertEqual("[ 21 ]", self.__bst.post_order(), 'Tree should be [ 21 ]')

    def test_remove_from_empty_tree_post_order(self):
        with self.assertRaises(ValueError):
            self.__bst.remove_element(1)
        self.assertEqual("[ ]", self.__bst.post_order(), 'Empty Tree should print "[ ]"')

    def test_remove_root_from_tree_post_order(self):
        self.__bst.insert_element(17)
        self.__bst.insert_element(38)
        self.__bst.remove_element(17)
        self.assertEqual("[ 38 ]", self.__bst.post_order(), 'Tree should be [ 38 ]')

    def test_remove_root_from_tree_with_2_children_post_order(self):
        self.__bst.insert_element(21)
        self.__bst.insert_element(17)
        self.__bst.insert_element(38)
        self.__bst.remove_element(21)
        self.assertEqual("[ 17, 38 ]", self.__bst.post_order(), 'Tree should be [ 17, 38 ]')

    def test_remove_3_elements_from_tree_with_5_elements_post_order(self):
        self.__bst.insert_element(6)
        self.__bst.insert_element(4)
        self.__bst.insert_element(8)
        self.__bst.insert_element(9)
        self.__bst.insert_element(10)
        self.__bst.remove_element(6)
        self.__bst.remove_element(9)
        self.__bst.remove_element(10)
        self.assertEqual("[ 4, 8 ]", self.__bst.post_order(), 'Tree should print "[ 4, 8 ]"')

    #Test Fraction 
    def test_less_than_for_fraction_one(self):
        self.assertEqual(False, self.__fraction_one.__lt__(self.__fraction_two), 'Should return False because 1/2 is not less than 1/3')
        
    def test_less_than_for_fraction_two(self):
        self.assertEqual(True, self.__fraction_two.__lt__(self.__fraction_one), 'Should return True because 1/3 is less than 1/2')

    def test_greater_than_for_fraction_one(self):
        self.assertEqual(True, self.__fraction_one.__gt__(self.__fraction_two), 'Should return True because 1/2 is greater than 1/3')

    def test_greater_than_for_fraction_two(self):
        self.assertEqual(False, self.__fraction_two.__gt__(self.__fraction_one), 'Should return False because 1/3 is not greater than 1/2')

    def test_equals_for_fraction_one(self):
        self.assertEqual(True, self.__fraction_one.__eq__(self.__fraction_three), 'Should return True because 1/2 is equal to 2/4')

    def test_equals_for_fraction_two(self):
        self.assertEqual(False, self.__fraction_one.__eq__(self.__fraction_two), 'Should return False because 1/2 is not equal to 1/3')

if __name__ == '__main__':
  unittest.main()