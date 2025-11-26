import unittest
import function
import main
from function import all_wattage, total_wattage_used
from main import Person

# Surveyed data of dormmates
surveyed_data = [
    main.Person("Adam", 13.6, 300, 0, 0, 11, 12, 0, 0, 2, 1, 0, 0),
    main.Person("Jack", 12.41, 69.6, 0, 1.52, 18, 27, 12, 0, 4, 2, 0, 1),
    main.Person("Ramses", 13.66, 300, 31.29, 0, 30, 30, 18, 0, 20, 6, 20, 0),
    main.Person("Bella", 12.41, 250, 31.29, 0.18, 32, 31, 1, 0, 25, 8, 0, 1),
    main.Person("Chris", 13.7, 650, 0, 0.15, 16, 15, 0, 1, 1, 1, 0, 0),
    main.Person("Diana", 10.78, 400, 32.4, 0, 10, 9, 0, 0, 1, 1, 0, 0),
    main.Person("Ethan", 12.7, 320, 19.3, 0.18, 27, 31, 1, 1, 10, 17, 0, 0),
    main.Person("Fiona", 7.1, 0, 0, 0.09, 24, 24, 0, 0, 6, 1, 0, 0),
    main.Person("George", 12.0, 450, 38.99, 0.18, 21, 22, 1, 0, 9, 5, 0, 0),
    main.Person("Hannah", 11.9, 300, 28.9, 0, 15, 39, 0, 0, 2, 26, 0, 0),
    main.Person("Ian", 11.2, 500, 31.29, 0.09, 33, 38, 0, 1, 20, 16, 0, 0),
    main.Person("Julia", 13.0, 350, 0, 0.18, 39, 41, 0, 0, 26, 7, 0, 0)
]

# Result messages for testing
results = {
    "Minimum": "This Person has used minimal amount of electricity which is good as it can save electricity bills",
    "Medium": "This Person has used the medium amount of electricity, which is alright in saving electricity bills",
    "High": "This Person has used high amount of electricity, which is not good in saving electricity bills"
}


class TestCases(unittest.TestCase):
    maxDiff = None  # Show full diff for long string comparisons

    # Test phone kilo wattage comparison
    def test_person_phone_kilo_watts_comparison(self):
        result = function.person_phone_kilo_watts_comparison(surveyed_data, 11)
        expected = "[name Diana, phone 10.78, laptop 400, ipad 32.4, airpods 0,\n name Fiona, phone 7.1, laptop 0, ipad 0, airpods 0.09]"
        self.assertEqual(expected, result)

    # Test laptop kilo wattage comparison
    def test_person_laptop_kilo_watts_comparison(self):
        result = function.person_laptop_kilo_watts_comparison(surveyed_data, 50)
        expected = "[name Fiona, phone 7.1, laptop 0, ipad 0, airpods 0.09]"
        self.assertEqual(expected, result)

    # Test ipad kilo wattage comparison
    def test_person_ipad_kilo_watts_comparison(self):
        result = function.person_ipad_kilo_watts_comparison(surveyed_data, 10)
        expected = "[name Adam, phone 13.6, laptop 300, ipad 0, airpods 0,\n name Jack, phone 12.41, laptop 69.6, ipad 0, airpods 1.52,\n name Chris, phone 13.7, laptop 650, ipad 0, airpods 0.15,\n name Fiona, phone 7.1, laptop 0, ipad 0, airpods 0.09,\n name Julia, phone 13.0, laptop 350, ipad 0, airpods 0.18]"
        self.assertEqual(expected, result)

    # Test airpods kilo wattage comparison
    def test_person_airpods_kilo_watts_comparison(self):
        result = function.person_airpods_kilo_watts_comparison(surveyed_data, 0.20)
        expected = "[name Adam, phone 13.6, laptop 300, ipad 0, airpods 0,\n name Ramses, phone 13.66, laptop 300, ipad 31.29, airpods 0,\n name Bella, phone 12.41, laptop 250, ipad 31.29, airpods 0.18,\n name Chris, phone 13.7, laptop 650, ipad 0, airpods 0.15,\n name Diana, phone 10.78, laptop 400, ipad 32.4, airpods 0,\n name Ethan, phone 12.7, laptop 320, ipad 19.3, airpods 0.18,\n name Fiona, phone 7.1, laptop 0, ipad 0, airpods 0.09,\n name George, phone 12.0, laptop 450, ipad 38.99, airpods 0.18,\n name Hannah, phone 11.9, laptop 300, ipad 28.9, airpods 0,\n name Ian, phone 11.2, laptop 500, ipad 31.29, airpods 0.09,\n name Julia, phone 13.0, laptop 350, ipad 0, airpods 0.18]"
        self.assertEqual(expected, result)

    # Test total wattage used
    def test_total_wattage_used(self):
        result = function.total_wattage_used(surveyed_data)
        expected = [64, 77, 1224, 1198, 166, 61, 2867, 17, 862, 5075, 5189, 1893]
        self.assertEqual(expected, result)

    # Test total cost in a year
    def test_total_cost_in_a_year(self):
        total_watts = function.all_wattage(function.total_wattage_used(surveyed_data))
        result = function.total_costs_in_a_year(total_watts)
        expected = 2156
        self.assertEqual(expected, result)

    # Test electricity usage results
    def test_testing_results(self):
        wattages = function.total_wattage_used(surveyed_data)
        result = function.testing_results(wattages, results)
        expected = [
            'This Person has used minimal amount of electricity which is good as it can save electricity bills',
            'This Person has used minimal amount of electricity which is good as it can save electricity bills',
            'This Person has used the medium amount of electricity, which is alright in saving electricity bills',
            'This Person has used the medium amount of electricity, which is alright in saving electricity bills',
            'This Person has used the medium amount of electricity, which is alright in saving electricity bills',
            'This Person has used minimal amount of electricity which is good as it can save electricity bills',
            'This Person has used high amount of electricity, which is not good in saving electricity bills',
            'This Person has used minimal amount of electricity which is good as it can save electricity bills',
            'This Person has used the medium amount of electricity, which is alright in saving electricity bills',
            'This Person has used high amount of electricity, which is not good in saving electricity bills',
            'This Person has used high amount of electricity, which is not good in saving electricity bills',
            'This Person has used high amount of electricity, which is not good in saving electricity bills'
        ]
        self.assertEqual(expected, result)

    # Test summary
    def test_summary(self):
        result = function.summary(surveyed_data)
        expected = (
            'Number of Calpoly Dormmates in Survey:',
            12,
            'Total amount of electricity that they used:',
            18693,
            'total_cost_year',
            2156,
            'Final Verdict=',
            'Most of the students are not overusing their electricity',
            'However',
            ['Ethan', 'Hannah', 'Ian', 'Julia'],
            'needs to cut down on their spending'
        )
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
