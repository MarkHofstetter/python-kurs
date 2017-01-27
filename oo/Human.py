class Human:

  def __init__(self,age = 25):
    self.age = age

  @property
  def age(self):
      return self.__age
  
  @age.setter
  def age(self, age):
      if age < 0:
          self.__age = 0
      elif age > 100:
          self.__age = 100
      else:
          self.__age = age


  @property
  def name(self):
      return self.__name

  @name.setter
  def name(self, name):
      self.__name = name

