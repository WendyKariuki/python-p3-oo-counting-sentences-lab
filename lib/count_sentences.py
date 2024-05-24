# # # #!/usr/bin/env python3
class MyString:
    def __init__(self, value=""):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if isinstance(value, str):
            self.__value = value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")

    def count_sentences(self):
      if not self.value:
          return 0 
      sentence_ends = [".", "!", "?"]
      count = 0
      prev_char = ''
      for char in self.value:
          if char in sentence_ends and prev_char not in sentence_ends:
              count += 1
          prev_char = char
      print("Intermediate count:", count)
      return count
