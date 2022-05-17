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
class ActionResult(Action):

   def name(self) -> Text:
        return "action_annoce_result"

   def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        split_cake = tracker.get_slot('split_cake')
        order_drink = tracker.get_slot('order_drink')
        order_dessert = tracker.get_slot('order_dessert')
        check_order = "So,you order a "+order_dessert+" and go with "+order_drink
        if(split_cake):
            check_order += " and need a split for cake."
        else:
            check_order += " and no need a split."


        dispatcher.utter_message(text= check_order)

        return []          
class ActionComfire(Action):

   def name(self) -> Text:
        return "action_comfirm"

   def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        check_order=""
        split_cake = tracker.get_slot('comfirm')
        if(split_cake):
            check_order += "utter_comfirm_nagative"
        else:
            check_order += "utter_comfirm_positive"
        dispatcher.utter_message(response= check_order)
        return []      
