import main
import test_file

# This function when given an electronic device from Person Object, returns the total_charging time per day
# Input: dict[str. float]
# Output: float
# Ex Input: Person[iphone, 5] it takes 5 hours for this Person to charge their phones
# Ex Output: Compares it to the total_charging_time of the device

def phone_charging_time(dict_phone: dict[str, float], phone_key: str) -> list[float]:
    new1 = []
    for x in dict_phone:
        new1.append(dict_phone[x])
    if new1 < main.Person[phone_key]: #This is the five row on the Person Object calling the total_phone_charging_time in the test_file
        total = main.Person[phone_key]
        total_1 = (new1 / total) * 100  # This gets the percentage
        print("Person uses less electricity consumption on phone by", new1)
    else:
        print("Person uses more electricity consumption on phone by", new1)
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





if__name__ = "__main()__"
