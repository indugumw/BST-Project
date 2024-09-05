class Binary_Search_Tree:
  # TODO.I have provided the public method skeletons. You will need
  # to add private methods to support the recursive algorithms
  # discussed in class

  class __BST_Node:
    # TODO The Node class is private. You may add any attributes and
    # methods you need. Recall that attributes in an inner class 
    # must be public to be reachable from the the methods.

    def __init__(self, value):
      self.value = value
      # TODO complete Node initialization
      self.left = None
      self.right = None
      self.height = 1

  #Update height of the node
  def update_height(self, node):
    r_height = 0
    l_height = 0
    #If the tree only contains the root node
    if node.left is None and node.right is None: 
      node.height = 1
    #If root node has children
    else:
      if node.left is not None:
        l_height = l_height + node.left.height
      if node.right is not None:
        r_height = r_height + node.right.height
    if r_height < l_height:
      node.height = l_height + 1
    else:
      node.height = r_height + 1
    return node.height

  def __init__(self):
    self.__root = None
    # TODO complete initialization
  
  #Determine whether value goes to the right or left side of the tree
  def __recursive_insert(self, node, val):
    #Base Case
    if node is None:
      return Binary_Search_Tree.__BST_Node(val)
    if node.value == val:
      raise ValueError
    #Recursive Case
    if val < node.value:
      node.left = self.__recursive_insert(node.left, val)
    else:
      node.right = self.__recursive_insert(node.right, val)
    #Updates height of the Nodes
    self.update_height(node)
    return self.__balance(node)

  #Remove node from the tree
  def __recursive_remove(self, node, val):
    if node is None:
      raise ValueError

    #Base Case
    if node.value == val:
      if (node.right is None) and (node.left is None):
        return None
      if node.left is None and node.right is not None:
        return node.right
      if node.right is None and node.left is not None: 
        return node.left
      #Recursive Case
      if node.left is not None and node.right is not None:
        node.value = self.locate_min(node.right)
        node.right = self.__recursive_remove(node.right, node.value)
    #Recursive Case
    elif val < node.value:
      node.left = self.__recursive_remove(node.left, val)
    elif val > node.value:
      node.right = self.__recursive_remove(node.right, val)
    #Update heights of the Nodes
    self.update_height(node)
    return self.__balance(node)

  #Locates minimum value of the node
  def locate_min(self, node):
    temp = node
    while temp.left is not None:
      temp = temp.left
    return temp.value
    
  def __recursive_in_order(self, node):
    s = ''
    #Add left nodes from tree to string
    if node.left is not None:
        s = s + self.__recursive_in_order(node.left)
    #Add root node value to string
    s = s + str(node.value) + ", "
    #Add right nodes from tree to string
    if node.right is not None:
        s = s + self.__recursive_in_order(node.right)
    return s

  def __recursive_pre_order(self, node):
    s = ''
    #Add root node value to string
    s = s + str(node.value) + ", "
    #Add left nodes from tree to string
    if node.left is not None:
        s = s + self.__recursive_pre_order(node.left)
    #Add right nodes from tree to string
    if node.right is not None:
        s = s + self.__recursive_pre_order(node.right)
    return s

  def __recursive_post_order(self, node):
    s = ''
    #Add left nodes from tree to string
    if node.left is not None:
        s = s + self.__recursive_post_order(node.left)
    #Add right nodes from tree to string
    if node.right is not None:
        s = s + self.__recursive_post_order(node.right)
    #Add root node value to string
    s = s + str(node.value) + ", "
    return s

  def __balance(self, node):
    #If node is balanced
    if self.__get_balance(node) == 0 or self.__get_balance(node) == 1 or self.__get_balance(node) == -1:
      return node
    #If node is left-heavy
    if self.__get_balance(node) == -2:
      if self.__get_balance(node.left) == 0 or self.__get_balance(node.left) == -1:
        return self.__right_rotation(node)
      if self.__get_balance(node.left) == 1:
        node.left = self.__left_rotation(node.left)
        return self.__right_rotation(node) 
    #If node right-heavy
    if self.__get_balance(node) == 2:
      if self.__get_balance(node.right) == 0 or self.__get_balance(node.right) == 1:
        return self.__left_rotation(node)
      if self.__get_balance(node.right) == -1:
        node.right = self.__right_rotation(node.right)
        return self.__left_rotation(node)

  def __get_balance(self, node):
    r_position = 0
    l_position = 0
    if node.right is not None:
      r_position = r_position + node.right.height
    if node.left is not None:
      l_position = l_position + node.left.height
    balance = r_position - l_position
    return balance
  
  def __left_rotation(self, node):
    #Shift nodes if tree is right-heavy
    temp = node.right
    node.right = temp.left
    temp.left = node
    self.update_height(node)
    self.update_height(temp)
    return temp

  def __right_rotation(self, node):
    #Shift nodes if tree is left-heavy
    temp = node.left
    node.left = temp.right
    temp.right = node
    self.update_height(node)
    self.update_height(temp)
    return temp

  #Change the values in a binary tree to a list
  def __recursive_tree_to_list(self, node):
    l = []
    #To_list follows the same arrangement as in_order_traversal
    if node is not None:
      #Add the left nodes of the tree to the list first
      l = self.__recursive_tree_to_list(node.left) 
      #Add the root node to the list
      l.append(node.value)
      #Add the right nodes of the tree to the list
      l = l + self.__recursive_tree_to_list(node.right)
    return l

  def to_list(self):
    return self.__recursive_tree_to_list(self.__root)
    
  def insert_element(self, value):
    # Insert the value specified into the tree at the correct
    # location based on "less is left; greater is right" binary
    # search tree ordering. If the value is already contained in
    # the tree, raise a ValueError. Your solution must be recursive.
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    # TODO replace pass with your implementation
    self.__root = self.__recursive_insert(self.__root, value)

  def remove_element(self, value):
    # Remove the value specified from the tree, raising a ValueError
    # if the value isn't found. When a replacement value is necessary,
    # select the minimum value to the from the right as this element's
    # replacement. Take note of when to move a node reference and when
    # to replace the value in a node instead. It is not necessary to
    # return the value (though it would reasonable to do so in some 
    # implementations). Your solution must be recursive. 
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    # TODO replace pass with your implementation
    self.__root = self.__recursive_remove(self.__root, value)

  def in_order(self):
    # Construct and return a string representing the in-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed as [ 4 ]. Trees with more
    # than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    # TODO replace pass with your implementation
    if self.__root is None:
        return "[ ]"
    s = "[ "
    s = s + self.__recursive_in_order(self.__root)[:-2]
    s = s + " ]"
    return s
    
  def pre_order(self):
    # Construct and return a string representing the pre-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    # TODO replace pass with your implementation
    if self.__root is None:
        return "[ ]"
    s = "[ "
    s = s + self.__recursive_pre_order(self.__root)[:-2]
    s = s + " ]"
    return s


  def post_order(self):
    # Construct an return a string representing the post-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    # TODO replace pass with your implementation
    if self.__root is None:
        return "[ ]"
    s = "[ "
    s = s + self.__recursive_post_order(self.__root)[:-2]
    s = s + " ]"
    return s

  def get_height(self):
    # return an integer that represents the height of the tree.
    # assume that an empty tree has height 0 and a tree with one
    # node has height 1. This method must operate in constant time.
    # TODO replace pass with your implementation
    if self.__root is not None:
        return self.__root.height
    return 0

  def __str__(self):
    return self.in_order()

if __name__ == '__main__':
  pass #unit tests make the main section unnecessary