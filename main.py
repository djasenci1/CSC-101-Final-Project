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
       return ("name {}, phone {}, laptop {}, ipad {}, airpods {}, "
               "phone charging time {}, laptop charging time, {}, ipad charging time {}, "
               "airpods charging time {}, phone charging frequency {}, laptop charging frequency {}, ipad charging frequency {}, "
               "airpods charging frequency {}").format(self.name, self.phone, self.laptop, self.ipad, self.airpods, self.average_phone_charging_frequency,
                                                       self.average_laptop_charging_frequency,self.average_ipad_charging_time, self.average_airpods_charging_frequency,
                                                       self.average_phone_charging_time,self.average_laptop_charging_time,self.average_ipad_charging_time,self.average_airpods_charging_time)

   def __eq__(self, other):
       return (self is other or
               type(other) == Person and
               self.name == other.name and
               self.phone == other.phone and
               self.laptop == other.laptop and
               self.ipad == other.ipad and
               self.airpods == other.airpods and

               self.average_phone_charging_time == other.average_phone_charging_time and
               self.average_laptop_charging_time == other.average_laptop_charging_time and
               self.average_ipad_charging_time == other.average_ipad_charging_time and
               self.average_airpods_charging_time == other.average_airpods_charging_time and

               self.average_phone_charging_frequency == other.average_phone_charging_frequency and
               self.average_laptop_charging_frequency == other.average_laptop_charging_frequency and
               self.average_ipad_charging_frequency == other.average_ipad_charging_frequency and
               self.average_airpods_charging_frequency == other.average_airpods_charging_frequency)
