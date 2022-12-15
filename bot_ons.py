from ons import ONS
from card_ons import Card
from utils.general import execute, sleep
from utils.driver import Err
import pandas as pd
import os


FILE_DIR = './files'
if not os.path.exists(FILE_DIR):
    os.mkdir(FILE_DIR)

LINKS = f'{FILE_DIR}/links.csv'
CACHE_FILE = F'{FILE_DIR}/cache'


END = False
class BotOns:
    def __init__(self, file=LINKS) -> None:
        self.df_links = pd.read_csv(file, sep=';') 


    @staticmethod
    def exec():
        ONS.accessONS()
        execute(ONS.enter_login, prev_wait=5, for_wait=5, thread=False)


    @staticmethod
    def get_card(name_search, type_card, day_init, day_end):
        cards = Card.cards(*ONS.request_card_info(name_search, day_init, day_end))

        if len(cards) == 0:
            return Err.ELEMENT_NOT_FOUND

        output = None
        for card in cards:
            if card.match_required(name_search, type_card):
                if not card.in_cache(CACHE_FILE):
                    card.save(LINKS)
                    card.save(CACHE_FILE, cache=True)

                output = card
        
        if output == None:
            output = Err.SEARCH_NOT_AVAILABLE
                
        return output

    
    @staticmethod
    def get_cards(infos:list):
        out = []
        for info in infos:
            out.append(BotOns.get_card(*info))
            sleep(1)

        return out