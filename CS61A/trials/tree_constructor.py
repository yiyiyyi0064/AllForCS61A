""" Build a tree constructor """
def tree(root_label, branches=[]):
    for branch in branches:
        assert is_tree(branch),'branches must be trees'
    return[root_label]+list(branches)
"""Assert and Consctruct trees with notifications"""
def label(tree):
    return tree[0]
"""The first number of the tree list Represents the tree label"""
def branches(tree):
    return tree[1:]
def is_tree(tree):
    if type(tree)!=list or len(tree)< 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True
def is_leave(tree):
    return not branches(tree)

def fib_tree(n):
    if n==0 or n==1:
        return tree(n)
    else :
        left,right=fib_tree(n-2),fib_tree(n-1)
        fib_n=label(left)+label(right)
        return tree(fib_n,[left,right])
def partition_tree(n,m):
    """Return a partition tree of n using parts of up to m"""
    if n==0:
        return tree(True)
    elif n<0 or m==0:
        return tree(False)
    else:
        left=partition_tree(n-m,m)
        right=partition_tree(n,m-1)
        return tree(m,[left,right])
""""partition=[] which means if we dont deliver a value it will automatically bind with []"""
def print_parts(tree, partition=[]):
    if is_leave(tree):
        if label(tree):
            print('+'.join(partition))
    else:
        left,right=branches(tree)
        m=str(label(tree))
        print_parts(left,partition+[m])
        print_parts(right,partition)