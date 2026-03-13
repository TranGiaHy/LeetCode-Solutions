class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        # Dán các mảnh giấy trong word1 lại thành 1 chuỗi dài
        s1 = "".join(word1)
        
        # Dán các mảnh giấy trong word2 lại thành 1 chuỗi dài
        s2 = "".join(word2)
        
        # Nếu s1 bằng s2 thì trả về True, ngược lại False
        if s1 == s2:
            return True
        else:
            return False
        
