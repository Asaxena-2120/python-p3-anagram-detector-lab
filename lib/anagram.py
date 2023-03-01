# your code goes here!
class Anagram:
    def __init__(self,word):
        self.word=word
    def match(self,match_word_list):
        result=[]
        for word in match_word_list:
            match_word_list=[letter for letter in word]
            if sorted(match_word_list)==sorted(self.word):
                result.append(word)
        return result