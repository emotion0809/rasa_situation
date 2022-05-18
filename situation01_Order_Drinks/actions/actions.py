
from errno import ESTALE
import pathlib
import random
from typing import Any, Text, Dict, List
from rasa_sdk.forms import FormValidationAction

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet


drinks_type_list = pathlib.Path("data/drinks_type.txt").read_text().split("\n")
drinks_list = pathlib.Path("data/drinks.txt").read_text().split("\n")
wine_list = pathlib.Path("data/wine.txt").read_text().split("\n")
cocktail_list = pathlib.Path("data/cocktail.txt").read_text().split("\n")
beer_list = pathlib.Path("data/beer.txt").read_text().split("\n")
len_drinks_list = len(drinks_list)
len_wine_list = len(wine_list)
len_cocktail_list = len(cocktail_list)
len_beer_list = len(beer_list)

class ActionCheckOrder(Action):

    def name(self) -> Text:
        return "action_check_order"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        check_order = "a "
        blended_or_on_rock = tracker.get_slot('blended_or_on_rock')
        salt_or_no_salt = tracker.get_slot('salt_or_no_salt')
        check_order += tracker.get_slot("drinks")
        if(blended_or_on_rock):
            check_order += " blended"
        else:
            check_order += " on_rock"
        if(salt_or_no_salt):
            check_order += " salt"
        else:
            check_order += " no_salt"
        dispatcher.utter_message(text= check_order)
        return []

class ActionSlotSetDrinks(Action):

    def name(self) -> Text:
        return "action_check_menu"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        drinks = next(tracker.get_latest_entity_values("drinks.txt"), None)
        if drinks is not None:
            if drinks in drinks_type_list:
                return [SlotSet("drinks_type",drinks),SlotSet("tmp_drinks",None)]
            elif drinks in drinks_list:
                return[SlotSet("drinks_type",None),SlotSet("tmp_drinks",drinks)]
        return[SlotSet("drinks_type",None),SlotSet("tmp_drinks",None)]

class ActionHaveThisDrinks(Action):

    def name(self) -> Text:
        return "action_have_this_drinks"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        drinks_type = tracker.get_slot('drinks_type')
        drinks = tracker.get_slot("tmp_drinks")
        if drinks_type is not None:
            dispatcher.utter_message(response = "utter_have_this_type")
        elif drinks is not None:
            dispatcher.utter_message(response = "utter_have_this_drinks")
        else:
            dispatcher.utter_message(text = "we don't have this drinks.")
        return []

class ActionAcceptRecommend(Action):

    def name(self) -> Text:
        return "action_accept_recommend"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        drinks = tracker.get_slot("tmp_drinks")
        return [SlotSet("tmp_drinks",None),SlotSet("drinks",drinks)]

class ActionOrderDrinks(Action):

    def name(self) -> Text:
        return "action_order_drinks"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        drinks = next(tracker.get_latest_entity_values("drinks.txt"), None)
        if drinks is not None:
            dispatcher.utter_message(response = "drinks_form")
        else:
            dispatcher.utter_message(text = "we don't have this drinks.")
        return [SlotSet("tmp_drinks",None),SlotSet("drinks",drinks)]

class ActionRecommend(Action):

    def name(self) -> Text:
        return "action_recommend"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        drinks_type = tracker.get_slot('drinks_type')
        if drinks_type == "wine":
            tmp_drinks = wine_list[random.randrange(len_wine_list)]
        elif drinks_type == "cocktail":
            tmp_drinks = cocktail_list[random.randrange(len_cocktail_list)]
        elif drinks_type == "beer":
            tmp_drinks = beer_list[random.randrange(len_beer_list)]
        else:
            tmp_drinks = drinks_list[random.randrange(len_drinks_list)]
        return [SlotSet("tmp_drinks",tmp_drinks),SlotSet("drinks_type",None)]