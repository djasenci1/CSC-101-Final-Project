import main
#Problem Statement:  Energy consumption from college students is often overlooked, but the dorm’s electricity is a significant part
# of the campus’s power demand. The purpose of this project is to bring awareness on the large amount of electricity we are using within
# our dorms, motivating us to find ways to cut down on such usage.




#This function filters out the lowest wattage hour for the four different devices (phone, laptop, ipad, airpod)
def lowest_wattage_hour_filter(surveyed_data):
    lowest_filter=[]

    for i in range(len(surveyed_data)):
        if i==0:
            lowest_phone_value=surveyed_data[i].phone
        elif lowest_phone_value == 0:
            lowest_phone_value = surveyed_data[i].phone
        elif surveyed_data[i].phone < lowest_phone_value and surveyed_data[i].phone != 0:
            lowest_phone_value=surveyed_data[i].phone
    lowest_filter.append(lowest_phone_value)

    for j in range(len(surveyed_data)):
        if j == 0:
            lowest_laptop_value = surveyed_data[j].laptop
        elif lowest_laptop_value == 0:
            lowest_laptop_value = surveyed_data[j].laptop
        elif surveyed_data[j].laptop < lowest_laptop_value and surveyed_data[j].laptop != 0:
            lowest_laptop_value = surveyed_data[j].laptop
    lowest_filter.append(lowest_laptop_value)

    for k in range(len(surveyed_data)):
        if k==0:
            lowest_ipad_value=surveyed_data[k].ipad
        elif lowest_ipad_value == 0:
            lowest_ipad_value = surveyed_data[k].ipad
        elif surveyed_data[k].ipad<lowest_ipad_value and surveyed_data[k].ipad!=0:
            lowest_ipad_value=surveyed_data[k].ipad
    lowest_filter.append(lowest_ipad_value)

    for l in range(len(surveyed_data)):
        if l == 0:
            lowest_airpods_value = surveyed_data[l].airpods
        elif lowest_airpods_value == 0:
            lowest_airpods_value = surveyed_data[l].airpods
        elif surveyed_data[l].airpods < lowest_airpods_value and surveyed_data[l].airpods != 0:
            lowest_airpods_value = surveyed_data[l].airpods
    lowest_filter.append(lowest_airpods_value)
    return lowest_filter

#This function filters out the highest wattage hour for the four different devices (phone, laptop, ipad, airpod)
def highest_wattage_hour_filter(surveyed_data):
    highest_filter=[]

    for i in range(len(surveyed_data)):
        if i == 0:
            highest_phone_value = surveyed_data[i].phone
        elif surveyed_data[i].phone > highest_phone_value:
            highest_phone_value = surveyed_data[i].phone

    for j in range(len(surveyed_data)):
        if j == 0:
            highest_laptop_value = surveyed_data[j].laptop
        elif surveyed_data[j].laptop > highest_laptop_value:
            highest_laptop_value = surveyed_data[j].laptop
    highest_filter.append(highest_laptop_value)

    for k in range(len(surveyed_data)):
        if k == 0:
            highest_ipad_value = surveyed_data[k].ipad
        elif surveyed_data[k].ipad > highest_ipad_value:
            highest_ipad_value = surveyed_data[k].ipad
    highest_filter.append(highest_ipad_value)

    for l in range(len(surveyed_data)):
        if l == 0:
            highest_airpods_value = surveyed_data[l].airpods
        elif surveyed_data[l].airpods > highest_airpods_value:
            highest_airpods_value = surveyed_data[l].airpods
    highest_filter.append(highest_airpods_value)
    return highest_filter

#This function goes through the lowest value of each device and compares them, outputing the real lowest device wattage
def lowest_device(surveyed_data):
    lowest_device_list=lowest_wattage_hour_filter(surveyed_data)

    for i in range(len(lowest_device_list)):
        if i==0:
            lowest_value=lowest_device_list[i]
        elif lowest_device_list[i]<lowest_value:
            lowest_value=lowest_device_list[i]
    return lowest_value
#This function goes through the highest value of each device and compares them, outputing the real highest device wattage
def highest_device(surveyed_data):
    highest_device_list = highest_wattage_hour_filter(surveyed_data)

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
def total_wattage_used(surveyed_data):
    total_wattage = 0
    wattage_list = []


    for i in range(len(surveyed_data)):
        phone_charging_time = conversion_to_hour(surveyed_data[i].average_phone_charging_time) * surveyed_data[i].average_phone_charging_frequency
        laptop_charging_time=conversion_to_hour(surveyed_data[i].average_laptop_charging_time) * surveyed_data[i].average_laptop_charging_frequency
        ipad_charging_time=conversion_to_hour(surveyed_data[i].average_ipad_charging_time) * surveyed_data[i].average_ipad_charging_frequency
        airpods_charging_time=conversion_to_hour(surveyed_data[i].average_airpods_charging_time) * surveyed_data[i].average_airpods_charging_frequency

        if phone_charging_time!=0:
            total_wattage += surveyed_data[i].phone/phone_charging_time
        if laptop_charging_time!=0:
            total_wattage += surveyed_data[i].laptop/laptop_charging_time
        if ipad_charging_time!=0:
            total_wattage += surveyed_data[i].ipad/ipad_charging_time
        if airpods_charging_time!=0:
            total_wattage += surveyed_data[i].airpods/airpods_charging_time
        wattage_list.append(int(total_wattage))
        total_wattage = 0

    return wattage_list


