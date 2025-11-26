import unittest
import function
import main
from function import all_wattage, total_wattage_used


surveyed_data=[
   main.Person(
       {"Adam": 18},
       13.6,
       300,
       0,
       0,
       11,
       12,
       0,
       0,
       2,
       1,
       0,
       0
   ),


   main.Person(
       {"Jack": 17},
       12.41,
       69.6,
       0,
       1.52,
       18,
       27,
       12,
       0,
       4,
       2,
       0,
       1
   ),


   main.Person(
       {"Ramses": 18},
       13.66,
       300,
       31.29,
       0,
       30,
       30,
       18,
       0,
       20,
       6,
       20,
       0
   ),


   main.Person(
       {"Bella": 19},
       12.41,
       250,
       31.29,
       0.18,
       32,
       31,
       1,
       0,
       25,
       8,
       0,
       1
   ),


   main.Person(
       {"Chris": 17},
       13.7,
       650,
       0,
       0.15,
       16,
       15,
       0,
       1,
       1,
       1,
       0,
       0
   ),


   main.Person(
       {"Diana": 19},
       10.78,
       400,
       32.4,
       0,
       10,
       9,
       0,
       0,
       1,
       1,
       0,
       0
   ),


   main.Person(
       {"Ethan": 18},
       12.7,
       320,
       19.3,
       0.18,
       27,
       31,
       1,
       1,
       10,
       17,
       0,
       0
   ),


   main.Person(
       {"Fiona": 17},
       7.1,
       0,
       0,
       0.09,
       24,
       24,
       0,
       0,
       6,
       1,
       0,
       0
   ),


   main.Person(
       {"George": 19},
       12.0,
       450,
       38.99,
       0.18,
       21,
       22,
       1,
       0,
       9,
       5,
       0,
       0
   ),


   main.Person(
       {"Hannah": 17},
       11.9,
       300,
       28.9,
       0,
       15,
       39,
       0,
       0,
       2,
       26,
       0,
       0
   ),


   main.Person(
       {"Ian": 18},
       11.2,
       500,
       31.29,
       0.09,
       33,
       38,
       0,
       1,
       20,
       16,
       0,
       0
   ),


   main.Person(
       {"Julia": 19},
       13.0,
       350,
       0,
       0.18,
       39,
       41,
       0,
       0,
       26,
       7,
       0,
       0
   )
]
results={"Minimum":"This Person has used minimal amount of electricity which is good as it can save electricity bills","Medium":"This Person has used the medium amount of electricity, which is alright in saving electricity bills","High":"This Person has used high amount of electricity, which is not good in saving electricity bills"}


class TestCases(unittest.TestCase):

    def test_person_phone_lowest_kilo_wattage(self):
        result = function.person_phone_lowest_kilo_wattage(surveyed_data,11)
        expected =  [{'Diana': 19}, 10.78, {'Fiona': 17}, 7.1]
        self.assertEqual(result, expected)

    def test_person_phone_highest_kilo_wattage(self):
        result = function.person_phone_highest_kilo_wattage(surveyed_data,11)
        expected = [{'Adam': 18}, 13.6, {'Jack': 17}, 12.41, {'Ramses': 18}, 13.66, {'Bella': 19}, 12.41, {'Chris': 17}, 13.7, {'Ethan': 18}, 12.7, {'George': 19}, 12.0, {'Hannah': 17}, 11.9, {'Ian': 18}, 11.2, {'Julia': 19}, 13.0]
        self.assertEqual(result, expected)

    def test_person_laptop_lowest_kilo_wattage(self):
        result = function.person_laptop_lowest_kilo_wattage(surveyed_data,11)
        expected = [{'Fiona': 17}, 0]
        self.assertEqual(result, expected)

    def test_person_laptop_highest_kilo_wattage(self):
        result = function.person_laptop_highest_kilo_wattage(surveyed_data,200)
        expected =  [{'Adam': 18}, 300, {'Ramses': 18}, 300, {'Bella': 19}, 250, {'Chris': 17}, 650, {'Diana': 19}, 400, {'Ethan': 18}, 320, {'George': 19}, 450, {'Hannah': 17}, 300, {'Ian': 18}, 500, {'Julia': 19}, 350]
        self.assertEqual(result, expected)





    def test_total_wattage_used(self):
       result=function.total_wattage_used(surveyed_data)
       expected=[64, 77, 1224, 1198, 166, 61, 2867, 17, 862, 5075, 5189, 1893]
       self.assertEqual(expected,result)
    def test_total_cost_in_a_year(self):
       result=function.total_costs_in_a_year(all_wattage(total_wattage_used(surveyed_data)))
       expected=2156
       self.assertEqual(expected,result)
    def testing_testing_results(self):
       result=function.testing_results(total_wattage_used(surveyed_data),results)
       expected=['This Person has used minimal amount of electricity which is good as it can '
'save electricity bills',
'This Person has used minimal amount of electricity which is good as it can '
'save electricity bills',
'This Person has used the medium amount of electricity, which is alright in '
'saving electricity bills',
'This Person has used the medium amount of electricity, which is alright in '
'saving electricity bills',
'This Person has used the medium amount of electricity, which is alright in '
'saving electricity bills',
'This Person has used minimal amount of electricity which is good as it can '
'save electricity bills',
'This Person has used high amount of electricity, which is not good in saving '
'electricity bills',
'This Person has used minimal amount of electricity which is good as it can '
'save electricity bills',
'This Person has used the medium amount of electricity, which is alright in '
'saving electricity bills',
'This Person has used high amount of electricity, which is not good in saving '
'electricity bills',
'This Person has used high amount of electricity, which is not good in saving '
'electricity bills',
'This Person has used high amount of electricity, which is not good in saving '
'electricity bills']
       self.assertEqual(expected,result)
    def test_summary(self):
       result=function.summary(surveyed_data)
       expected=('Number of Calpoly Dormmates in Survey:',
 12,
 'Total amount of electricity that they used:',
 18693,
 'total_cost_year',
 2156,
 'Final Verdict=',
 'Most of the students are not overusing their electricity',
 'However',
 [{'Ethan': 18}, {'Hannah': 17}, {'Ian': 18}, {'Julia': 19}],
 'needs to cut down on their spending')
       self.assertEqual(expected,result)

