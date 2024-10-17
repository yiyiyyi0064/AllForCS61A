############## You do not need to understand any of this code!
import base64
ob = "CmRlZiBhZGRpdGlvbihleHByKToKICAgIGRpdmlkZW5kID0gZXhwci5maXJzdAogICAgZXhwciA9IGV4cHIucmVzdAogICAgd2hpbGUgZXhwciAhPSBuaWw6CiAgICAgICAgZGl2aXNvciA9IGV4cHIuZmlyc3QKICAgICAgICBkaXZpZGVuZCArPSBkaXZpc29yCiAgICAgICAgZXhwciA9IGV4cHIucmVzdAogICAgcmV0dXJuIGRpdmlkZW5kCgpkZWYgc3VidHJhY3Rpb24oZXhwcik6CiAgICBkaXZpZGVuZCA9IGV4cHIuZmlyc3QKICAgIGV4cHIgPSBleHByLnJlc3QKICAgIHdoaWxlIGV4cHIgIT0gbmlsOgogICAgICAgIGRpdmlzb3IgPSBleHByLmZpcnN0CiAgICAgICAgZGl2aWRlbmQgLT0gZGl2aXNvcgogICAgICAgIGV4cHIgPSBleHByLnJlc3QKICAgIHJldHVybiBkaXZpZGVuZAoKZGVmIG11bHRpcGxpY2F0aW9uKGV4cHIpOgogICAgZGl2aWRlbmQgPSBleHByLmZpcnN0CiAgICBleHByID0gZXhwci5yZXN0CiAgICB3aGlsZSBleHByICE9IG5pbDoKICAgICAgICBkaXZpc29yID0gZXhwci5maXJzdAogICAgICAgIGRpdmlkZW5kICo9IGRpdmlzb3IKICAgICAgICBleHByID0gZXhwci5yZXN0CiAgICByZXR1cm4gZGl2aWRlbmQKCmRlZiBkaXZpc2lvbihleHByKToKICAgIGRpdmlkZW5kID0gZXhwci5maXJzdAogICAgZXhwciA9IGV4cHIucmVzdAogICAgd2hpbGUgZXhwciAhPSBuaWw6CiAgICAgICAgZGl2aXNvciA9IGV4cHIuZmlyc3QKICAgICAgICBkaXZpZGVuZCAvPSBkaXZpc29yCiAgICAgICAgZXhwciA9IGV4cHIucmVzdAogICAgcmV0dXJuIGRpdmlkZW5kCg=="
exec(base64.b64decode(ob.encode("ascii")).decode("ascii"))
##############

def calc_eval(exp):
    """
    >>> calc_eval(Pair("define", Pair("a", Pair(1, nil))))
    'a'
    >>> calc_eval("a")
    1
    >>> calc_eval(Pair("+", Pair(1, Pair(2, nil))))
    3
    """
    if isinstance(exp, Pair):
        operator = exp.first # UPDATE THIS FOR Q2
        operands = exp.rest # UPDATE THIS FOR Q2
        if operator == 'and': # and expressions
            return eval_and(operands)
        elif operator == 'define': # define expressions
            return eval_define(operands)
        else: # Call expressions
            #这句是最重要的 究竟是如何解析整个expr的
            return calc_apply(calc_eval(operator), operands.map(calc_eval)) # UPDATE THIS FOR Q2
        #显然仅仅传入operator和operands是远远不够的 需要再对这两个进行处理 确保得到最基本的形式
    elif exp in OPERATORS:   # Looking up procedures
        return OPERATORS[exp] #calc解析operators 最后不是pair只剩一个符号 就会到这里来 返回计算op
    elif isinstance(exp, int) or isinstance(exp, bool):   # Numbers and booleans
        return exp
    elif exp in bindings.keys(): # CHANGE THIS CONDITION FOR Q4
        return bindings[exp] # UPDATE THIS FOR Q4

def calc_apply(op, args):
    return op(args)

def floor_div(args):
    """
    >>> floor_div(Pair(100, Pair(10, nil)))
    10
    >>> floor_div(Pair(5, Pair(3, nil)))
    1
    >>> floor_div(Pair(1, Pair(1, nil)))
    1
    >>> floor_div(Pair(5, Pair(2, nil)))
    2
    >>> floor_div(Pair(23, Pair(2, Pair(5, nil))))
    2
    >>> calc_eval(Pair("//", Pair(4, Pair(2, nil))))
    2
    >>> calc_eval(Pair("//", Pair(100, Pair(2, Pair(2, Pair(2, Pair(2, Pair(2, nil))))))))
    3
    >>> calc_eval(Pair("//", Pair(100, Pair(Pair("+", Pair(2, Pair(3, nil))), nil))))
    20
    """
    "*** YOUR CODE HERE ***"
    #可以直接用while迭代！
    def multiple_div(exp,value):
        if exp==nil:
            #print(value)
            return value
        else:
            value=value//(exp.first)
            return multiple_div(exp.rest,value)
    #高阶函数:最后返回的值在mulptiple这里 而没有返回到调用处
    return multiple_div(args.rest,args.first)
    
    