# This function sums all wattages in a list
def all_wattage(total_wattage_used):
    total_wattage_number = 0
    for i in total_wattage_used:
        total_wattage_number += i
    return total_wattage_number


# This function calculates total electricity cost in a year
def total_costs_in_a_year(all_wattage):
    total_electricity_cost = int(all_wattage * 0.000316 * 365)
    return total_electricity_cost


# This function categorizes usage based on wattage thresholds
def the_results(total_wattage_used, result_messages):
    the_result = []
    for i in total_wattage_used:
        if i > 1500:
            the_result.append(result_messages["High"])
        elif i > 150:
            the_result.append(result_messages["Medium"])
        else:
            the_result.append(result_messages["Minimum"])

    return the_result

#This function identifies the individuals who are using more electricity than needed
def verdict(surveyed_data,the_result):
    verdict_list=[]
    for i in range(len(the_result)):
        if the_result[i]=='This Person has used high amount of electricity, which is not good in saving electricity bills':
            verdict_list.append(surveyed_data[i].name)
    return verdict_list

#This function predicts how much money the school would have to pay every year for freshmen assuming that there are only 5500 freshmens
def prediction(surveyed_data):
    total_wattage = total_wattage_used(surveyed_data)
    all_watts = all_wattage(total_wattage)
    total_cost = total_costs_in_a_year(all_watts)
    total_freshmen_population=5500
    predicted_result=total_cost*total_freshmen_population//len(surveyed_data)
    return predicted_result

#This function gives the final verdict, if over 50% of the people are using high amounts of electrcitiy, it will say:
# "Most of the students have high electricity usage in the dorm", otherwise, it will say:
#"Most of the students are not overusing their electricity"
def final_verdict(surveyed_data):
   counter=0
   for i in surveyed_data:
       if i>1500:
           counter+=1
   if counter>=len(surveyed_data)//2:
       the_verdict="Most of the students have high electricity usage in the dorm"
   else:
       the_verdict="Most of the students are not overusing their electricity"
   return the_verdict

def ways_to_improve():
    return " 1. Unplug devices when not in use (chargers, speakers, etc.).\n 2. Use a power strip and switch it off at night, super convenient for shutting everything down at once. \n 3. Avoid leaving laptops plugged in at 100%; charge to 80% to 90%, then unplug."

# This function summarizes the survey results and returns a string value with all the information we've gathered
def summary(surveyed_data,result_message):
   lowest_watt_hour=lowest_device(surveyed_data)
   highest_watt_hour=highest_device(surveyed_data)
   total_wattage = total_wattage_used(surveyed_data)
   all_watts = all_wattage(total_wattage)
   total_cost = total_costs_in_a_year(all_watts)
   predicted=prediction(surveyed_data)
   final_verdict_result = final_verdict(total_wattage)
   results=the_results(total_wattage,result_message)
   verdict_list=verdict(surveyed_data, results)
   improvement=ways_to_improve()
   return (
           "Number of Calpoly Dormmates in Survey: " + str(len(surveyed_data)) + "\n"
           "Lowest Device Watt Hour: "+str(lowest_watt_hour)+" Wh\n"
            "Highest Device Watt Hour: "+str(highest_watt_hour)+" Wh\n"
           "Total amount of electricity that they used in a day: " + str(all_watts) + " watts \n"
           "Total Cost used by these individuals in a year: " + str(total_cost) + " dollars \n"
           "Assuming that there is 5500 freshmen at Calpoly, the total cost for the entire year for all the freshmen will be: " +str(predicted)+" dollars\n"
           "Final Verdict : " + str(final_verdict_result) + "\n"
           "However, " + str(verdict_list) + " need(s) to cut down on their electricity usage" +"\n"
           "\nSome tips for saving power include: "+ "\n"+improvement
   )

#Reflection on the social responsibility aspect of your project:
#Through this project we were able to learn a lot about approximately how much electricity freshmen have used and approximately how much money that amount of electricity equates to. We hope our project shows how students can improve their electricity usage by being more aware of how much money they are spending from electricity.





