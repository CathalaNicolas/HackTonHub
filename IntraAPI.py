import json;
import requests;

##Class Event represent one event to display on the screen
class Event:
	startTime = ""
	endTime = ""
	room = ""
	roomDescription = ""
	roomSeats = ""
	title = ""
	duration = ""
	typeEvent = ""
	
	##Print information of the event
	def printInfo(self):
		print("New Event ----")
		print("Start Time: " + str(self.startTime))
		print("endTime: " + str(self.endTime))
		print("room: " + str(self.room))
		print("roomDescription: " + str(self.roomDescription))
		print("roomSeats: " + str(self.roomSeats))
		print("title: " + str(self.title))
		print("duration: " + str(self.duration))
		print("typeEvent: " + str(self.typeEvent))
		print("End Event ----\n")

##Class eventManager, handles the list of Event and handles the request to intra's API.
class EventManager:
	jsonContent = dict()
	url = ""
	numberEvent = 0
	listEvent = list()

	##Init of EventManager class, we get json and build the list of event on construction. 
	##Param Start	define the start date of the request, form => "YYYY-MM-DD"
	##Param End		define the end date of the request, form => "YYYY-MM-DD"
	##
	##Example: Start = "2019-02-16" for 16 february 2019
	def __init__(self, start, end):
		self.url = "https://intra.epitech.eu/auth-6f2226bcc4e95b0ab4fcc1ea0c41185cd6b088ef/planning/load?format=json&start=" + start + "&end=" + end
		self.updateJson()
		self.buildListFromJson()

	##Build list of Event base on jsonContent, module as to be from "B-INN-000" to get registered as an event
	def buildListFromJson(self):
		for item in self.jsonContent:
			if "codemodule" in item and item["codemodule"] == "B-INN-000":
				event = Event()
				if "start" in item:
					event.startTime = str(item["start"])
				if "end" in item:
					event.endTime = str(item["end"])
				if "room" in item:
					tmp = item["room"]
					if tmp != None and "code" in tmp:
						event.room = str(tmp["code"]).split("/")[-1]
					if tmp != None and "type" in tmp:
						event.roomDescription = str(tmp["type"])
					if tmp != None and "seats" in tmp:
						event.roomSeats = str(tmp["seats"])
				if "acti_title" in item:
					event.title = str(item["acti_title"])
				if "nb_hours" in item:
					event.duration = str(item["nb_hours"])
				if "type_title" in item:
					event.typeEvent = str(item["type_title"])
				self.listEvent.append(event)
	
	##Update jsonContent with new request to Epitech intra API
	def updateJson(self):
		response = requests.get(self.url)
		binary = response.content
		self.jsonContent = json.loads(binary)
	
	##Print Json in more pretty way
	def printPrettyJson(self):
		print(json.dumps(self.jsonContent, indent=4))
	
	##Print information of the list of event
	def printEventInfo(self):
		for event in self.listEvent:
			event.printInfo()

if __name__ == '__main__':
	manager = EventManager("2019-01-01", "2019-02-16")
	manager.printPrettyJson()
	manager.printEventInfo()
