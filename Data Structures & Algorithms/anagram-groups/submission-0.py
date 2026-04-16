class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_dict = {}
        for ind_str in strs:
            charss = sorted(ind_str)
            sorted_chars = "".join(charss)
            
            the_list = anagram_dict.get(sorted_chars, [])
            the_list.append(ind_str)
            anagram_dict[sorted_chars] = the_list 


        ret_array = []
        for _, arrays in anagram_dict.items():
            ret_array.append(arrays)


        return ret_array