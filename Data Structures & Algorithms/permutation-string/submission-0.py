class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        fr_map = {}
        for ch in s1:
            if ch in fr_map:
                fr_map[ch] += 1
            else:
                fr_map[ch] = 1

        for i, ch in enumerate(s2):
            if ch in fr_map:
                cp_fr_map = deepcopy(fr_map)
                while len(cp_fr_map) > 0:
                    if ch in cp_fr_map:
                        cp_fr_map[ch] -= 1
                        if cp_fr_map[ch] == 0:
                            del cp_fr_map[ch]
                    else:
                        break

                    i += 1
                    if i >= len(s2):
                        break
                    ch = s2[i]
                if len(cp_fr_map) == 0:
                    return True

        return False


        

        
        

        