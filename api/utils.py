from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import time

class CoinMarketCap:
    BASE_URL="https://coinmarketcap.com/currencies/"

    def __init__(self):
        options=webdriver.FirefoxOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        self.driver=webdriver.Firefox(service=Service(GeckoDriverManager().install()),options=options)

    # To scrape coin details
    def get_coin_data(self,coin):
        url=f'{self.BASE_URL}{coin}'
        self.driver.get(url)
        self.driver.maximize_window()
        time.sleep(3)

        try:
            # price field
            price=''
            try:
                price=self.driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/section/div/div[2]/span').text
                price=float(self.removeComma(price[1:]))
            except:
                price='Was not able to scrape this field'


            # price_change field
            price_change=''
            try:
                price_change=self.driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/section/div/div[2]/div/div/p')
                price_change=float(self.checkColor(price_change.get_attribute('color'))+price_change.text[:price_change.text.find('%')])
            except:
                price_change='Was not able to scrape this field'

            
            # market_cap field
            market_cap=''
            try:
                market_cap=self.driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[2]/section[2]/div/div[1]/div/dl/div[1]/div[1]/dd').text
                market_cap=(self.removeComma(market_cap[market_cap.find('$')+1:]))
            except:
                market_cap='Was not able to scrape this field'
            
            
            # market_cap_rank field
            market_cap_rank=''
            try:
                market_cap_rank=self.driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[2]/section[2]/div/div[1]/div/dl/div[1]/div[2]/div/span').text
                market_cap_rank=int(market_cap_rank[1:])
            except:
                market_cap_rank='Was not able to scrape this field'
            
            
            # volume field
            volume=''
            try:
                volume=self.driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[2]/section[2]/div/div[1]/div/dl/div[2]/div[1]/dd').text
                volume=(self.removeComma(volume[volume.find('$')+1:]))
            except:
                volume='Was not able to scrape this field'
            
            
            # volume_rank field
            volume_rank=''
            try:
                volume_rank=self.driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[2]/section[2]/div/div[1]/div/dl/div[2]/div[2]/div/span').text
                volume_rank=int(volume_rank[1:])
            except:
                volume_rank='Was not able to scrape this field'
            
            
            # volume_change field
            volume_change=''
            try:
                volume_change=self.driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[2]/section[2]/div/div[1]/div/dl/div[3]/div/dd').text
                volume_change=float(volume_change[:-1])
            except:
                volume_change='Was not able to scrape this field'

            
            # circulating_supply field
            circulating_supply=''
            try:
                circulating_supply=self.driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[2]/section[2]/div/div[1]/div/dl/div[4]/div/dd').text
                circulating_supply=(self.removeComma(circulating_supply[:circulating_supply.find(' ')]))
            except:
                circulating_supply='Was not able to scrape this field'


            # total_supply field
            total_supply=''
            try:
                total_supply=self.driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[2]/section[2]/div/div[1]/div/dl/div[5]/div/dd').text
                total_supply=(self.removeComma(total_supply[:total_supply.find(' ')]))
            except:
                total_supply='Was not able to scrape this field'



            # diluted_market_cap field
            diluted_market_cap=''
            try:
                diluted_market_cap=self.driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[2]/section[2]/div/div[1]/div/dl/div[7]/div/dd').text
                diluted_market_cap=(self.removeComma(diluted_market_cap[1:]))
            except:
                diluted_market_cap='Was not able to scrape this field'


            # contracts list
            contracts=[]    
            try:
                contract_name=self.driver.find_elements(By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[2]/section[2]/div/div[2]/div[1]/div[2]/div/div[1]/a/span[1]")
                address=self.driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[2]/section[2]/div/div[2]/div[1]/div[2]/div/div[1]/a/span[2]')
                for i in range(len(contract_name)):
                    contract={
                        'name':contract_name[i].text[:-1],
                        'address':address[i].text
                    }
                    contracts.append(contract)
            except:
                pass

            
            # official_links list
            official_links=[]
            try:
                official_links_elements=self.driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[2]/section[2]/div/div[2]/div[2]/div[2]/div/div/a')
                for i in official_links_elements:
                    link_name=i.text
                    link=i.get_attribute('href')
                    official_link={
                        'name':link_name,
                        'link':link
                    }
                    official_links.append(official_link)
            except:
                pass            


            # socials list
            socials=[]
            try:
                social_elements=self.driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[2]/section[2]/div/div[2]/div[3]/div[2]/div/div/a')
                for i in social_elements:
                    social_name=i.text
                    url=i.get_attribute('href')
                    social={
                        'name':social_name,
                        'url':url
                    }
                    socials.append(social)
            except:
                pass


            data={
                'price':price,
                'price_change':price_change,
                'market_cap':market_cap,
                'market_cap_rank':market_cap_rank,
                'volume':volume,
                'volume_rank':volume_rank,
                'volume_change':volume_change,
                'circulating_supply':circulating_supply,
                'total_supply':total_supply,
                'diluted_market_cap':diluted_market_cap,
                'contracts':contracts,
                'official_links':official_links,
                'socials':socials
            }

            return data
        except Exception as e:
            raise Exception(f"Scraping failed: {str(e)}")
        
        
    #  To close the driver
    def close(self):
        self.driver.quit()

    # To check weather the numbers are in green or red. To represent sign
    def checkColor(self,color):
        sign=''
        if color!='green':
            sign='-'
        return sign


    # To remove commas from the number strings
    def removeComma(self,val):
        num=''
        for i in val:
            if i==',':
                continue
            num+=i
        return num

