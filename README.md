# estireno

# 📊 Predição de Preços: Estireno (Europa vs. China)

**Status do Projeto:** 🟢 Operacional *(Atualizado via Personal Gateway)*

<p align="center">
<img src="images/preview_dashboard.jpg" alt="Preview do Dashboard de Estireno" width="800">
</p>

<p align="center">
<a href="https://app.powerbi.com/view?r=eyJrIjoiNGJkZDE4MmItYzE2OC00MGU4LTliNzgtODljZWYyNmIxOWI0IiwidCI6IjkxZTdhZTIzLTdkOGYtNGYwNC1hZDZhLWNkYTgzNTEyZDY1OSJ9" target="_blank">
🚀 <b>Clique aqui para acessar o Dashboard Interativo</b>
</a>
</p>

---

## 📝 Descrição do Projeto

Este projeto integra uma pipeline de dados em Python com um dashboard de Business Intelligence para prever a volatilidade do mercado petroquímico europeu. O foco central é a relação de preços do Poliestireno (PS) entre a Europa e a China, utilizando o Petróleo Brent como o principal driver de custo.

Os dados utilizados são provenientes de fontes públicas e mercados financeiros reais (via Yahoo Finance), coletados exclusivamente para fins de estudo, treinamento e demonstração de competências técnicas em Engenharia de Dados e Machine Learning.

## ⚙️ Arquitetura e Automação

Diferente de modelos estáticos, este projeto é um ecossistema vivo:

* **Coleta diária:** Um script Python executa rotinas de limpeza e modelagem diariamente.
* **Pipeline de Dados:** A extração é feita via biblioteca `yfinance`, garantindo dados atualizados de fechamento de mercado.
* **Integração em Nuvem:** O processamento ocorre localmente em um ambiente Miniconda, mas os resultados são enviados automaticamente para o Power BI Service através de um Microsoft Personal Gateway. Isso permite que o dashboard reflita as condições de mercado do dia anterior sem intervenção manual.

## 🔬 Metodologia e Machine Learning

### O Modelo Prophet "Sob o Capô"

Para a previsão de séries temporais, foi utilizado o **Facebook Prophet**, um modelo aditivo decomponível que trata dados de séries temporais como uma combinação de tendências em diferentes escalas.

A base matemática do modelo segue a fórmula:

$$y(t) = g(t) + s(t) + h(t) + \epsilon_t$$

**Onde:**
* $g(t)$ **(Tendência):** Modela mudanças não periódicas. No caso do Estireno, captura o crescimento ou declínio de longo prazo do mercado.
* $s(t)$ **(Sazonalidade):** Modela mudanças periódicas (semanal, mensal, anual) usando Séries de Fourier. Essencial para captar ciclos de manutenção de plantas petroquímicas e variações de demanda sazonal.
* $h(t)$ **(Feriados/Eventos):** Considera o efeito de datas específicas (como o Ano Novo Chinês) que impactam drasticamente o volume de negociação.
* $\epsilon_t$ **(Erro):** Representa variações atípicas não explicadas pelo modelo.

> **💡 Regressores Externos:** O modelo foi potencializado com a inclusão do `Brent_Lag_30`. Como o petróleo é a matéria-prima base, sua variação hoje impacta o preço do polímero físico em aproximadamente 30 dias. Esta variável exógena reduz significativamente o erro médio (MAE) da predição.

### 📖 Dicionário de Dados (Colunas Geradas)

* `ds`: Timestamp (Eixo temporal da análise).
* `PS_Europa`: Preço real de mercado do Poliestireno no continente europeu.
* `yhat`: A estimativa central ("preço justo") calculada pelo Machine Learning.
* `yhat_lower` / `yhat_upper`: Intervalo de confiança da previsão (Bandas de incerteza).
* `Estireno_China`: Preço de referência do mercado asiático (Benchmark global).
* `BZ=F`: Cotação em tempo real do Petróleo Brent.
* `Brent_Lag_30`: O valor do Brent deslocado em 30 dias para análise de correlação tardia.
* `Spread_Estimado`: Diferencial bruto entre os preços da Europa e China.

## 📊 Visualizações e Inteligência de Negócio

O dashboard foi estruturado em três páginas lógicas para facilitar a extração de insights:

### 1. Panorama e Forecast
Focada em *"O que aconteceu e o que virá"*.
* **Fan Chart:** Exibe o preço real contra a previsão do Prophet. As bandas de incerteza permitem que o gestor avalie o risco de volatilidade.
* **Análise Lead-Lag:** Um gráfico de eixos alinhados que sobrepõe o Brent de 30 dias atrás com o preço do PS de hoje, visualizando graficamente o repasse de custos na cadeia produtiva.

### 2. Correlação de Mercado
Focada em *"Por que aconteceu"*.
* **Dispersão de Ações (Scatter Plot):** Correlaciona o preço físico do PS com o valor das ações de grandes players (LYB/WLK). Pontos fora da curva de tendência indicam momentos de descolamento entre o mercado financeiro e a economia real.
* **Velocímetro de Spread:** Um KPI visual que monitora a saúde da margem europeia. Se o ponteiro entra na zona vermelha, a produção local está sob estresse de custos.

### 3. Simulador de Arbitragem
Focada em *"E se acontecer?"*.
* **What-if Simulator:** Permite ao usuário simular variações percentuais no preço da China.
* **Gráfico de Rosca (Composição de Preço):** Mostra quanto do preço europeu é composto pelo "piso" chinês vs. o "prêmio regional". Se o prêmio europeu cresce demais, o gráfico indica um alto risco de invasão de produtos importados da Ásia por arbitragem.

## 🚀 Tecnologias Utilizadas

* **Linguagem:** Python 3.10+
* **Bibliotecas ML:** Facebook Prophet, Pandas, NumPy
* **Data Source:** yFinance API
* **BI:** Power BI Desktop & Service (DAX Avançado)
* **Ambiente:** Miniconda (Gestão de ambientes e Gateway)

---

Desenvolvido por **Renato Benevenuto** *Engenheiro Civil | Especialista em Gestão de Projetos | Aspirante a Data Scientist*
