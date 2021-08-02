
class Tree_node():
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


class Binary_search_tree():

    def __init__(self):
        self.root = None


    def lookup(self, key):
        ''' return node with key, uses recursion '''

        def lookup_rec(node, key):
            if node == None:
                return None
            elif key == node.key:
                return node
            elif key < node.key:
                return lookup_rec(node.left, key)
            else:
                return lookup_rec(node.right, key)

        return lookup_rec(self.root, key)


    def insert(self, key, val):
        ''' insert node with key,val into tree, uses recursion '''

        def insert_rec(node, key, val):
            if key == node.key:
                node.val = val     # update the val for this key
            elif key < node.key:
                if node.left == None:
                    node.left = Tree_node(key, val)
                else:
                    insert_rec(node.left, key, val)
            else: #key > node.key:
                if node.right == None:
                    node.right = Tree_node(key, val)
                else:
                    insert_rec(node.right, key, val)
            return
        
        if self.root == None: #an empty tree
            self.root = Tree_node(key, val)
        else:
            insert_rec(self.root, key, val)


    def minimum(self):
        ''' return node with minimal key '''
        if self.root == None:
            return None
        node = self.root
        left = node.left
        while left != None:
            node = left
            left = node.left
        return node


    def depth(self):
        ''' return depth of tree, uses recursion'''
        def depth_rec(node):
            if node == None:
                return -1
            else:
                return 1 + max(depth_rec(node.left), depth_rec(node.right))

        return depth_rec(self.root)


    def size(self):
        ''' return number of nodes in tree, uses recursion '''
        def size_rec(node):
            if node == None:
                return 0
            else:
                return 1 + size_rec(node.left) + size_rec(node.right)

        return size_rec(self.root)


    
    def is_sorted(self):
        '''return True iff the tree is sorted, given that vals are between 0 to 100'''
        node = self.root
        def rec_is_sorted(node, min_val, max_val):
            if node == None:
                return True
            else:
                if node.val >= min_val and node.val <= max_val:
                    return rec_is_sorted(node.left, min_val, node.val) and rec_is_sorted(node.right, node.val, max_val)
                else:
                    return False
                        
        return rec_is_sorted(node, 0, 100)



