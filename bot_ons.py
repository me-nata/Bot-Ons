import datetime
from ons import ONS
from card_ons import Card
from utils.general import *
from utils.driver import Err
import pandas as pd

class BotOns:
    @staticmethod
    def exec():
        ONS.accessONS()
        execute(ONS.enter_login, prev_wait=5, for_wait=5, thread=False)


    @staticmethod
    def get_card(name_search, type_file, day_start, day_end):
        cards = Card.cards(*ONS.request_card_info(name_search, day_start, day_end))

        if len(cards) == 0:
            return Err.ELEMENT_NOT_FOUND

        output = []
        for card in cards:
            print(card)
            if card.match_required(name_search, type_file):
                output.append(card)
        
        if output == []:
            return Err.SEARCH_NOT_AVAILABLE
            

        return output[0] if len(output) == 1 else output

    
    @staticmethod
    def get_cards(infos:list):
        out = []
        for info in infos:
            out.append(BotOns.get_card(*info))
            sleep(1)

        return out