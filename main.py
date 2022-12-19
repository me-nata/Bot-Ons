from bot_ons import BotOns
from utils.general import today


BotOns.exec()
out = BotOns.get_card('acomph', 'xls', '12/12/2022', today())

print(*out if type(out) == list else out)