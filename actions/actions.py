# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"


#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
import requests
from rasa_sdk.events import AllSlotsReset

class ValidateRooms(Action):
    
    def name(self)-> Text:
        return "validate_room_no"
    
    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        no_room = tracker.get_slot('number_of_room')
        print("number of room", no_room)
        print("Checking................")
        if no_room > 5:
            dispatcher.utter_message(text="You can't book more than  rooms")
            return []
        dispatcher.utter_message(text="Validating the rooms")
        return []
        







