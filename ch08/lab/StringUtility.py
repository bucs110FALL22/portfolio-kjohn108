class StringUtility:
  def __init__(self, string):
    self.string = string

  def __str__(self):
    return (self.string)

  def vowels(self):
    count = 0
    for i in self.string:
      if(i=="a" or i=="e"or i=="i" or i=="o" or i=="u"):
        count = count + 1
      if (count >5):
        return "many"
      else:
        return count
        
  def bothEnds(self):
    size = len(self.string)
    if (size <= 2):
      return ""
    else:
      str = self.string[0] + self.string[1] + self.string[-2] + self.string[-1]
      return str

  def fixStart(self):
    if len(self.string)>=1:
      firstchar= self.string[0]
      for i in self.string:
        str = self.string[1:].replace(firstchar,"*")
        return self.string[0]+ str
    else:
      return""


  def asciiSum(self):
    str = 0
    for i in range(len(self.string)):
        str = str + ord(self.string[i])
    return str

  def cipher(self):
    length = len(self.string)
    new = ""
    for i in range(length):
      letter = self.string[i]
        

    
  
  

    
  