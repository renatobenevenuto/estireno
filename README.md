# 📊 Predição de Preços: Estireno (Europa vs. China)

**Status do Projeto:** 🟢 Operacional *(Atualizado via Personal Gateway)*

<p align="center">
<img src="images/preview_dashboard.jpg" alt="Preview do Dashboard de Estireno" width="800">
</p>

<p align="center">
<a href="[https://app.powerbi.com/view?r=eyJrIjoiNGJkZDE4MmItYzE2OC00MGU4LTliNzgtODljZWYyNmIxOWI0IiwidCI6IjkxZTdhZTIzLTdkOGYtNGYwNC1hZDZhLWNkYTgzNTEyZDY1OSJ9](https://app.powerbi.com/view?r=eyJrIjoiNGJkZDE4MmItYzE2OC00MGU4LTliNzgtODljZWYyNmIxOWI0IiwidCI6IjkxZTdhZTIzLTdkOGYtNGYwNC1hZDZhLWNkYTgzNTEyZDY1OSJ9)" target="_blank">
<b>🚀 Clique aqui para acessar o Dashboard Interativo</b>
</a>
</p>

---

## 📝 Descrição do Projeto

Este projeto integra uma pipeline de dados em **Python** com um dashboard de **Business Intelligence** para prever a volatilidade do mercado petroquímico europeu. O foco central é a relação de preços do Poliestireno (PS) entre a Europa e a China, utilizando o Petróleo Brent como o principal driver de custo.

Os dados são extraídos em tempo real via Yahoo Finance, processados em ambiente Miniconda e automatizados para refletir as condições diárias do mercado global.

---

## 💡 Guia de Decisão Estratégica (Manual do Usuário)

Este dashboard foi desenhado para apoiar profissionais de **Suprimentos e Supply Chain** em quatro frentes analíticas:

1.  **Planejamento de Compras (Página 1):** Identifica se o momento é de antecipar ordens ou operar *hand-to-mouth* baseado na tendência do Prophet.
2.  **Gestão de Risco (Página 1):** Utiliza a **Sensibilidade Dinâmica** para prever o impacto de variações do petróleo no custo do polímero em 30 dias.
3.  **Sentimento de Mercado (Página 2):** Monitora a correlação ($R^2$) entre ações petroquímicas (**LYB/WLK**) e o preço físico.
4.  **Estratégia de Negociação (Página 3):** Simula choques no mercado chinês para estabelecer preços-teto de negociação.
5.  **Terminal de Suprimentos (Página 4):** Central de execução que fornece recomendações diretas ("Buy/Wait") e cálculos de desembolso financeiro.

---

## 🔬 Metodologia e Machine Learning

### O Modelo Prophet "Sob o Capô"
A base matemática segue a lógica aditiva: $y(t) = g(t) + s(t) + h(t) + \epsilon_t$, onde capturamos tendência, sazonalidade e feriados asiáticos, potencializados pelo regressor externo `Brent_Lag_30`.

### O Índice de Oportunidade ($I_o$)
Desenvolvemos um indicador proprietário para a recomendação automática:
$$I_o = \frac{P_{atual}}{\overline{P}_{90d}} \cdot \left( \frac{\hat{y}_{t+30}}{P_{atual}} \right)$$

* **$I_o < 1$ (Oportunidade):** Preço abaixo da média trimestral com previsão estável/queda.
* **$I_o > 1$ (Risco):** Mercado sobrevalorizado ou com alta projetada agressiva.

---

## ⚙️ Operação da Página 4: Terminal de Suprimentos

A Página 4 funciona como um **SAD (Sistema de Apoio à Decisão)** prescritivo. Abaixo, detalhamos como operar e interpretar este terminal:

### 1. Market Outlook (Relatório Dinâmico em Scroll)
* **O que indica:** Um letreiro digital (estilo Bloomberg) que processa as variáveis de mercado via DAX e gera uma recomendação textual em tempo real.
* **Como ler:** O texto avalia se o preço atual está "Caro" ou "Barato" frente à média e sugere a ação imediata (ex: "Momento ótimo para fechar volumes").

### 2. Calculadora de Desembolso e Sliders de Simulação
* **Slider de Volume (ton):** Permite ao comprador simular a quantidade que pretende adquirir.
* **Slider de Frete (USD/t):** Permite ajustar o custo logístico estimado de importação da Ásia.
* **Visual de Desembolso:** Um cartão que elimina valores nulos (COALESCE) e mostra o investimento total necessário para a carga simulada.

### 3. Gráfico de Tendência (Momentum 90 dias)
* **O que indica:** Um "zoom" no último trimestre. Possui uma **Linha de Constante Dinâmica** que marca a média móvel de 90 dias.
* **Interpretação:** Se o preço real cruzar a média para baixo, confirma-se o fim da pressão de alta. O gráfico ajuda a identificar o "fundo" do mercado para compras em larga escala.

### 4. Gráfico de Cascata (Waterfall de Landed Cost)
* **O que indica:** Descompõe o preço europeu partindo da China.
* **Composição:** `Preço China` + `Custo Logístico` + `Prêmio Regional` = `Preço Europa`.
* **Como operar:** Ao mover o slider de frete, o **Prêmio Regional** recalcula-se. Se o prêmio for alto, significa que o fornecedor europeu tem margem para dar desconto.

### 5. Cards com Iconografia Delta
* **O que indica:** Exibe o preço atual e a variação em relação à média de 90 dias.
* **Visual:** Utiliza ícones dinâmicos (▼/▲) e cores (Verde/Vermelho) via formatação condicional para indicar se o comprador está pagando acima ou abaixo do benchmark histórico.

---

## 🎯 Por que esta página é estratégica?

O **Terminal de Suprimentos** transforma dados em poder de barganha:

1.  **Landed Cost Analysis:** Ao ajustar o slider de frete, o comprador descobre se a inflação do produto é logística ou se é um "prêmio" excessivo cobrado pelo fornecedor local.
2.  **Argumentação Técnica:** O comprador não negocia baseado em "achismo", mas em um diferencial comprovado em relação à arbitragem transcontinental.
3.  **Planejamento de Caixa:** A calculadora de desembolso permite previsões rápidas de fluxo de caixa para a diretoria financeira.
4.  **Mitigação de Erro Humano:** O relatório automático (Market Outlook) remove o viés emocional, mantendo a estratégia fiel aos fundamentos matemáticos do modelo.

---

## 🛠️ Glossário Técnico de Unidades

* **Polímeros (PS):** USD/t (Tonelada Métrica).
* **Petróleo (Brent):** USD/bbl (Barril).
* **Ações (LYB/WLK):** USD/share (Ação).
* **Sensibilidade:** Coeficiente de repasse $\Delta USD/t / \Delta USD/bbl$.

---

Desenvolvido por **Renato Benevenuto**
*Engenheiro Civil | MSc em Business & Finance | Data Scientist*
