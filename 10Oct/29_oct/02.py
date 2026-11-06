class mutstr:
    def __init__(self,s):
        self.chars = list(s)

    def update(self,i,ch):
        self.chars[i] = ch

    def __repr__(self):
        res = ''
        for ch in self.chars:
            res += ch
        return res

st = mutstr('abc')
print(st)
print(id(st))
st.update(2,'d')
print(id(st))
print(st)
