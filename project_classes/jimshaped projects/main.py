from crypto_scraper import CryptoCurrency


if __name__ == "__main__":
    symbol1 = CryptoCurrency(symbol="btcusd")
    print(symbol1.price)

