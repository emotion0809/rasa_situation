# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk.forms import FormValidationAction

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

class ActionHelloWorld(Action):

   def name(self) -> Text:
        return "action_wheatherSplit"

   def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        check_order = "You will"
        split_cake = tracker.get_slot('split_cake')
        if(split_cake):
            check_order += " split"
        else:
            check_order += " not split"
        dispatcher.utter_message(text= check_order)

        return []
class ActionInvest(Action):

   def name(self) -> Text:
        return "invest_mood"

   def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        check_order = ""
        split_cake = tracker.get_slot('invest_mood')
        if(split_cake):
            check_order += " split"
        else:
            check_order += " not split"
        dispatcher.utter_message(text= check_order)

        return []        
