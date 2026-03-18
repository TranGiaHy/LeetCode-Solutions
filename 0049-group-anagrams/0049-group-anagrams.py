class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        # Khởi tạo 
        # defaultdict(list) giúp tự động tạo sẵn một cái Giỏ rỗng (List rỗng)
        anagram_map = collections.defaultdict(list)

        # Vòng lặp quét qua từng từ (word) trong danh sách strs
        for word in strs:

            # Sắp xếp (sorted) các chữ cái theo thứ tự ABC rồi ghép lại thành 1 chuỗi.
            # Ví dụ: "eat", "tea", "ate" xếp lại thành "aet".
            signature = "".join(sorted(word))

            # Gom nhóm lại
            # Lấy từ gốc ban đầu ném vào anagram_map (nơi có signature)
            anagram_map[signature].append(word)

        # Trả về kết quả:
        # Lấy tất cả các Giỏ (các nhóm từ) ở trong sổ tay ra ngoài.
        return anagram_map.values()
        