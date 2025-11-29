import unittest
import function
import main



surveyed_data=[
       main.Person(
           "Adrian",
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
           "Adam",
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
           "Ramses",
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
           "Bella",
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
           "Chris",
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
           "Diana",
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
           "Ethan",
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
           "Fiona",
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
           "Douglas",
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
           "Hannah",
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
           "Ian",
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
           "Julia",
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
reduced_surveyed_data=[
main.Person(
    "Adrian",
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
    "Bella",
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
    "Chris",
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
    "Diana",
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
    "Fiona",
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
    "Hannah",
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
    "Ian",
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
    "Julia",
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


results={"Minimum":"This Person has used minimal amount of electricity which is good as it can save electricity bills",
         "Medium":"This Person has used the medium amount of electricity, which is alright in saving electricity bills",
         "High":"This Person has used high amount of electricity, which is not good in saving electricity bills"}


class TestCases(unittest.TestCase):
    def test_lowest_wattage_hour_filter_1(self):
        result=function.lowest_wattage_hour_filter(surveyed_data)
        expected=[7.1, 69.6, 19.3, 0.09]
        self.assertEqual(expected,result)
    def test_lowest_wattage_hour_filter_2(self):
        result = function.lowest_wattage_hour_filter(reduced_surveyed_data)
        expected = [7.1, 250, 28.9, 0.09]
        self.assertEqual(expected, result)


    def test_highest_wattage_hour_filter_1(self):
        result=function.highest_wattage_hour_filter(surveyed_data)
        expected=[650, 38.99, 1.52]
        self.assertEqual(expected,result)
    def test_highest_wattage_hour_filter_2(self):
        result = function.highest_wattage_hour_filter(reduced_surveyed_data)
        expected = [650, 32.4, 0.18]
        self.assertEqual(expected, result)


    def test_lowest_device_1(self):
        result=function.lowest_device(surveyed_data)
        expected=0.09
        self.assertEqual(expected,result)
    def test_lowest_device_2(self):
        result=function.lowest_device(reduced_surveyed_data)
        expected=0.09
        self.assertEqual(expected,result)


    def test_highest_device_1(self):
        result=function.highest_device(surveyed_data)
        expected=650
        self.assertEqual(expected,result)
    def test_highest_device_2(self):
        result=function.highest_device(reduced_surveyed_data)
        expected=650
        self.assertEqual(expected,result)

    def test_conversion_to_hour_1(self):
        result=function.conversion_to_hour(30)
        expected=0.5
        self.assertEqual(expected,result)
    def test_conversion_to_hour_2(self):
        result=function.conversion_to_hour(120)
        expected=2
        self.assertEqual(expected,result)

    def test_total_wattage_used_1(self):
       result=function.total_wattage_used(surveyed_data)
       expected=[1537, 87, 106, 61, 2651, 2731, 39, 2, 249, 41, 50, 73]
       self.assertEqual(expected,result)
    def test_total_wattage_used_2(self):
       result=function.total_wattage_used(reduced_surveyed_data)
       expected=[1537, 61, 2651, 2731, 2, 41, 50, 73]
       self.assertEqual(expected,result)


    def test_all_wattage_1(self):
        wattage_list=function.total_wattage_used(surveyed_data)
        result=function.all_wattage(wattage_list)
        expected=7627
        self.assertEqual(expected,result)
    def test_all_wattage_2(self):
        wattage_list=function.total_wattage_used(reduced_surveyed_data)
        result=function.all_wattage(wattage_list)
        expected=7146
        self.assertEqual(expected,result)

    def test_total_cost_in_a_year_1(self):
        wattage_list = function.total_wattage_used(surveyed_data)
        total_wattage_number=function.all_wattage(wattage_list)
        result=function.total_costs_in_a_year(total_wattage_number)
        expected=879
        self.assertEqual(expected,result)
    def test_total_cost_in_a_year_2(self):
        wattage_list = function.total_wattage_used(reduced_surveyed_data)
        total_wattage_number=function.all_wattage(wattage_list)
        result=function.total_costs_in_a_year(total_wattage_number)
        expected=824
        self.assertEqual(expected,result)

    def testing_results_1(self):
       wattage_list = function.total_wattage_used(surveyed_data)
       result=function.the_results(wattage_list,results)
       expected=['This Person has used high amount of electricity, which is not good in saving '
 'electricity bills',
 'This Person has used minimal amount of electricity which is good as it can '
 'save electricity bills',
 'This Person has used minimal amount of electricity which is good as it can '
 'save electricity bills',
 'This Person has used minimal amount of electricity which is good as it can '
 'save electricity bills',
 'This Person has used high amount of electricity, which is not good in saving '
 'electricity bills',
 'This Person has used high amount of electricity, which is not good in saving '
 'electricity bills',
 'This Person has used minimal amount of electricity which is good as it can '
 'save electricity bills',
 'This Person has used minimal amount of electricity which is good as it can '
 'save electricity bills',
 'This Person has used the medium amount of electricity, which is alright in '
 'saving electricity bills',
 'This Person has used minimal amount of electricity which is good as it can '
 'save electricity bills',
 'This Person has used minimal amount of electricity which is good as it can '
 'save electricity bills',
 'This Person has used minimal amount of electricity which is good as it can '
 'save electricity bills']
       self.assertEqual(expected,result)

    def testing_the_results_2(self):
       wattage_list = function.total_wattage_used(reduced_surveyed_data)
       result = function.the_results(wattage_list, results)
       expected = ['This Person has used high amount of electricity, which is not good in saving '
 'electricity bills',
 'This Person has used minimal amount of electricity which is good as it can '
 'save electricity bills',
 'This Person has used high amount of electricity, which is not good in saving '
 'electricity bills',
 'This Person has used high amount of electricity, which is not good in saving '
 'electricity bills',
 'This Person has used minimal amount of electricity which is good as it can '
 'save electricity bills',
 'This Person has used minimal amount of electricity which is good as it can '
 'save electricity bills',
 'This Person has used minimal amount of electricity which is good as it can '
 'save electricity bills',
 'This Person has used minimal amount of electricity which is good as it can '
 'save electricity bills']
       self.assertEqual(expected,result)


    def test_prediction_1(self):
        result=function.prediction(surveyed_data)
        expected=402875
        self.assertEqual(expected,result)
    def test_prediction_2(self):
        result=function.prediction(reduced_surveyed_data)
        expected=566500
        self.assertEqual(expected,result)

    def test_final_verdict_1(self):
        wattage_list = function.total_wattage_used(surveyed_data)
        result=function.final_verdict(wattage_list)
        expected="Most of the students are not overusing their electricity"
        self.assertEqual(expected,result)
    def test_final_verdict_2(self):
        wattage_list = function.total_wattage_used(reduced_surveyed_data)
        result=function.final_verdict(wattage_list)
        expected="Most of the students are not overusing their electricity"
        self.assertEqual(expected,result)

    def test_ways_to_improve_1(self):
        result=function.ways_to_improve()
        expected=(" 1. Unplug devices when not in use (chargers, speakers, etc.).\n"
       " 2. Use a power strip and switch it off at night—super convenient for shutting everything down at once. \n"
       " 3. Avoid leaving laptops plugged in at 100%; charge to ~80–90%, then unplug.")
        self.assertEqual(expected,result)
    def test_ways_to_improve_2(self):
        result=function.ways_to_improve()
        expected=(" 1. Unplug devices when not in use (chargers, speakers, etc.).\n"
       " 2. Use a power strip and switch it off at night—super convenient for shutting everything down at once. \n"
       " 3. Avoid leaving laptops plugged in at 100%; charge to ~80–90%, then unplug.")
        self.assertEqual(expected,result)

    def test_summary_1(self):
       result=function.summary(surveyed_data)
       expected=(
       "Number of Calpoly Dormmates in Survey: 12\n"
       "Lowest Device Watt Hour: 0.09 Wh\n"
       "Highest Device Watt Hour: 650 Wh\n"
       "Total amount of electricity that they used in a day: 7627 watts \n"
       "Total Cost used by these individuals in a year: 879 dollars \n"
       "Assuming that there is 5500 freshmen at Calpoly, the total cost for the entire year for all the freshmen will be: 402875 dollars\n"
       "Final Verdict : Most of the students are not overusing their electricity\n"
       "However, ['Adrian', 'Chris', 'Diana'] need(s) to cut down on their electricity usage\n"
       "\n"
       "Some tips for saving power include: \n"
       " 1. Unplug devices when not in use (chargers, speakers, etc.).\n"
       " 2. Use a power strip and switch it off at night—super convenient for shutting everything down at once. \n"
       " 3. Avoid leaving laptops plugged in at 100%; charge to ~80–90%, then unplug."
       )

       self.assertEqual(expected,result)
    def test_summary_2(self):
       result=function.summary(reduced_surveyed_data)
       expected=(
       "Number of Calpoly Dormmates in Survey: 8\n"
       "Lowest Device Watt Hour: 0.09 Wh\n"
       "Highest Device Watt Hour: 650 Wh\n"
       "Total amount of electricity that they used in a day: 7146 watts \n"
       "Total Cost used by these individuals in a year: 824 dollars \n"
       "Assuming that there is 5500 freshmen at Calpoly, the total cost for the entire year for all the freshmen will be: 566500 dollars\n"
       "Final Verdict : Most of the students are not overusing their electricity\n"
       "However, ['Adrian', 'Chris', 'Diana'] need(s) to cut down on their electricity usage\n"
       "\n"
       "Some tips for saving power include: \n"
       " 1. Unplug devices when not in use (chargers, speakers, etc.).\n"
       " 2. Use a power strip and switch it off at night—super convenient for shutting everything down at once. \n"
       " 3. Avoid leaving laptops plugged in at 100%; charge to ~80–90%, then unplug."
       )

       self.assertEqual(expected,result)


#This portion saves the function summary output into a new text file
output_file_path = 'summary_output.txt'
try:
    with open(output_file_path, 'w') as f:
        f.write(function.summary(surveyed_data))
    print("\n"+f"Successfully saved results to {output_file_path}")
except:
    print("Error saving file")




