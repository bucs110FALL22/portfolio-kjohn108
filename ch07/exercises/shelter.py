import time


class Animal: 
  def _init_(self, name, type):
    self.id = time.strftime("%d%m%M%S")
    #self.id = self(id)
    #self.id = uuid()
    self.name = name
    self.type = type
    self.arrived = time.strftime("%d%m%M%S")
    self.adopted = None
    
  def set_adopted(self):
    self.adopted = time.strftime("%d%m%M%S")

  def __str__():
    result_str = F''


def main():
  fido = Animal("fido","dog")
  fido.set_adopted()
  print(fido)
  

