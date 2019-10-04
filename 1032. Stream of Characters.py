class StreamChecker(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        # time complexity O(m * n)
        # space complexity O(m * n)
        self.dict = {}
        for word in words:
            curr_dict = self.dict
            for ch in word[::-1]:
                if ch not in curr_dict:
                    curr_dict[ch] = {}
                curr_dict = curr_dict[ch]
            curr_dict["_end_"] = True
        self.string = ""


    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """
        # time complexity O(m)
        # space complexity O(1)
        curr_dict = self.dict
        self.string = letter + self.string
        for ch in self.string:
            if ch in curr_dict:
                curr_dict = curr_dict[ch]
                if "_end_" in curr_dict:
                    return True
            else:
                break
        return False




# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

"""
StreamChecker streamChecker = new StreamChecker(["cd","f","kl"]); // init the dictionary.
streamChecker.query('a');          // return false
streamChecker.query('b');          // return false
streamChecker.query('c');          // return false
streamChecker.query('d');          // return true, because 'cd' is in the wordlist
streamChecker.query('e');          // return false
streamChecker.query('f');          // return true, because 'f' is in the wordlist
streamChecker.query('g');          // return false
streamChecker.query('h');          // return false
streamChecker.query('i');          // return false
streamChecker.query('j');          // return false
streamChecker.query('k');          // return false
streamChecker.query('l');          // return true, because 'kl' is in the wordlist
"""
