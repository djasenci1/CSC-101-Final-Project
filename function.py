import main

def kilo_wattage_comparsion(list1, value):
    new1 = []
    for x in list1:
        if x.phone > value:
            new1.append(x)
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


# This function summarizes the survey results
def summary(list1):
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
