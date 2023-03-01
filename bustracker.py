import urllib.request
import json
import time
from datetime import datetime


def get_predictions(stops,directions):
	visits = []

	for stop in stops:

		dateformat = '%Y-%m-%dT%H:%M:%SZ'
		url = 'https://api.511.org/transit/StopMonitoring?'
		api_key = 'api_key=baac5dd7-16fd-4bbf-b417-7fdd9ced9619'
		agency = '&agency=SF'
		stopCode = '&stopCode='+str(stop)
		frmt = '&format=json'

		resp = urllib.request.urlopen(url+api_key+agency+stopCode+frmt)
		content = resp.read().decode('utf-8-sig').encode('utf-8')

		data = json.loads(content)

		recordedtime = datetime.strptime(data['ServiceDelivery']['StopMonitoringDelivery']['ResponseTimestamp'],dateformat)

		for stops in data['ServiceDelivery']['StopMonitoringDelivery']['MonitoredStopVisit']:
			direction = str(stops['MonitoredVehicleJourney']['DirectionRef'])
			if direction not in directions:
				continue
			line = str(stops['MonitoredVehicleJourney']['LineRef'] + ' ' + str(stops['MonitoredVehicleJourney']['DirectionRef']))
			expectedtime = datetime.strptime(stops['MonitoredVehicleJourney']['MonitoredCall']['ExpectedArrivalTime'],dateformat)
			timedelta = expectedtime-recordedtime

			rounded_eta = timedelta.seconds

			if timedelta.days < 10:
				visits.append([line, rounded_eta])

	return visits

def update_predictions(visits, s):
	out = []
	for busses in visits:
		out.append([busses[0], busses[1] - s])

	return out 


def parse_predictions(visits):
	route_list = []
	for routes in visits:
		if routes[0] not in route_list:
			route_list.append(routes[0])

	incomming_busses = []
	for routes in route_list:
		route_times = str(routes) + ":"
		for eta in visits:
			if eta[0] == routes:
				route_times = route_times + " " + str(int(eta[1]/60)) + ","
		incomming_busses.append(route_times[:-1])

	incomming_busses.sort()

	return incomming_busses

def main():

	while True:

		print("\nRefreshing Data!")
		try:
			visits = get_predictions([14159,14158],['IB'])#,'OB'])

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

