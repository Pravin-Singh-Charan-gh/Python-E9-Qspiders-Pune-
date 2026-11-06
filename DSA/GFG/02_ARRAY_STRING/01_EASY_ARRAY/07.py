class Solution:
    def rearrange(self,arr):
        # code here
        pos = []
        neg = []
        for i in arr:
            if i>=0:
                pos.append(i)
            else:
                neg.append(i)
                
        pi = ni = 0
        i = 0
        while pi<len(pos) and ni<len(neg):
            arr[i] = pos[pi]
            pi+=1
            i+=1
            arr[i] = neg[ni]
            ni+=1
            i+=1
        while pi<len(pos):
            arr[i] = pos[pi]
            pi+=1
            i+=1
            
        while ni<len(neg):
            arr[i] = neg[ni]
            ni+=1
            i+=1
        