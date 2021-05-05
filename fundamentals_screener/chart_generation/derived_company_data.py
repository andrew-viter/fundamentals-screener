import pandas as pd
import numpy as np
from decimal import Decimal

class DerivedCompanyData:
    def __init__(self, cd):
        self.base_data = cd
        self.derived_company_data = self.calculate_data()

    def calculate_data(self):
        ncols = len(self.base_data.income_statement.columns)
        derived_data = np.zeros((9, ncols), dtype=Decimal)
        derived_data[0] = 100 * (self.base_data.income_statement.loc['Gross Income'] / self.base_data.income_statement.loc['Sales/Revenue'])
        derived_data[1] = 100 * (self.base_data.income_statement.loc['Pretax Income'] / self.base_data.income_statement.loc['Sales/Revenue'])
        derived_data[2] = 100 * (self.base_data.income_statement.loc['Net Income'] / self.base_data.income_statement.loc['Sales/Revenue'])
        derived_data[3] = 100 * (self.base_data.income_statement.loc['Cost of Goods Sold (COGS) incl. D&A'] / self.base_data.income_statement.loc['Sales/Revenue'])
        derived_data[4] = self.base_data.income_statement.loc['EPS (Basic)']
        derived_data[5] = self.base_data.income_statement.loc['EPS (Diluted)']
        derived_data[6] = self.base_data.balance_sheet.loc['Total Current Assets'] / self.base_data.balance_sheet.loc['Total Current Liabilities']
        derived_data[7] = (self.base_data.balance_sheet.loc['Long-Term Debt'] + self.base_data.balance_sheet.loc['ST Debt & Current Portion LT Debt']) / self.base_data.balance_sheet.loc['Total Shareholders\' Equity']
        derived_data[8] = self.base_data.cash_flows.loc['Free Cash Flow']
        if ncols < 5:
            injected_zeros = np.zeros((9, 5-ncols), dtype=Decimal)
            return np.concatenate((injected_zeros, derived_data), axis=1)
        return derived_data