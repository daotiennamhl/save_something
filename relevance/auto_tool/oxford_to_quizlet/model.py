class Model:
  def __init__(self, word, prn, mean, *ex):
    self.word = word
    self.prn = prn
    self.mean = mean
    self.ex = ex
  def toString(self):
    return f'''
{self.word}:
{self.prn}
{self.mean}
- {self.ex[0]}
- {self.ex[1]}
'''