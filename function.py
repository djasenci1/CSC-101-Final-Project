import main
import test_file

# This function, when given Person Object, returns a comparison of each electronic device used by a person to the total watts.
# Input: Person1 -> phone total kWatts compare to average_charging_per_day
# Output: total Watts that's being used per day on Person1 phone
def person1_phone_average_charging_per_day(list1, value):
    new1 = []
    for x in list1:
        if x.main.Person[2] < value:
            new1.append(x)
            print("Person1 uses above average kilo watts per day")
        else:
            print("Person1 uses below average kilo watts per day")
    return new1

def conversion_to_hour(number):
   conversion=number//60+number%60/60
   return conversion

def total_wattage_used(list1):
   total_wattage=0
   wattage_list=[]
   for i in range(len(list1)):
       total_wattage+=list1[i].phone*conversion_to_hour(list1[i].average_phone_charging_time)*list1[i].average_phone_charging_frequency
       total_wattage += list1[i].laptop * conversion_to_hour(list1[i].average_laptop_charging_time)*list1[i].average_laptop_charging_frequency
       total_wattage += list1[i].ipad * conversion_to_hour(list1[i].average_ipad_charging_time) * list1[i].average_ipad_charging_frequency
       total_wattage += list1[i].airpods * conversion_to_hour(list1[i].average_airpods_charging_time) * list1[i].average_airpods_charging_frequency
       wattage_list.append(int(total_wattage))
       total_wattage=0
   return wattage_list


def all_wattage(list1):
   total_wattage_number=0
   for i in list1:
       total_wattage_number+=i
   return total_wattage_number


def total_costs_in_a_year(number):
   total_electricity_cost=int(number*0.000316*365)
   return total_electricity_cost

def testing_results(list1, result_messages):
   the_result = []
   for i in list1:
       if i > 1500:
           the_result.append(result_messages["High"])
       elif i > 150:
           the_result.append(result_messages["Medium"])
       else:
           the_result.append(result_messages["Minimum"])
   return the_result

def verdict(list1):
   counter=0
   for i in list1:
       if i>1500:
           counter+=1
   if counter>=len(list1)//2:
       the_verdict="Most of the students have high electricity usage in the dorm"
   else:
       the_verdict="Most of the students are not overusing their electricity"
   return the_verdict
def summary(list1):
   total_wattage = total_wattage_used(list1)
   all_watts = all_wattage(total_wattage)
   total_cost = total_costs_in_a_year(all_watts)
   verdict_result = verdict(total_wattage)


   return "Number of Calpoly Dormmates in Survey:", len(list1), "Total amount of electricity that they used:", all_watts, "total_cost_year",total_cost, "verdict", verdict_result












