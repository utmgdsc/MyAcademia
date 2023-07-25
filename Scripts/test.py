import json

with open('aggregated_programs.json', 'r') as f:
    l=[]
    data = json.load(f)
    for program in data:
        for req in data[program]['detailAssessments']:
            l.append(data[program]['detailAssessments'][req]['type'])
    print(set(l))


