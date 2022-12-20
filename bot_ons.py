from ons import ONS
from card_ons import Card
from utils.general import *
from utils.driver import Err


class BotOns:
    def __init__(self) -> None:
        self.ons = ONS()


    def exec(self):
        self.ons.accessONS()
        execute(self.ons.enter_login, thread=False)


    def get_card(self, name_search, type_file, day_start, day_end):
        cards = Card.cards(*self.ons.request_card_info(name_search, day_start, day_end))

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

    
    def get_cards(self, infos:list):
        out = []
        for info in infos:
            out.append(self.get_card(*info))
            sleep(1)

        return out


    def get_file(self, card: Card) -> None:
        self.ons.download(card.link)