class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stack=[]
        #sort according to first element
        z=sorted(intervals, key=lambda x: x[0])
        print(z)
        stack.append(z[0])
        a=stack[0][0]
        b=stack[0][1]
        for i in range(1,len(z)):
            c=z[i][0]
            d=z[i][1]
            if(c<=b and d<=b):
                stack.pop()
                stack.append([a,b])
            elif(c<=b and d>=b):
                stack.pop()
                stack.append([a,d])
            else:
                stack.append([c,d])
            a=stack[-1][0]
            b=stack[-1][1]
        return stack
        
