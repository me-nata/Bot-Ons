from bot_ons import BotOns
from utils.general import today
import pandas as pd


BotOns.exec()
BotOns.get_cards([
    ('IPDO', 'pdf', '12/12/2022', today()),
    ('IPDO', 'pdf', '12/12/2022', today()),
    ('IPDO', 'pdf', '10/12/2022', today()),
    ('IPDO', 'pdf', '10/12/2022', today()),
    ('IPDO', 'pdf', '10/12/2022', today())
])

df = pd.read_csv('./files/links.csv', sep=';', encoding='latin-1')