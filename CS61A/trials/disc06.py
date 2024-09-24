def gen_fin():
    n,add= 0,1
    while True:
        yield n
        n,add=n+add,n

def differences(t):
    previous_x=next(t)
    for x in t:#自带next
        yield x-previous_x
        previous_x=x #保存上一个数 for自带next x会跳到下一个数 需要保存上一个数来compare

def partition_gen(n,m):
    exat_match= []
    if n<0 or m==0:
        return []
    else:
        if n==m:
            exat_match= [[m]] # 所以这里用[[m]]的原因也清楚了：因为相当于当前情况的一种分支 如果是最后那么就会返回到引用处
        #不能直接用return的原因是：如果3==3 就return了那么就会缺少更加细分的可能 比如1+1+1
        with_m = [p+[[m]] for p in partition_gen(n-m,m)]
        #但是因为是 p in partition 那么就只会取出[[m,n,q]]中的[m,n,q] 来构成with_m中的一种
        #with_m 可能有多种 但都要和已经取出的m进行组合 合成为完整的取用方式
        without_m=partition_gen(n,m-1) #这里就是完全两种可能了，如果不一样不会放在一起的，路径是完全不同的
        return with_m+without_m+exat_match #当下的mn所有的匹配方式 
def list_partition(n,m):
   if n>0 and m>0:
        if n==m:
           yield str(m)
        for p in list_partition(n-m,m):
           yield p+'+'+str(m)
        yield from list_partition(n,m-1)
        #recursive 想要recursive后所有的结果        