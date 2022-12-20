# from card_ons import Card
from bot_ons import BotOns
# from utils.driver import MyDriver
from wpp import Wpp


PATH_DOWNLOAD = 'C:\\Users\\middle\\Downloads\\'

bot = BotOns()
bot.exec()
card= bot.get_card('ipdo', 'pdf', '12/12/2022', '12/12/2022')[0]
# bot.get_file(card)

wpp = Wpp()
wpp.send_to('+5533998358645', text=card.str_wpp(), file=PATH_DOWNLOAD + card.footer['Nome do arquivo'])