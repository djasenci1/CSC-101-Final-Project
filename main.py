class Person:

   def __init__(self,
           name: str,
           phone: float,
           laptop: float,
           ipad: float,
           airpods: float,
           average_phone_charging_time: float,
           average_laptop_charging_time: float,
           average_ipad_charging_time: float,
           average_airpods_charging_time: float,
           average_phone_charging_frequency:float,
           average_laptop_charging_frequency:float,
           average_ipad_charging_frequency: float,
           average_airpods_charging_frequency:float):

       self.name = name
       self.phone = phone
       self.laptop = laptop
       self.ipad = ipad
       self.airpods = airpods

       self.average_phone_charging_time = average_phone_charging_time
       self.average_laptop_charging_time = average_laptop_charging_time
       self.average_ipad_charging_time = average_ipad_charging_time
       self.average_airpods_charging_time = average_airpods_charging_time


       self.average_phone_charging_frequency = average_phone_charging_frequency
       self.average_laptop_charging_frequency = average_laptop_charging_frequency
       self.average_ipad_charging_frequency = average_ipad_charging_frequency
       self.average_airpods_charging_frequency = average_airpods_charging_frequency

   def __repr__(self):
       return "name {}, phone {}, laptop {}, ipad {}, airpods {}".format(self.name, self.phone, self.laptop, self.ipad, self.airpods)

   def __eq__(self, other):
       return (self is other or
               type(other) == Person and
               self.name == other.name and
               self.phone == other.phone and
               self.laptop == other.laptop and
               self.ipad == other.ipad and
               self.airpods == other.airpods)

   def __str__(self):
       return f"name {self.name}, phone {self.phone}, laptop {self.laptop}, ipad {self.ipad}, airpods {self.airpods}"
