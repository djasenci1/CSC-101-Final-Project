import main

# This function, when given survey_data, returns people whose phone wattage
# is less than the given value. It returns a list alternating between
# the person's name dict and their phone wattage.
def person_phone_lowest_wattage(list1, value):
    new1 = []
    for i in range(len(list1)):
        if list1[i].phone < value:
            new1.append(list1[i].name)
            new1.append(list1[i].phone)
    return new1


# This function, when given survey_data, returns people whose phone wattage
# is greater than the given value.
def person_phone_highest_wattage(list1, value):
    new1 = []
    for i in range(len(list1)):
        if list1[i].phone > value:
            new1.append(list1[i].name)
            new1.append(list1[i].phone)
    return new1


# This function, when given survey_data, returns people whose laptop wattage
# is less than the given value.
def person_laptop_lowest_wattage(list1, value):
    new1 = []
    for i in range(len(list1)):
        if list1[i].laptop < value:
            new1.append(list1[i].name)
            new1.append(list1[i].laptop)
    return new1


# This function, when given survey_data, returns people whose laptop wattage
# is greater than the given value.
def person_laptop_highest_wattage(list1, value):
    new1 = []
    for i in range(len(list1)):
        if list1[i].laptop > value:
            new1.append(list1[i].name)
            new1.append(list1[i].laptop)
    return new1


# This function, when given survey_data, returns people whose iPad wattage
# is less than the given value.
def person_ipad_lowest_wattage(list1, value):
    new1 = []
    for i in range(len(list1)):
        if list1[i].ipad < value:
            new1.append(list1[i].name)
            new1.append(list1[i].ipad)
    return new1


# This function, when given survey_data, returns people whose iPad wattage
# is greater than the given value.
def person_ipad_highest_wattage(list1, value):
    new1 = []
    for i in range(len(list1)):
        if list1[i].ipad > value:
            new1.append(list1[i].name)
            new1.append(list1[i].ipad)
    return new1


# This function, when given survey_data, returns people whose AirPods wattage
# is less than the given value.
def person_airpods_lowest_wattage(list1, value):
    new1 = []
    for i in range(len(list1)):
        if list1[i].airpods < value:
            new1.append(list1[i].name)
            new1.append(list1[i].airpods)
    return new1


# This function, when given survey_data, returns people whose AirPods wattage
# is greater than the given value.
def person_airpods_highest_wattage(list1, value):
    new1 = []
    for i in range(len(list1)):
        if list1[i].airpods > value:
            new1.append(list1[i].name)
            new1.append(list1[i].airpods)
    return new1


# This function converts minutes to hours (as a float).
def conversion_to_hour(number):
    conversion = number // 60 + number % 60 / 60
    return conversion


# This function calculates total wattage used by each person.
# It returns a list of total wattage values (integers), one per person.
def total_wattage_used(list1):
    total_wattage = 0
    wattage_list = []

    for i in range(len(list1)):
        total_wattage += (
            list1[i].phone
            * conversion_to_hour(list1[i].average_phone_charging_time)
            * list1[i].average_phone_charging_frequency
        )
        total_wattage += (
            list1[i].laptop
            * conversion_to_hour(list1[i].average_laptop_charging_time)
            * list1[i].average_laptop_charging_frequency
        )
        total_wattage += (
            list1[i].ipad
            * conversion_to_hour(list1[i].average_ipad_charging_time)
            * list1[i].average_ipad_charging_frequency
        )
        total_wattage += (
            list1[i].airpods
            * conversion_to_hour(list1[i].average_airpods_charging_time)
            * list1[i].average_airpods_charging_frequency
        )
        wattage_list.append(int(total_wattage))
        total_wattage = 0

    return wattage_list


# This function sums all wattages in a list.
def all_wattage(list1):
    total_wattage_number = 0
    for i in list1:
        total_wattage_number += i
    return total_wattage_number


# This function calculates total electricity cost in a year
# based on total wattage and a fixed cost rate.
def total_costs_in_a_year(number):
    total_electricity_cost = int(number * 0.000316 * 365)
    return total_electricity_cost


# This function categorizes usage based on wattage thresholds.
# result_messages is a dict with keys "Minimum", "Medium", "High".
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


# This function summarizes the survey results, including total watts,
# total yearly cost, overusers, and lists of people with lowest and highest
# wattage devices (phone, laptop, iPad, AirPods).
def summary(list1):
    # Total watts and cost
    total_watts = all_wattage(total_wattage_used(list1))
    total_cost = total_costs_in_a_year(total_watts)

    # Phone stats (threshold 11 watts)
    phone_lowest = person_phone_lowest_wattage(list1, 11)
    phone_highest = person_phone_highest_wattage(list1, 11)

    # Laptop stats (lowest threshold 11 watts, highest 200 watts)
    laptop_lowest = person_laptop_lowest_wattage(list1, 11)
    laptop_highest = person_laptop_highest_wattage(list1, 200)

    # iPad stats (lowest threshold 20 watts, highest 30 watts)
    ipad_lowest = person_ipad_lowest_wattage(list1, 20)
    ipad_highest = person_ipad_highest_wattage(list1, 30)

    # AirPods stats (lowest threshold 0.09 watts, highest 1 watt)
    airpods_lowest = person_airpods_lowest_wattage(list1, 0.09)
    airpods_highest = person_airpods_highest_wattage(list1, 1)

    # Overusers (total wattage > 1500)
    wattage_list = total_wattage_used(list1)
    overusers = []
    for i in range(len(list1)):
        if wattage_list[i] > 1500:
            overusers.append(list1[i].name)

    verdict = (
        "Number of Calpoly Dormmates in Survey:",
        len(list1),
        "Total amount of electricity that they used:",
        total_watts,
        "total_cost_year",
        total_cost,
        "Final Verdict=",
        "Most of the students are not overusing their electricity",
        "However",
        overusers,
        "needs to cut down on their spending",
        "List of people with lowest wattage phone device:",
        phone_lowest,
        "List of people with highest wattage phone device:",
        phone_highest,
        "List of people with lowest wattage laptop device:",
        laptop_lowest,
        "List of people with highest wattage laptop device:",
        laptop_highest,
        "List of people with lowest wattage iPad device:",
        ipad_lowest,
        "List of people with highest wattage iPad device:",
        ipad_highest,
        "List of people with lowest wattage AirPods device:",
        airpods_lowest,
        "List of people with highest wattage AirPods device:",
        airpods_highest,
    )

    return verdict
