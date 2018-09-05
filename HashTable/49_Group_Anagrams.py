#
# coding=utf-8

# 49. Group Anagrams
# 字母分组

import collections


class Solution(object):
    
    # Myway sorted+hash O(mlogm*n) O(nm)
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dct = {}
        for s in strs:
            s_sorted = ''.join(sorted(s))
            if s_sorted not in dct:
                dct[s_sorted] = [s]
            else:
                dct[s_sorted].append(s)
            
        return dct.values()
    
    # PCway sorted+hash
    def groupAnagrams2(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()
