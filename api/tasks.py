from celery import shared_task
from .utils import CoinMarketCap

@shared_task
def scrape_crypto_data(payload):
    result=[]
    scraper=CoinMarketCap()

    try:
        for coin in payload:
            coin_data=scraper.get_coin_data(coin)
            result.append({'coin':coin,'output':coin_data})
    except Exception as e:
        raise Exception(f"Task failed: {str(e)}")
    finally:
        scraper.close()
    
    return result