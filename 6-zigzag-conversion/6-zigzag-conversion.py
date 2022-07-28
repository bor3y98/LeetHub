class Solution:
    def convert(self, s: str, numRows: int) -> str:
        i =0
        incerment=True
        string_list=["" for i in range(numRows)]
        for item in s:
            string_list[i]+=item
            if incerment:
                i+=1
                if i>=numRows:
                    i-=2
                    incerment=False
            else:
                i-=1
                if i<0:
                    i+=2
                    incerment=True
        return "".join(string_list)
            