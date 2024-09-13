import matplotlib.pyplot as plt

def plot_portfolio_performance(portfolio):
    """
    Gera gráficos para visualizar o desempenho da carteira.
    """
    portfolio_returns = (portfolio.returns * portfolio.allocations).sum(axis=1)
    cumulative_returns = (1 + portfolio_returns).cumprod()

    # Plotar retorno cumulativo
    plt.figure(figsize=(10, 6))
    cumulative_returns.plot()
    plt.title("Desempenho da Carteira")
    plt.xlabel("Data")
    plt.ylabel("Retorno Cumulativo")
    plt.grid(True)
    plt.show()
