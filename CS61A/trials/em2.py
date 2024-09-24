def insert_items(s,before,after):    
    i=0
    while i<len(s):
        if before == s[i]:
            s=s[:i]+[s[i]]+[after]+s[(i+1):]
            i=i+1
        i=i+1
    return s
