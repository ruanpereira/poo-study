
class Character:
    def __init__(self, value):
        self.__value = value
@property
def value(self):
    return self.__value
@value.setter
def value(self):
    if not isinstance(value, str):
        raise ValueError("Value must me a string")
    if not len(value) == 1:
        raise ValueError("String length must be 1")
    if not value.isalpha() and not value.isdigit():
        raise ValueError("Value must be a letter or digit")
    self.__value = value
   
    def __str__(self):
        return self.value

class Letter(Character):
    def __init__(self, value):
        self.__value = value
@property
def value(self):
    return self.__value
@value.setter
def value(self):
    if not isinstance(value, str):
        raise ValueError("Value must be a string")
    if not len(value) == 1:
        raise ValueError("String length must be 1")
    if not value.isalpha():
        raise ValueError("Value must me a letter")
    self.__value = value
    
    def __str__(self):
        return self.value
    def to_lower(self):
        return self.value.lower()
    def to_upper(self):
        return self.value.upper()

class Vowel(Letter):
    def __init__(self, value):
        self.__value = value
@property
def value(self):
    return self.__value
@value.setter
def value(self):
    if not isinstance(value, str):
        raise ValueError("Value must be a string")
    if not len(value) == 1:
        raise ValueError("String length must be 1")
    if not value.isalpha():
        raise ValueError("Value must me a letter")
    if value in ["a", 'e', "i", 'o', "u"]:
        self.__value = value
    else: 
        raise ValueError("Value must be a vowel")
        
    
    def __str__(self):
        return self.value
    def to_lower(self):
        return self.value.lower()
    def to_upper(self):
        return self.value.upper()
  
class Consonant(Letter):
     def __init__(self, value):
        self.__value = value
@property
def value(self):
    return self.__value
@value.setter
def value(self):
    if not isinstance(value, str):
        raise ValueError("Value must be a string")
    if not len(value) == 1:
        raise ValueError("String length must be 1")
    if not value.isalpha():
        raise ValueError("Value must me a letter")
    if value not in ["a", 'e', "i", 'o', "u"]:
        self.__value = value
    else: 
        raise ValueError("Value must be a consonant")
        
    
    def __str__(self):
        return self.value
    def to_lower(self):
        return self.value.lower()
    def to_upper(self):
        return self.value.upper()
 
class Digit(Character):
    def __init__(self, value):
        self.__value = value
@property
def value(self):
    return self.__value
@value.setter
def value(self):
    if not isinstance(value, str):
        raise ValueError("Value must be a string")
    if not len(value) == 1:
        raise ValueError("String length must be 1")
    if not value.isalpha():
        raise ValueError("Value must me a letter")
    if value in ["0", '1', "2", '3', "4", '5', '6', '7', '8', '9']:
        self.__value = value
    else: 
        raise ValueError("Value must be a digit")
        
    
    def __str__(self):
        return self.value
    def to_int(self):
        return int(self.value)
  

