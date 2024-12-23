import urllib.request
import json
import time
import configparser
from datetime import datetime

SHOW_DIRECTION = False
SCREEN_WIDTH = 11

def get_config():
	'''
	Loads api key from config.ini

			Parameters:

			Returns:
				config (str): config contents
	'''
	config = configparser.ConfigParser()
	config.read('config.ini')#~/bus-tracker/bus-tracker/

	return config

def get_predictions(stops,directions):
	'''
    Quereies api and parses to find upcoming stops with the matching stops & directions.

            Parameters:
                    stops (int): A list of stop ID's
                    directions (str): List of string Direction codes either 'IB' or 'OB'

            Returns:
                    visits (str,int): List of Tuples of (str,int) formatted as [[Bus line, ETA in seconds],...]
    '''
	config_contents = get_config()
	API_KEY = str(config_contents['credentials']['api'])
	SHOW_DIRECTION = 'True' == config_contents['display']['show_direction']

	visits = []

	for stop in stops:

		dateformat = '%Y-%m-%dT%H:%M:%SZ'
		url = 'https://api.511.org/transit/StopMonitoring?'
		api_key = 'api_key=' + API_KEY
		agency = '&agency=SF'
		stopCode = '&stopCode='+str(stop)
		frmt = '&format=json'

		print(url+api_key+agency+stopCode+frmt)
		resp = urllib.request.urlopen(url+api_key+agency+stopCode+frmt)
		content = resp.read().decode('utf-8-sig').encode('utf-8')

		data = json.loads(content)

		recordedtime = datetime.strptime(data['ServiceDelivery']['StopMonitoringDelivery']['ResponseTimestamp'],dateformat)

		for stops in data['ServiceDelivery']['StopMonitoringDelivery']['MonitoredStopVisit']:
			direction = str(stops['MonitoredVehicleJourney']['DirectionRef'])
			if direction not in directions:
				continue
			line = str(stops['MonitoredVehicleJourney']['LineRef'])
			if SHOW_DIRECTION:
				line += (' ' + str(stops['MonitoredVehicleJourney']['DirectionRef']))
			expectedtime = datetime.strptime(stops['MonitoredVehicleJourney']['MonitoredCall']['ExpectedArrivalTime'],dateformat)
			timedelta = expectedtime-recordedtime

			rounded_eta = timedelta.seconds

			if timedelta.days < 10:
				visits.append([line, rounded_eta])

	return visits

def update_predictions(visits, s):
	'''
    Updates past predictions with elapsed time (s)

            Parameters:
                    visits (str,int): List of Tuples of (str,int) formatted as [[Bus line, ETA in seconds],...]
                    s (int): Time in seconds elapsed to update the prediction by

            Returns:
                    out (str): Updated list of Tuples of strings formatted as [[Bus line, ETA],...]
    '''
	out = []
	for busses in visits:
		out.append([busses[0], busses[1] - s])

	return out 


def parse_predictions(visits):
	'''
    Parse list of expected bus arrivals into displayable strings

            Parameters:
                    visits (str,int): List of Tuples of (str,int) formatted as [[Bus line, ETA in seconds],...]

            Returns:
                    incomming_busses (str): List of strings formatted as "Bus line: ETA,..."
    '''
	config_contents = get_config()
	SCREEN_WIDTH = int(config_contents['display']['screen_width'])

	route_list = []
	for routes in visits:
		if routes[0] not in route_list:
			route_list.append(routes[0])

	incomming_busses = []
	for routes in route_list:
		route_times = str(routes) + ":"
		for eta in visits:
			if eta[0] == routes and len(route_times) + 4 <= SCREEN_WIDTH:
				append_time = int(eta[1]/60)
				route_times = f"{route_times:s} {append_time:2d},"

			incomming_busses.append(route_times[:-1])

		incomming_busses.sort()

	return incomming_busses

def main():
	while True:
		print("\nRefreshing Data!")
		try:
			visits = get_predictions([14159,14158],['IB'])
			for i in range(60):
				print("")
				print(i)
				incomming_busses = update_predictions(visits,i)
				for predictions in parse_predictions(incomming_busses):
					print(predictions)
				time.sleep(1)
		except:
			print("\nNetwork Error\n")
			time.sleep(5)



if __name__ == "__main__":
	main()

