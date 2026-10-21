class Solution:
    def minOperations(self,s:str)->int:
        n=len(s)
        arr=list(s)
        sorted_str=True
        for i in range(1,n):
            if arr[i]<arr[i-1]:
                sorted_str=False
                break
        if sorted_str:
            return 0
        if n==2:
            return -1
        minChar=min(arr)
        maxChar=max(arr)
        if arr[0]==minChar or arr[n-1]==maxChar:
            return 1
        minMid=min(arr[1:n-1])
        maxMid=max(arr[1:n-1])
        if arr[0]>maxMid and arr[n-1]<minMid:
            return 3
        return 2