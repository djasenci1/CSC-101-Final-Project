class Person:

   def __init__(self,
           name: dict[str, float],
           phone: dict[str, float],
           laptop: dict[str, float],
           ipad: dict[str, float],
           airpods: dict[str, float],
           total_phone_charging_time: float,
           total_laptop_charging_time: float,
           total_ipad_charging_time: float,
           total_airpods_charging_time: float,
           total_phone_charging_frequency:float,
           total_laptop_charging_frequency:float,
           total_ipad_charging_frequency: float,
           total_airpods_charging_frequency:float):

       self.name = name
       self.phone = phone
       self.laptop = laptop
       self.ipad = ipad
       self.airpods = airpods

       self.total_phone_charging_time = total_phone_charging_time
       self.total_laptop_charging_time = total_laptop_charging_time
       self.total_ipad_charging_time = total_ipad_charging_time
       self.total_airpods_charging_time = total_airpods_charging_time


       self.total_phone_charging_frequency = total_phone_charging_frequency
       self.total_laptop_charging_frequency = total_laptop_charging_frequency
       self.total_ipad_charging_frequency = total_ipad_charging_frequency
       self.total_airpods_charging_frequency = total_airpods_charging_frequency

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