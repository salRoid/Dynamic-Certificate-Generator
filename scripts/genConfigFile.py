import sys
import json

# TODO Validate Plot Certificate.jpg exists if not ask to run
# TODO Validate both the arguments

certificateId  =  sys.argv[1]
totalTextFields = sys.argv[2]
totalTextFields = int(totalTextFields)

# Create Dictionary for JSON config file
data = {}
data['properties'] = []
for i in range(0, totalTextFields, 1):
    textfield = "text " + str(i+1)
    identifier = raw_input("Enter unique Identifier for" + textfield + ": " )
    x1, x2, y1, y2 = raw_input("Enter x1, x2, y1, y2 for " + textfield + ": ").split(" ")
    fontName, fontSize = raw_input("Enter font name and font size for " + textfield + ": ").split(" ")

    data['properties'].append({
    'name': identifier,
    'x1': x1,
    'y1' : y1,
    'x2': x2,
    'y2': y2,
    'fontSize': fontSize,
    'fontName' : fontName
})
# create JSON object
json_object = json.dumps(data, indent = 4, sort_keys=True) 

# create Certificate file name .json
pathConfig = '/Users/salroid/Documents/GitHub/Dynamic-Certificate-Generator/Configs/' + certificateId +  '.json'
with open(pathConfig, 'w') as outfile:
    outfile.write(json_object)