scheme_t = True   # Scheme's #t
scheme_f = False  # Scheme's #f

def eval_and(expressions):
    """
    >>> calc_eval(Pair("and", Pair(1, nil)))
    1
    >>> calc_eval(Pair("and", Pair(False, Pair("1", nil))))
    False
    >>> calc_eval(Pair("and", Pair(1, Pair(Pair("//", Pair(5, Pair(2, nil))), nil))))
    2
    >>> calc_eval(Pair("and", Pair(Pair('+', Pair(1, Pair(1, nil))), Pair(3, nil))))
    3
    >>> calc_eval(Pair("and", Pair(Pair('-', Pair(1, Pair(0, nil))), Pair(Pair('/', Pair(5, Pair(2, nil))), nil))))
    2.5
    >>> calc_eval(Pair("and", Pair(0, Pair(1, nil))))
    1
    >>> calc_eval(Pair("and", nil))
    True
    """
    "*** YOUR CODE HERE ***"
    #没有传入and
    expr=expressions
    #其实我只要计算与and并列的pair
    #有可能 1,2,nil 
    val=scheme_t
    while expr!=nil:
        #退出时还有一个pair
        #要用is not 如果直接用!= 会导致变成值判断
        if calc_eval(expr.first) is not scheme_f:
            #print(calc_eval(expr.first))
            val=calc_eval(expr.first)
            expr=expr.rest
        else:
            return False
    return val

bindings = {}

def eval_define(expressions):
    """
    >>> eval_define(Pair("a", Pair(1, nil)))
    'a'
    >>> eval_define(Pair("b", Pair(3, nil)))
    'b'
    >>> eval_define(Pair("c", Pair("a", nil)))
    'c'
    >>> calc_eval("c")
    1
    >>> calc_eval(Pair("define", Pair("d", Pair("//", nil))))
    'd'
    >>> calc_eval(Pair("d", Pair(4, Pair(2, nil))))
    2
    """
    "*** YOUR CODE HERE ***"
    # symbol expressions(value)
    symbol=expressions.first
    #print(symbol)
    operand=expressions.rest
    if operand.rest is nil:
        operand=calc_eval(operand.first)
    else:
        #如果有两个pair pair("+", pair(2, nil))and没问题是因为总是调用的first
        #至少是这样 不会有单独进入pair(2,nil)的情况 
        operand=calc_eval(operand)
    bindings[symbol]=operand
    return symbol

OPERATORS = { "//": floor_div, "+": addition, "-": subtraction, "*": multiplication, "/": division }

class Pair:
    """A pair has two instance attributes: first and rest. rest must be a Pair or nil

    >>> s = Pair(1, Pair(2, nil))
    >>> s
    Pair(1, Pair(2, nil))
    >>> print(s)
    (1 2)
    >>> print(s.map(lambda x: x+4))
    (5 6)
    """
    def __init__(self, first, rest):
        self.first = first
        self.rest = rest

    def __repr__(self):
        return 'Pair({0}, {1})'.format(repr(self.first), repr(self.rest))

    def __str__(self):
        s = '(' + str(self.first)
        rest = self.rest
        while isinstance(rest, Pair):
            s += ' ' + str(rest.first)
            rest = rest.rest
        if rest is not nil:
            s += ' . ' + str(rest)
        return s + ')'

    def __len__(self):
        n, rest = 1, self.rest
        while isinstance(rest, Pair):
            n += 1
            rest = rest.rest
        if rest is not nil:
            raise TypeError('length attempted on improper list')
        return n

    def __eq__(self, p):
        if not isinstance(p, Pair):
            return False
        return self.first == p.first and self.rest == p.rest

    def map(self, fn):
        """Return a Scheme list after mapping Python function FN to SELF."""
        mapped = fn(self.first)
        if self.rest is nil or isinstance(self.rest, Pair):
            return Pair(mapped, self.rest.map(fn))
        else:
            raise TypeError('ill-formed list')

class nil:
    """The empty list"""

    def __repr__(self):
        return 'nil'

    def __str__(self):
        return '()'

    def __len__(self):
        return 0

    def map(self, fn):
        return self

nil = nil() # Assignment hides the nil class; there is only one instance

