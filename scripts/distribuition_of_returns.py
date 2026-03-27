import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from scipy.stats import norm, t, kurtosis


def download_data(stock, start_date, end_date):
    ticker = yf.download(stock, start=start_date, end=end_date, progress=False)

    if ticker.empty:
        raise ValueError("Nenhum dado foi baixado. Verifique o ticker ou o período.")

    data = pd.DataFrame()
    data["Price"] = ticker["Close"].squeeze()
    return data.dropna()


def calculate_returns(stock_data):
    stock_data = stock_data.copy()
    stock_data["Returns"] = np.log(stock_data["Price"] / stock_data["Price"].shift(1))
    return stock_data.dropna()


def show_distribution(returns, stock_name):
    mean = returns.mean()
    std = returns.std()

    # Curtose
    kurt = kurtosis(returns, fisher=False)         # curtose total
    excess_kurt = kurtosis(returns, fisher=True)   # excesso de curtose

    # Ajuste t de Student
    df_t, loc_t, scale_t = t.fit(returns)

    # Eixo x para as curvas
    x = np.linspace(mean - 5 * std, mean + 5 * std, 1000)

    # Curvas
    normal_curve = norm.pdf(x, mean, std)
    t_curve = t.pdf(x, df_t, loc=loc_t, scale=scale_t)

    # Gráfico
    plt.figure(figsize=(12, 6))
    plt.hist(
        returns,
        bins=120,
        density=True,
        alpha=0.6,
        color="lightgray",
        edgecolor="black",
        label="Retornos observados"
    )

    plt.plot(x, normal_curve, linewidth=2, label="Normal ajustada")
    plt.plot(x, t_curve, linewidth=2, label="t de Student ajustada")

    plt.title(f"Distribuição dos retornos logarítmicos - {stock_name}")
    plt.xlabel("Retorno logarítmico")
    plt.ylabel("Densidade")
    plt.legend()
    plt.tight_layout()
    plt.show()

    # Resultados no terminal
    print("=" * 60)
    print(f"Ativo analisado: {stock_name}")
    print("=" * 60)
    print(f"Média dos retornos: {mean:.6f}")
    print(f"Desvio-padrão: {std:.6f}")
    print(f"Curtose: {kurt:.6f}")
    print(f"Excesso de curtose: {excess_kurt:.6f}")
    print("\nParâmetros da t de Student ajustada:")
    print(f"Graus de liberdade (df): {df_t:.6f}")
    print(f"Loc: {loc_t:.6f}")
    print(f"Scale: {scale_t:.6f}")

    if excess_kurt > 0:
        print("\nInterpretação: a distribuição tem caudas mais pesadas que a Normal.")
    else:
        print("\nInterpretação: a distribuição não mostra excesso de curtose positivo relevante.")


if __name__ == "__main__":
    stock = "VALE3.SA"
    start_date = "2010-01-01"
    end_date = "2025-12-31"

    stock_data = download_data(stock, start_date, end_date)
    stock_data = calculate_returns(stock_data)

    show_distribution(stock_data["Returns"], stock)