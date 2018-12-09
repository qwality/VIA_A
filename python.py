import json
import sys
import requests


def load_json(path):
	with open(path, "r") as j:
		return json.load(j)
		
def save_json(data, path):
	with open(path, "w") as j:
		json.dump(data, j)

def main(*args):
	data = load_json("data.json")
	#print(data)
	if(len(args) < 3):
		return 0
	
	val1 = args[1]
	val2 = args[2]
	new_entry = {"c":[{"v": val1, "f":None}, {"v": int(val2), "f":None}]}
	
	data['rows'].append(new_entry)
	r = requests.post(
		"http://www.qwality.cz/VIA_A/data.php?json=" + json.dumps(data)
	)
	print(r.text)
















if __name__ == "__main__":
	main(*sys.argv)
