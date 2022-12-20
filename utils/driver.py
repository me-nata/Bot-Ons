from enum import Enum
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from utils.general import execute
import os


class Err(Enum):
    NOP=0
    SITE_NOT_ACESS=1
    LOGIN_NOT_ACESS=2
    ELEMENT_NOT_FOUND=3
    FILE_NOT_FOUND=4
    SEARCH_NOT_AVAILABLE=5


class Element:
    @staticmethod
    def make(by:By, value:str, word=None) -> dict:
        return {
            'by': by,
            'value': value,
            'word': word
        } 


class MyDriver:
    def __init__(self, name_dir) -> None:
        dir_path = os.getcwd()
        profile = os.path.join(dir_path, "profile", name_dir)
        options = webdriver.ChromeOptions()
        options.add_argument(r"user-data-dir={}".format(profile))

        self.DRIVER = webdriver.Chrome(chrome_options=options)
        
        self.END = False
        self.IN_EXEC = False


    def _access(self, site:str) -> None:
        self.DRIVER.get(site)
        self.DRIVER.maximize_window()
        self.END = False
        while not self.END: pass


    def access(self, site:str) -> None:
        if self.IN_EXEC:
            self.END = True

        self.IN_EXEC = True
        execute(self._access, args=[site])


    def close(self) -> None:
        self.END = True
        self.IN_EXEC = False


    def open(self, link:str) -> None:
        self.DRIVER.get(link)


    def exist(self, element: Element) -> True:
        try:
            self.DRIVER.find_element(element['by'], element['value'])
        except: 
            return False

        return True
        
        
    def click(self, element:dict) -> None:
        self.DRIVER.find_element(element['by'], element['value']).click()


    @staticmethod
    def erase(field):
        field.send_keys(Keys.CONTROL, 'a', Keys.DELETE)


    def write(self, element:dict, delete_field=False) -> None:
        field = self.DRIVER.find_element(element['by'], element['value'])
       
        if delete_field:
            MyDriver.erase(field)
        
        field.send_keys(element['word'])


    def write_enter(self, element:dict, delete_field=False) -> None:
        field = self.DRIVER.find_element(element['by'], element['value'])
    
        if delete_field:
            MyDriver.erase(field)
        
        field.send_keys(element['word'], Keys.ENTER)
        

    def write_and_click(self, element_write:dict, element_click:dict, delete_field=False) -> None:
        self.write(element_write, delete_field)
        self.click(element_click)


    def enter_simple_login(self, element_username:dict, element_password:dict, element_submit_button:dict, wait:tuple=(0,0), enter=False) -> None:
        execute(
            lambda: self.write_enter(element_username) if enter else self.write(element_username), 
            thread=False, prev_wait=wait[0], for_wait=wait[1]
        )
        self.write_and_click(element_password, element_submit_button)

    
    def restart(self):
        self.DRIVER.refresh()


    @staticmethod
    def getPropertys(elements, property):
        return [element.get_property(property) for element in elements]