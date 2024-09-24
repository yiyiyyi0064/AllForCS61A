def prefixes(s):
    if s:
        yield from prefixes(s[:-1])
        yield s
#最后调用的反而最先生成 
def prefix(s):
    if s:
        for x in prefix(s[:-1]):#每执行一次就少一个
            yield x
        yield s

def substrings(s):
    if s:
        yield from prefixes(s)
        yield from substrings(s[1:]) #每执行一次就少一个
        #每取一个值x 都会调用一次substrings 那么就会执行其内部函数 
        #就会调用生成prefixes 直到sub的next为' '

def list_partitions(n,m):
    if n<0 or m==0:
        return []
    else:
        if m==n:
            exact_match=[[m]]
    with_m=[p+[m] for p in list_partitions(n-m,m)]
    without_m=list_partitions(n,m-1)
    #一直在纠结without前面已经用的怎么办 实际上每一条路径都是unique
    #后面得到的数据 一定会返回到with中 组成数组 否则n不会变化也就是没使用
    return with_m+without_m+exact_match