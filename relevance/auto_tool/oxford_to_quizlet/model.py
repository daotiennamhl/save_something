class Model:
  def __init__(self, i, word, de, prn, mean, *ex):
    self.i = i
    self.word = word
    self.de = de
    self.prn = prn
    self.mean = mean
    self.ex = ex
  def toString(self):
    return f'''
{self.i}. {self.word}:
{self.prn} - {self.de}
{self.mean}
- {self.ex[0]}
- {self.ex[1]}
'''