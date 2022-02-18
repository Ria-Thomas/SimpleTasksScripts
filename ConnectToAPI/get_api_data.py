import requests
import json

# Use requests.get to access an API link: Sample API given here
response_api = requests.get("https://services1.arcgis.com/xeMpV7tU1t4KD3Ei/arcgis/rest/services/BC_COVID19_Dashboard_Case_Details_Production/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json")

data = response_api.text
# Parse the data into json
parse_json = json.loads(data)
# Gets a specific portion of the JSON. In this example 'features'
df = pd.json_normalize(parse_json['features'])
