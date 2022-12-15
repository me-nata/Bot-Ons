import os
from utils.driver import *
from utils.general import sleep


dir_path = os.getcwd()
profile = os.path.join(dir_path, "profile", "ons")
options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir={}".format(profile))

driver= MyDriver(options)


class ONS:
    @staticmethod
    def accessONS():
        global driver
        driver.access('https://sintegre.ons.org.br/paginas/busca.aspx')    


    @staticmethod
    def enter_login():
        global driver

        id_email = 'username'
        id_password = 'password'

        if driver.exist(Element.make(By.ID, id_password)) or driver.exist(Element.make(By.ID, id_email)):
            print('Please make your login in ONS')
            while driver.exist(Element.make(By.ID, id_password)) or driver.exist(Element.make(By.ID, id_email)): pass
        
        print('Login Success')

        sleep(3)
        
        driver.restart()


    @staticmethod
    def search(name, date_de, date_ate):
        global driver

        id_search = 'tbSearch'
        id_date_de = 'tbDataDe'
        id_date_ate = 'tbDataAte'
        
        driver.write(Element.make(By.ID, id_search, name), delete_field=True)
        driver.write(Element.make(By.NAME, id_date_de, word=date_de), delete_field=True)
        driver.write_enter(Element.make(By.NAME, id_date_ate, word=date_ate), delete_field=True)


    @staticmethod
    def request_card_info(name_search, day_init, day_end):
        execute(ONS.search, args=[name_search, day_init, day_end], thread=False)

        titles_element    = driver.DRIVER.find_elements(By.CLASS_NAME, 'resultado-titulo')
        subtitles_element = driver.DRIVER.find_elements(By.CLASS_NAME, 'resultado-corpo')
        footer_element    = driver.DRIVER.find_elements(By.CLASS_NAME, 'resultado-footer')
        links_element     = driver.DRIVER.find_elements(By.ID, 'link-botao')

        titles = MyDriver.getPropertys(titles_element, 'innerText')
        subtitles = MyDriver.getPropertys(subtitles_element, 'innerText')
        footer = MyDriver.getPropertys(footer_element, 'innerText')
        links = MyDriver.getPropertys(links_element, 'href')

        return (titles, subtitles, footer, links)