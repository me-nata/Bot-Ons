from utils.driver import *
from utils.general import sleep, os


class ONS:
    def __init__(self) -> None:
        self.driver= MyDriver(name_dir='ons')


    def download(self, link:str) -> None:
        self.driver.open(link)


    def accessONS(self) -> None:
        self.driver.access('https://sintegre.ons.org.br/paginas/busca.aspx')    


    def enter_login(self):
        id_email = 'username'
        id_password = 'password'

        if self.driver.exist(Element.make(By.ID, id_password)) or self.driver.exist(Element.make(By.ID, id_email)):
            print('Please make your login in ONS')
            while self.driver.exist(Element.make(By.ID, id_password)) or self.driver.exist(Element.make(By.ID, id_email)): pass
            sleep(2)
            self.driver.restart()
        
        print('Login Success')


    def search(self, name, date_de, date_ate):
        id_search = 'tbSearch'
        id_date_de = 'tbDataDe'
        id_date_ate = 'tbDataAte'
        
        self.driver.write(Element.make(By.ID, id_search, name), delete_field=True)
        self.driver.write(Element.make(By.NAME, id_date_de, word=date_de), delete_field=True)
        self.driver.write_enter(Element.make(By.NAME, id_date_ate, word=date_ate), delete_field=True)


    def request_card_info(self, name_search, day_init, day_end):
        execute(self.search, args=[name_search, day_init, day_end], thread=False)

        titles_element    = self.driver.DRIVER.find_elements(By.CLASS_NAME, 'resultado-titulo')
        subtitles_element = self.driver.DRIVER.find_elements(By.CLASS_NAME, 'resultado-corpo')
        footer_element    = self.driver.DRIVER.find_elements(By.CLASS_NAME, 'resultado-footer')
        links_element     = self.driver.DRIVER.find_elements(By.ID, 'link-botao')

        titles = MyDriver.getPropertys(titles_element, 'innerText')
        subtitles = MyDriver.getPropertys(subtitles_element, 'innerText')
        footer = MyDriver.getPropertys(footer_element, 'innerText')
        links = MyDriver.getPropertys(links_element, 'href')

        return (titles, subtitles, footer, links)