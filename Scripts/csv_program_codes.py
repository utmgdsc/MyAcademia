import json
import csv
'''
Made a script that converts the json file to a csv file and returns the program id.
'''

with open('program_data.csv', mode='w') as csv_file:
    with open("aggregated_programs.json", "r") as f:
        data = json.load(f)
        # print(data)
        for program in data:
            csv_file.write(program)
            csv_file.write('\n')
