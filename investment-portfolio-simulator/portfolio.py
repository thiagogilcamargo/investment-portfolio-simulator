import numpy as np

class Portfolio:
    def __init__(self, assets, allocations, data):
        self.assets = assets
        self.allocations = allocations
        self.data = data
        self.returns = self.data.pct_change().dropna()

    def calculate_performance(self):
        # Calcular o retorno esperado e risco (volatilidade)
        expected_return = np.sum(self.returns.mean() * self.allocations) * 252
        cov_matrix_annual = self.returns.cov() * 252
        portfolio_volatility = np.sqrt(np.dot(self.allocations, np.dot(cov_matrix_annual, self.allocations)))

        # Calcular o Sharpe Ratio (supõe-se taxa livre de risco de 0%)
        sharpe_ratio = expected_return / portfolio_volatility

        return {
            'expected_return': expected_return * 100,  # em percentual
            'volatility': portfolio_volatility * 100,  # em percentual
            'sharpe_ratio': sharpe_ratio
        }
