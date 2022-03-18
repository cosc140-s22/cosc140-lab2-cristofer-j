from enum import Enum

class FoodCategory(Enum):
  VEGETABLE= 1
  FRUIT = 2 
  GRAIN = 3
  PROTEIN = 4
  DAIRY = 5
  OIL = 6
  OTHER =7 



class FoodItem(object):
  def __init__(self,name,category,calories):
    self.name= name
    self.category= FoodCategory(category)
    self.calories = int(calories)


  def get_name(self):
    return self.name
  def get_category(self):
    return self.category
  def calories_per_100g(self):
    return self.calories

  def __str__(self):
    return f'{self.name} ({self.category}) {self.calories}cal/100g'

class FoodServing(object):
  def __init__(self,food, amount):
    self.fooditem= food
    self.amt= int(amount)
    
  def food(self):
    return self.fooditem
    
  def amount(self):
    return self.amt
    
  def calories(self):
    return int(self.amt* (self.fooditem.calories_per_100g()/100))
    
  def __str__(self):
    return f"{self.amt}g of {self.fooditem}"
  
  

class Meal(object):
  def __init__(self):
    self.list= list()
  def addFood(self,foodserving):
    self.list.append(foodserving)
  def calories(self):
    sum=0 
    for serving in self.list:
      sum+= serving.calories()
    return int(sum)
  def __str__(self):
    result=''
    for serving in self.list:
      result+= f'{serving}\n'
    return result
  
  
    
  
  

