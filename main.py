from bot_ons import BotOns
from utils.general import today
import pandas as pd


BotOns.exec()
out = BotOns.get_card('acomph', 'xls', '12/12/2022', today())

print(*out if type(out) == list else out)