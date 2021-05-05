import pandas as pd
import chart_generation.web_data.source as source
import chart_generation.web_data.clean as clean

class CompanyData:
    def __init__(self, symbol):
        self.symbol = symbol
        self.income_statement = self.retrieve_statement()
        self.balance_sheet = self.retrieve_statement('balance-sheet')
        self.cash_flows = self.retrieve_statement('cash-flow')

    def retrieve_statement(self, stm = ''):
        temp = source.source_data(self.symbol, stm)
        temp = clean.drop_useless_columns(temp)
        return clean.clean_table_data(temp)
