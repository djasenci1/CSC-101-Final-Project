import main
import test_file


# This function, when given Person object, it returns the person dictonary with the a lower phone kilo wattage compare to the value.
# Input: Person1 -> phone total kWatts compare to average_charging_per_day (which is the value)
# Output: total Watts that's being used per day on Person1 phone
def person_phone_kilo_watts_comparison(list1, value):
    person = []

    # find the person phone that has a lower kilo watts phone < value
    for x in list1:
        if x.phone < value:
            person.append(x)

    # make it into a str not a list (having the name of the person and phone)
    result = f"[{str(person[0])},\n {str(person[1])}]"

    return result
# This result tells us who has a phone with low kil wattage

def person_laptop_kilo_watts_comparison(list1, value):
    person = []
    for x in list1:
        if x.laptop < value:
            person.append(x)

    result = f"[{str(person[0])},\n {str(person[1])}]"
    return result
# This result tells us who has a laptop with a low kilo wattage



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





if__name__ = "__main()__"
