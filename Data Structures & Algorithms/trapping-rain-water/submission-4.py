class Solution:
    def trap(self, height: List[int]) -> int:
        
        Lmax = height[0]
        Rmax = height[len(height)-1]
        
        Li = 0
        Ri = len(height) - 1

        Tw = 0

        while Li < Ri:

            if height[Li] < Lmax :
                w = abs(min(Lmax, Rmax) - height[Li]) #why li not ri?
                Tw += w
            elif (height[Ri] < Rmax):
                w = abs(min(Lmax, Rmax) - height[Ri])
                Tw += w
            
            Lmax = max(Lmax, height[Li])
            Rmax = max(Rmax, height[Ri])
                 

            if height[Li] < height[Ri]:
                    Li += 1
            else:
                    Ri -= 1

        return Tw