import main


def person_phone_lowest_wattage(list1):
    for i in range(len(list1)):
        if i==0:
            lowest_value=list1[i].phone
        elif lowest_value == 0:
            lowest_value = list1[i].phone
        elif list1[i].phone < lowest_value and list1[i].phone != 0:
            lowest_value=list1[i].phone
    return lowest_value
def person_phone_highest_wattage(list1):
    for i in range(len(list1)):
        if i==0:
            highest_value=list1[i].phone
        elif list1[i].phone>highest_value:
            highest_value=list1[i].phone
    return highest_value
def person_laptop_lowest_wattage(list1):
    for i in range(len(list1)):
        if i==0:
            lowest_value=list1[i].laptop
        elif lowest_value == 0:
            lowest_value = list1[i].laptop
        elif list1[i].laptop < lowest_value and list1[i].laptop != 0:
            lowest_value=list1[i].laptop
    return lowest_value
def person_laptop_highest_wattage(list1):
    for i in range(len(list1)):
        if i == 0:
            highest_value = list1[i].laptop
        elif list1[i].laptop > highest_value:
            highest_value = list1[i].laptop
    return highest_value
def person_ipad_lowest_wattage(list1):
    for i in range(len(list1)):
        if i==0:
            lowest_value=list1[i].ipad
        elif lowest_value == 0:
            lowest_value = list1[i].ipad
        elif list1[i].ipad<lowest_value and list1[i].ipad!=0:
            lowest_value=list1[i].ipad
    return lowest_value
def person_ipad_highest_wattage(list1):
    for i in range(len(list1)):
        if i == 0:
            highest_value = list1[i].ipad
        elif list1[i].ipad > highest_value:
            highest_value = list1[i].ipad
    return highest_value
def person_airpods_lowest_wattage(list1):
    for i in range(len(list1)):
        if i==0:
            lowest_value=list1[i].airpods
        elif lowest_value == 0:
            lowest_value = list1[i].airpods
        elif list1[i].airpods < lowest_value and list1[i].airpods != 0:
            lowest_value=list1[i].airpods
    return lowest_value
def person_airpods_highest_wattage(list1):
    for i in range(len(list1)):
        if i == 0:
            highest_value = list1[i].airpods
        elif list1[i].airpods > highest_value:
            highest_value = list1[i].airpods
    return highest_value
def lowest_device(list1):
    lowest_phone=person_phone_lowest_wattage(list1)
    lowest_laptop=person_laptop_lowest_wattage(list1)
    lowest_ipad=person_ipad_lowest_wattage(list1)
    lowest_airpods=person_airpods_lowest_wattage(list1)
    lowest_device_list=[lowest_phone,lowest_laptop,lowest_ipad,lowest_airpods]

    for i in range(len(lowest_device_list)):
        if i==0:
            lowest_value=lowest_device_list[i]
        elif lowest_device_list[i]<lowest_value:
            lowest_value=lowest_device_list[i]
    return lowest_value

def highest_device(list1):
    highest_phone = person_phone_highest_wattage(list1)
    highest_laptop = person_laptop_highest_wattage(list1)
    highest_ipad = person_ipad_highest_wattage(list1)
    highest_airpods = person_airpods_highest_wattage(list1)
    highest_device_list = [highest_phone, highest_laptop, highest_ipad, highest_airpods]

    for i in range(len(highest_device_list)):
        if i == 0:
            highest_value = highest_device_list[i]
        elif highest_device_list[i] > highest_value:
            highest_value = highest_device_list[i]
    return highest_value

# This function converts minutes to hours
def conversion_to_hour(number):
    conversion = number // 60 + number % 60 / 60
    return conversion


# This function calculates total wattage used by each person
def total_wattage_used(list1):
    total_wattage = 0
    wattage_list = []

    for i in range(len(list1)):
        total_wattage += list1[i].phone * conversion_to_hour(list1[i].average_phone_charging_time) * list1[i].average_phone_charging_frequency
        total_wattage += list1[i].laptop * conversion_to_hour(list1[i].average_laptop_charging_time) * list1[i].average_laptop_charging_frequency
        total_wattage += list1[i].ipad * conversion_to_hour(list1[i].average_ipad_charging_time) * list1[i].average_ipad_charging_frequency
        total_wattage += list1[i].airpods * conversion_to_hour(list1[i].average_airpods_charging_time) * list1[i].average_airpods_charging_frequency
        wattage_list.append(int(total_wattage))
        total_wattage = 0

    return wattage_list


# This function sums all wattages in a list
def all_wattage(list1):
    total_wattage_number = 0
    for i in list1:
        total_wattage_number += i
    return total_wattage_number


# This function calculates total electricity cost in a year
def total_costs_in_a_year(number):
    total_electricity_cost = int(number * 0.000316 * 365)
    return total_electricity_cost


# This function categorizes usage based on wattage thresholds
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

def verdict(surveyed_data,total_wattaged_used):
    verdict_list=[]
    for i in range(len(total_wattaged_used)):
        if total_wattaged_used[i]>1500:
            verdict_list.append(surveyed_data[i].name)
    return verdict_list

def prediction(list1):
    total_wattage = total_wattage_used(list1)
    all_watts = all_wattage(total_wattage)
    total_cost = total_costs_in_a_year(all_watts)
    total_population=5500
    predicted_result=total_cost*total_population//len(list1)
    return predicted_result

#This function gives the final verdict, if over 50% of the people are using high amounts of electrcitiy, it will say, otherwise, it will say that most ofo the students are using normal amounts of electricity
def final_verdict(list1):
   counter=0
   for i in list1:
       if i>1500:
           counter+=1
   if counter>=len(list1)//2:
       the_verdict="Most of the students have high electricity usage in the dorm"
   else:
       the_verdict="Most of the students are not overusing their electricity"
   return the_verdict

def ways_to_improve():
    return " 1. Unplug devices when not in use (chargers, speakers, etc.).\n 2. Use a power strip and switch it off at night—super convenient for shutting everything down at once. \n 3. Avoid leaving laptops plugged in at 100%; charge to ~80–90%, then unplug."

# This function summarizes the survey results
def summary(list1):
   lowest_watt_hour=lowest_device(list1)
   highest_watt_hour=highest_device(list1)
   total_wattage = total_wattage_used(list1)
   all_watts = all_wattage(total_wattage)
   total_cost = total_costs_in_a_year(all_watts)
   predicted=prediction(list1)
   final_verdict_result = final_verdict(total_wattage)
   verdict_list=verdict(list1, total_wattage)
   improvement=ways_to_improve()
   return (
           "Number of Calpoly Dormmates in Survey: " + str(len(list1)) + "\n"
           "Lowest Device Watt Hour: "+str(lowest_watt_hour)+" Wh\n"
            "Highest Device Watt Hour: "+str(highest_watt_hour)+" Wh\n"
           "Total amount of electricity that they used: " + str(all_watts) + " watts \n"
           "Total Cost used by these individuals in a year: " + str(total_cost) + " dollars \n"
           "Assuming that there is 5500 freshmen at Calpoly, the total cost for the entire year for all the freshmens will be: " +str(predicted)+" dollars\n"
           "Final Verdict : " + str(final_verdict_result) + "\n"
           "However, " + str(verdict_list) + " need(s) to cut down on their electricity usage" +"\n"
           "\nSome tips include for saving power include: "+ "\n"+improvement
   )






