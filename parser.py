import yaml
import re

#Parsing the yaml file
#Error Handling
try:
    with open("project.yaml", 'r') as f:
        valuesYaml = yaml.load(f, Loader=yaml.FullLoader)
except FileNotFoundError:   
    print("ERROR: Yaml file not found!")
    exit()


#Storing all teams in a list
members= valuesYaml['teams']

# Iterating over the list of teams
print("                                    Project Name : "+valuesYaml['name'])
print("************************************************************************************************************************")
for item in members:
    info=item['members']
    # Iterating over the list of valid members (non empty)
    for mail in info:
        bmwmail=mail['mail']
        role= mail['role']
        #BMW Mail Validation
        if re.search("@bm(w|w|w).de$", bmwmail):
            print("Team name= "+item['name'])
            print("Team Email= "+bmwmail)
            print("Team Role=" +role)
            print("==================================================")



