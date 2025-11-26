import main

# This function, when given survey_data, returns people with the lowest kilo wattage phone depend on if it's less than 11 kilo wattage (value)
# Intput: survey_data -> list1 and value -> 11 kilo wattage
# Output: A new dictorary of people with the lowest kilo wattage with they phone kilo_wattage displayed
def person_phone_lowest_kilo_wattage(list1, value):
    new1 = []

    for i in range(0, len(list1)):
        if  list1[i].phone < value:
             new1.append(list1[i].name)
             new1.append(list1[i].phone)

    return new1

# This function, when given survey_data, returns people with the highest kilo wattage phone depend on if it's greater than 11 kilo wattage (value)
# Intput: survey_data -> list1 and value -> 11 kilo wattage
# Output: A new dictorary of people with the lowest kilo wattage with they phone kilo_wattage displayed
def person_phone_highest_kilo_wattage(list1, value):
    new1 = []

    for i in range(0, len(list1)):
        if list1[i].phone > value:
            new1.append(list1[i].name)
            new1.append(list1[i].phone)

    return new1

# This function, when given survey_data, returns people with the lowest kilo wattage laptop depend on if it's less than 11 kilo wattage (value)
# Intput: survey_data -> list1 and value -> 11 kilo wattage
# Output: A new dictorary of people with the lowest kilo wattage with they phone kilo_wattage displayed
def person_laptop_lowest_kilo_wattage(list1, value):
    new1 = []

    for i in range(0, len(list1)):
        if list1[i].laptop < value:
            new1.append(list1[i].name)
            new1.append(list1[i].laptop)

    return new1

# This function, when given survey_data, returns people with the highest kilo wattage laptop depend on if it's greater than 11 kilo wattage (value)
# Intput: survey_data -> list1 and value -> 11 kilo wattage
# Output: A new dictorary of people with the lowest kilo wattage with they phone kilo_wattage displayed
def person_laptop_highest_kilo_wattage(list1, value):
    new1 = []

    for i in range(0, len(list1)):
        if list1[i].laptop > value:
         new1.append(list1[i].name)
         new1.append(list1[i].laptop)

    return new1

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


#This function identifies the individuals who are using High amounts of electricity
def verdict(surveyed_data,total_wattaged_used):
    verdict_list=[]
    for i in range(len(total_wattaged_used)):
        if total_wattaged_used[i]>1500:
            verdict_list.append(surveyed_data[i].name)
    return verdict_list

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

#Adam's Version of Summary:
def summary(list1):
   total_wattage = total_wattage_used(list1)
   all_watts = all_wattage(total_wattage)
   total_cost = total_costs_in_a_year(all_watts)
   final_verdict_result = final_verdict(total_wattage)
   verdict_list=verdict(list1, total_wattage)

   return ("Number of Calpoly Dormmates in Survey:", len(list1), "Total amount of electricity that they used:",
           all_watts, "total_cost_year",total_cost, "Final Verdict=", final_verdict_result,
           "However", verdict_list, "needs to cut down on their spending")

# This function summarizes the survey results
def summary2(list1):
    total_watts = all_wattage(total_wattage_used(list1))
    total_cost = total_costs_in_a_year(total_watts)

    overusers = []
    for p, watts in zip(list1, total_wattage_used(list1)):
        if watts > 1500:
            overusers.append(p.name)

    verdict = (
        "Number of Calpoly Dormmates in Survey:", len(list1),
        "Total amount of electricity that they used:", total_watts,
        "total_cost_year", total_cost,
        "Final Verdict=",
        "Most of the students are not overusing their electricity",
        "However",
        overusers,
        "needs to cut down on their spending"
    )

    return verdict
