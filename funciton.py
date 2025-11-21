import main

# This function when given an electronic device from Person Object, returns the total_charging time per day
# Input: dict[str. float]
# Output: float
# Ex Input: Person[iphone, 5] it takes 5 hours for this Person to charge their phones
# Ex Output: Compares it to the total_charging_time of the device

def phone_charging_time(dict_phone: dict[str, float], phone_key:str) -> list[float]:
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


if__name__ = "__main()__"
