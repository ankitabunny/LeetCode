class Solution:
    def backtrack(self, current: string, open:int, close:int, n:int):
        # Base case
        if len(current)==2*n:
            self.result.append(current)
            return 
        
        # Add opening bracket
        if open<n:
            self.backtrack(current+'(',open+1,close,n)

        # Add closing bracket
        if close<open:
            self.backtrack(current+')',open,close+1,n)
    
    def generateParenthesis(self, n: int) -> list[str]:
        self.result=[]
        self.backtrack("",0,0,n)

        return self.result

        
