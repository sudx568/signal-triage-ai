import pandas as pd


class DataLoader:

    def __init__(self, path):

        self.path = path

    def load(self):

        df = pd.read_csv(self.path)

        df = df.dropna()

        return df