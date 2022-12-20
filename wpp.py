from utils.driver import Element, MyDriver, By

class Wpp:
    def __init__(self) -> None:
        self.driver = MyDriver('wpp')
        self.driver.access('https://web.whatsapp.com')
        while not self.driver.exist(Element.make(By.ID, 'side')): pass # enter verify


    def send_to(self, phone, text, file=None):
        self.driver.open(f'https://web.whatsapp.com/send?phone={phone}&text={text}')
        button = Element.make(By.XPATH, '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')
        while(not self.driver.exist(button)): pass # verify load page

        if file != None:
            path_clip = '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/span'
            self.driver.click(element=Element.make(By.XPATH, path_clip))
            
            path_input_file = '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[4]/button/input'
            input_file = self.driver.DRIVER.find_element(By.XPATH, path_input_file)

            input_file.send_keys(file)
            
            path_ok = '/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div/span'
            ok = Element.make(By.XPATH, path_ok)
            while not self.driver.exist(ok): pass
            self.driver.click(element=ok)
        else:
            self.driver.click(element=button)
    