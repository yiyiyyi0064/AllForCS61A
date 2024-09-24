def tree(label,branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label]+list(branches)
def label(tree):
    return tree[0]
def branches(tree):
    return tree[1:]
def is_leave(tree):
    return len(tree)==1
def is_tree(tree):
    if type(tree) != list or len(tree)<1:
        return False
    for branch in branches(tree) :
        if not is_tree(branch):
            return False
    return True

def has_path(t,p):
    if t==p:
        return True
    elif t!=p and is_leave(t):
        return False
    else:
        return any(has_path(b,p[1:])for b in branches(t))
    #这个思路值得学习！
    #只要在这个拓展中，有一个 branch是满足的，那么就会返回true，直到返回最初引用的地方

def find_path(t,x):
    if x==t[0]:
        return list(x)
    for b in branches(t):
        path=find_path(b)
        if path:
            return [label(t)]+path
            #这个就是找到了之后 要输出上一级路径
    return None