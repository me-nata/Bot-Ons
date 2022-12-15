import pandas as pd


class Card:
    def __init__(self, title, subtitle, footer, link) -> None:
        self.title = title
        self.subtitle = subtitle
        self.footer = Card.get_footer(footer)
        self.link = link


    @staticmethod
    def get_footer(footer:str):
        groups = [element.split('\n') for element in footer.split(':')]
        general = [element.strip() for group in groups for element in group]
        
        # Remove "baixar" label 
        general.pop(-1)

        # Remove string concat with date
        concat = 'Processo'
        general[-2] = general[-2][:-len(concat)].strip()
        general.insert(-1, 'Processo')

        footer = {}
        i = 0
        while(i < len(general)):
            footer[general[i]] = general[i+1]
            i+=2

        return footer
    

    def match_required(self, search_name:str, type_required:str):
        name = self.footer['Nome do arquivo'].split('.')[0].lower()
        type = self.footer['Nome do arquivo'].split('.')[1].lower()

        return search_name.lower() in name and type_required == type


    def __str__(self) -> str:
        return f"""
            {self.title}
            {self.subtitle}
            {self.footer}
            {self.link}
        """


    @staticmethod
    def cards(titles, subtitles, footer, links) -> list:
        cards = []
        for i in range(len(titles)):
            cards.append(Card(titles[i], subtitles[i], footer[i], links[i]))

        return cards

    
    def save(self, file, cache=False):
        nome = self.footer['Nome do arquivo']
        data = ''
        if cache:
            data = f'{nome}\n'
        else:
            tipo = self.footer['Tipo']
            data = self.footer['Data']
            processo = self.footer['Processo']

            data = f'\n{self.title};{self.subtitle};{tipo};{nome};{data};{processo};{self.link}'

        with open(file, 'a') as links:
            links.write(data)
            links.close()
        

    def in_cache(self, file):
        with open(file, 'r') as f:
            lines = f.readlines()
            f.close()

        output = False
        for name in lines:
            if name[:-1] == self.footer['Nome do arquivo']:
                output = True
                break

        return output