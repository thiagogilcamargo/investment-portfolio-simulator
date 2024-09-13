# Simulador de Carteira de Investimentos

Este projeto é um **Simulador de Carteira de Investimentos** desenvolvido em Python, voltado para análise de retorno e risco de uma carteira composta por ativos do mercado financeiro. Além disso, ele realiza simulações de Monte Carlo para prever possíveis cenários de desempenho futuro da carteira.

## Funcionalidades

- Permite ao usuário criar uma carteira de investimentos com alocações específicas para diferentes ativos.
- Calcula o **retorno esperado**, **risco (volatilidade)** e **Sharpe Ratio** da carteira.
- Baixa automaticamente os dados históricos de preços de ações usando a API `yfinance`.
- Visualiza o desempenho da carteira ao longo do tempo através de gráficos.
- Realiza **Simulação de Monte Carlo** para prever cenários futuros da carteira.

## Tecnologias Utilizadas

- **Python 3.9+**
- **Pandas**: Manipulação de dados.
- **yfinance**: Obtenção de dados financeiros.
- **Matplotlib**: Visualização de dados.
- **Numpy**: Cálculos matemáticos e simulação.

## Instalação

1. Clone este repositório:
    ```bash
    git clone https://github.com/thiagogilcamargo/investment-portfolio-simulator.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd simulador-carteira-investimentos
    ```
3. Instale as dependências necessárias:
    ```bash
    pip install -r requirements.txt
    ```

## Como Usar

1. Execute o script principal `main.py`:
    ```bash
    python main.py
    ```

2. O simulador solicitará a escolha dos ativos e suas respectivas alocações. Exemplo de ativos pré-definidos no código:
    - **AAPL** (Apple)
    - **MSFT** (Microsoft)
    - **GOOGL** (Google)
    - **TSLA** (Tesla)
  
   As alocações são definidas em percentual e devem somar 100% (exemplo: `[0.3, 0.2, 0.3, 0.2]`).

3. O simulador então:
    - Baixa os dados históricos dos ativos.
    - Calcula o retorno e risco da carteira.
    - Exibe gráficos de desempenho.
    - Realiza a simulação de Monte Carlo para prever o comportamento futuro da carteira.

## Exemplo de Resultados

- **Retorno esperado**: 12.50%
- **Risco (volatilidade)**: 8.75%
- **Sharpe Ratio**: 1.43

Abaixo, um gráfico será exibido mostrando o retorno cumulativo da carteira ao longo do período de análise, bem como gráficos das simulações de Monte Carlo.

## Estrutura do Projeto

```plaintext

simulador-carteira-investimentos/
│
├── main.py               # Ponto de entrada do simulador
├── portfolio.py          # Classe para gerenciar a carteira de investimentos
├── data_fetcher.py       # Função para baixar dados financeiros
├── visualizer.py         # Função para visualizar o desempenho
├── simulations.py        # Função para realizar simulação de Monte Carlo
├── README.md             # Documentação do projeto
└── requirements.txt      # Dependências do projeto

## Melhorias Futuras

- Implementar uma interface gráfica (GUI) para tornar o simulador mais interativo.
- Adicionar mais métricas financeiras, como VaR (Value at Risk) e Beta da carteira.
- Expandir a análise para incluir títulos de renda fixa e outros tipos de ativos.

## Licença

Este projeto está licenciado sob os termos da [MIT License](LICENSE).

---

Projeto desenvolvido para fins educacionais, simulando a criação de uma carteira de investimentos e utilizando técnicas de simulação para o setor financeiro.


 
