import pandas as pd
import chart_generation.web_data.source as source
import chart_generation.web_data.clean as clean

class CompanyData:
    def __init__(self, symbol):
        self.symbol = symbol
        self.income_statement = self.i_s()
        self.balance_sheet = self.b_s()
        self.cash_flows = self.c_f()

    def i_s(self):
        temp = source.source_data(self.symbol, '')
        temp = clean.drop_useless_columns(temp)
        return temp

    def b_s(self):
        temp = source.source_data(self.symbol, 'balance-sheet')
        temp = clean.drop_useless_columns(temp)
        return temp

    def c_f(self):
        temp = source.source_data(self.symbol, 'cash-flow')
        return clean.drop_useless_columns(temp)
