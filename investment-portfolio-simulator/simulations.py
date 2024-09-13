import numpy as np
import matplotlib.pyplot as plt

def monte_carlo_simulation(portfolio, num_simulations=1000, num_days=252):
    """
    Simulação de Monte Carlo para prever o desempenho da carteira.
    """
    portfolio_returns = (portfolio.returns * portfolio.allocations).sum(axis=1)
    mean_return = portfolio_returns.mean()
    volatility = portfolio_returns.std()

    results = np.zeros((num_simulations, num_days))

    for i in range(num_simulations):
        daily_returns = np.random.normal(mean_return, volatility, num_days)
        results[i, :] = np.cumprod(1 + daily_returns)

    # Plotar as simulações
    plt.figure(figsize=(10, 6))
    plt.plot(results.T, color='grey', alpha=0.1)
    plt.title("Simulação de Monte Carlo - Previsão do Desempenho da Carteira")
    plt.xlabel("Dias")
    plt.ylabel("Retorno Cumulativo")
    plt.grid(True)
    plt.show()
