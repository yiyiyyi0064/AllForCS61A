def draw(hand,positions):
    positions=sorted(positions)
    result=[]
    for i in positions:
        result+=[hand[i]]
    for i in result:
        hand.remove(i)
    return result 
    #return list(reversed( [hand.pop(i) for i in reversed(sorted(positions))] ))
    #真的蛮厉害的，因为如果前面变量减少了，会影响后面变量的删除，所以先删除后面的！神！

LOWERCASE_LETTERS='abcdefghigklmnopqrstuvwxyz'
class capslock:
    def __init__(self):
        self.pressed=0
    def press(self):
        self.pressed+=1
class Button:
    caps=capslock()
    #这是对于所有的button都是这样的
    def __init__(self,letter,output):
        #output 就是指的操作
        assert letter in LOWERCASE_LETTERS
        #要求所有的letter 必须在要求字母中
        self.letter=letter
        self.output=output
        self.pressed=0
    def press(self):
        self.pressed += 1
        if self.caps.pressed%2==0:
            self.output(self.letter)
        else:
            self.output(self.letter.upper())
        return self

class keyboard:
    def __init__(self) :
        self.typed=[]
        self.keys={c: Button(c,self.typed.append) for c in LOWERCASE_LETTERS}    
    def type(self,word):
        assert all([w in LOWERCASE_LETTERS for w in word]), 'word must be all lowercase'
        for w in word:
            self.keys[w].press()
            #word中的单词载入typed


    
        