import sys
import json

# Interface Value for specific 

certificateId  =  sys.argv[1]
totalTextFields = sys.argv[2]

# TODO Validate both the arguments

totalTextFields = int(totalTextFields)
print (certificateId)
print (totalTextFields)

data = {}
data['properties'] = []

for i in range(0, totalTextFields, 1):
    textfield = "text " + str(i+1)
    identifier = raw_input("Enter unique Identifier for" + textfield + ": " )
    x1, y1, x2, y2 = raw_input("Enter x, y, x1, y1 for " + textfield + ": ").split(" ")
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

json_object = json.dumps(data, indent = 4) 
with open('/Users/salroid/Documents/GitHub/Dynamic-Certificate-Generator/Configs/data.json', 'w') as outfile:
    outfile.write(json_object)