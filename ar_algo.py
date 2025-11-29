
class arrayHndler:
    """
    BELOW ITS ONLY LEVEL 1 ARRAY/LIST PROBLEMS
    """
    def __init__(self,ar:list):
        self.ar = ar
    def Length(self):
        return len(self.ar)
    
    def Max(self):
        max = 0
        for k in range(0,len(self.ar)):
            if self.ar[k] > max:
                max = self.ar[k]
        return max
    
    def Min(self):
        min = 0
        for j in range(0,len(self.ar)):
            if min > self.ar[j]:
                min = self.ar[j]
        return min
    
    def Reverse(self):
        ret_ = []
        for i in range(len(self.ar)-1,-1,-1):
            ret_.append(self.ar[i])
        return ret_
    def CountOcc(self,val):
        count_occ = 0
        for i in range(0,len(self.ar)):
            if self.ar[i] == val:
                count_occ += 1
        return count_occ
    
    """
    BELOW ITS ONLY LEVEL 2 ARRAY/LIST PROBLEMS
    """    
    def oddNumbers(self):
        return [x for x in self.ar if x %2 != 0]
    
    def Distinct(self):
        ret_ar = self.ar.copy()
        for k in range(0,len(ret_ar)):
            for j in range(0,len(ret_ar)):
                if ret_ar[k] == ret_ar[j] and k < j:
                    ret_ar.pop(j)
        return ret_ar
    
    def isSorted(self):
