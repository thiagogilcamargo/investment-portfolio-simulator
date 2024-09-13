from portfolio import Portfolio
from data_fetcher import fetch_data
from visualizer import plot_portfolio_performance
from simulations import monte_carlo_simulation

def main():
    print("Bem-vindo ao Simulador de Carteira de Investimentos!")
    
    # Exemplo de ativos e suas respectivas alocações
    assets = ['AAPL', 'MSFT', 'GOOGL', 'TSLA']
    allocations = [0.3, 0.2, 0.3, 0.2]  # Deve somar 1

    # Definir o período para análise (em anos)
    period = '5y'

    # Baixar dados financeiros
    data = fetch_data(assets, period)
    
    # Criar a carteira
    portfolio = Portfolio(assets, allocations, data)
    
    # Mostrar retorno e risco da carteira
    portfolio_performance = portfolio.calculate_performance()
    print(f"Retorno esperado: {portfolio_performance['expected_return']:.2f}%")
    print(f"Risco (volatilidade): {portfolio_performance['volatility']:.2f}%")
    print(f"Sharpe Ratio: {portfolio_performance['sharpe_ratio']:.2f}")

    # Visualizar o desempenho
    plot_portfolio_performance(portfolio)

    # Simulação de Monte Carlo
    monte_carlo_simulation(portfolio)

if __name__ == "__main__":
    main()
