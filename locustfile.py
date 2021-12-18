from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(5, 20)
    host = 'https://api.coinlore.net/api/'

    @task
    def GetInformationAboutCryptoMarket(self):
        self.client.get("global/")

    @task
    def GetInformationAboutFirts100Coins(self):
        self.client.get("tickers/")

    @task
    def GetInformationForSpecificCoin(self):
        self.client.get("ticker/?id=90")

    @task
    def GetFirst50MarketsForSpecificCoin(self):
        self.client.get("coin/markets/?id=90")

    @task
    def GetAllExchanges(self):
        self.client.get("exchanges/")

    @task
    def GetSpecificExchangeByID(self):
        self.client.get("exchange/?id=5")

    @task
    def GetSocialStatsForCoin(self):
        self.client.get("coin/social_stats/?id=80")

