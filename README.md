# CAPM Analysis em Python

Este projeto implementa o modelo de precificação de ativos (CAPM) utilizando dados reais de mercado, com foco na estimação empírica e interpretação econômica dos resultados.

<img width="924" height="540" alt="CAPM VALE3 vs BVSP" src="https://github.com/user-attachments/assets/269e8715-f3df-4664-86e7-20171d819628" />

---

## Objetivo

Analisar a relação entre risco e retorno de um ativo em relação ao mercado, estimando:

- Beta (risco sistemático)
- Alpha (retorno anormal)
- Significância estatística
- Poder explicativo do modelo (R²)

---

## Metodologia

1. Coleta de dados via Yahoo Finance
2. Cálculo de retornos logarítmicos mensais
3. Cálculo de retornos em excesso:

   R<sub>i</sub> − R<sub>f</sub> = α + β (R<sub>m</sub> − R<sub>f</sub>) + ε

5. Estimação via regressão OLS (statsmodels)

---

## Ferramentas

- Python
- Pandas
- NumPy
- Statsmodels
- Matplotlib
- yfinance

---

## Resultados

Exemplo de output da regressão:

- **Beta:** 0.79  
- **Alpha:** ~0 (não significativo)  
- **R²:** 0.25  

---

## Interpretação dos Resultados

### Beta
| Valor | Significado |
|---|---|
| β > 1 | Mais volátil que o mercado — sobe e cai mais |
| β = 1 | Move igual ao mercado |
| β < 1 | Menos volátil que o mercado — mais defensivo |
| β < 0 | Move na direção oposta ao mercado (raro) |

Neste caso: **β ≈ 0.79**, indicando que o ativo é menos sensível ao mercado (perfil mais defensivo).

---

### Alpha
O retorno que o ativo gerou **além do que o CAPM previa** dado seu nível de risco.

- **α > 0** → ativo superou o esperado  
- **α = 0** → retorno compatível com o risco  
- **α < 0** → desempenho abaixo do esperado  

Neste caso: **alpha não é estatisticamente significativo**, sugerindo que o ativo está corretamente precificado pelo CAPM.

---

### R²
Mede quanto da variação do ativo é explicada pelo mercado.

- **R² alto (> 0,7)** → forte dependência do mercado  
- **R² baixo (< 0,3)** → outros fatores dominam  

Neste caso: **R² ≈ 0.25**, o que é esperado para ativos individuais, indicando que o mercado explica apenas parte dos retornos.

---

### Prêmio de risco

Se \( R_m - R_f < 0 \), o mercado rendeu menos que a taxa livre de risco.

Nesse cenário, o CAPM perde interpretação econômica, pois o modelo assume prêmio de risco positivo.

Isso é relevante para o Brasil, onde houve períodos prolongados com CDI elevado.

---

## Limitações do CAPM ⚠️

1. **Um único fator**  
   Assume que apenas o mercado explica retornos — o que é insuficiente para ativos como VALE3.

2. **Taxas constantes**  
   Na prática, taxa livre de risco e retornos variam ao longo do tempo.

3. **Distribuição normal**  
   Retornos financeiros apresentam caudas gordas (eventos extremos).

4. **Hipótese de mercado eficiente**  
   Nem sempre válida na prática.

---

## Principais Insights

- O CAPM captura o risco sistemático, mas não explica totalmente os retornos
- Beta é estatisticamente significativo, indicando relação com o mercado
- O baixo R² reforça a importância de outros fatores (setor, commodities, macro)
