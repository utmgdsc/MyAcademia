import json
import csv
# with open('program_data.csv', mode='w') as csv_file:
#     fieldnames = ['program_id', 'program_name', 'program_type', 'program_level', 'program_campus', 'program_department', 'program_faculty', 'program_description', 'program_requirements', 'program_notes']
#     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#     writer.writeheader()
#     with open("aggregated_programs.json", "r") as f:
#         data = json.load(f)
#         for program in data:
#             for key in data[program]:
#                 if key == 'detailAssessments':
#                     for key1 in data[program][key]:
#                         writer.writerow({'count': data[program][key][key1]['count'], 'program_name': data[program]['title']})
#                             # print(data[program][key][key1])
with open("aggregated_programs.json", "r") as f:
    data = json.load(f)
    # print(data)
    for program in data:
        if program == "ERMAJ0728":
            for key in data[program]:
                if key == 'detailAssessments':
                    for key1 in data[program][key]:
                        #print(data[program][key][key1])
                        for key2 in data[program][key][key1]:
                            print(data[program][key][key1][key2])





