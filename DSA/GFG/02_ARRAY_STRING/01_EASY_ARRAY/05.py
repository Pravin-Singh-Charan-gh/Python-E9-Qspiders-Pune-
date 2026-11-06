class Solution:
    @staticmethod
    def rev_arr(arr,st,end):
        while st<end:
            arr[st],arr[end] = arr[end],arr[st]
            st+=1
            end-=1
            
    def rotateArr(self, arr, d):
        # code here
        n = len(arr)
        d %= n
        
        self.rev_arr(arr,0,d-1)
        self.rev_arr(arr,d,n-1)
        self.rev_arr(arr,0,n-1)
        