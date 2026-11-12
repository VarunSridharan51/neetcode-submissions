class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_count_dict = dict(Counter(s))
        t_count_dict = dict(Counter(t))

        s_len = len(s)
        t_len = len(t)

        if s == t:
            return True

        if s_len != t_len:
            return False

        if s_count_dict == t_count_dict:
            return True
        else:
            return False