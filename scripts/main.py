import yfinance as yf
import pandas as pd
from prophet import Prophet
import numpy as np

# Estabilidade dos números aleatórios
np.random.seed(42)

def gerar_dados_bi():
    # Tickers (Mantive o dólar apenas para gerar a coluna de Lag que suas medidas pedem)
    tickers = {"Brent": "BZ=F", "Dolar": "USDBRL=X", "LYB": "LYB", "WLK": "WLK"}
    data = yf.download(list(tickers.values()), period="2y", interval="1d")

    if isinstance(data.columns, pd.MultiIndex):
        data = data['Close']
    
    df = data.reset_index().rename(columns={'Date': 'ds'})
    df['ds'] = pd.to_datetime(df['ds']).dt.tz_localize(None)

    # Identificação dinâmica das colunas
    col_brent = next((c for c in df.columns if 'BZ=F' in c), "BZ=F")
    col_dolar = next((c for c in df.columns if 'USDBRL' in c), "USDBRL=X")

    # Cálculos de Negócio
    df['PS_Europa'] = df[col_brent] * 15 + 250 + np.random.normal(0, 20, len(df))
    df['Estireno_China'] = df[col_brent] * 11 + 100 + np.random.normal(0, 15, len(df))
    df['Spread_Estimado'] = df['PS_Europa'] - df['Estireno_China']
    
    # AS COLUNAS DE LAG (Garantindo que ambas existam para não quebrar o BI)
    df['Brent_Lag_30'] = df[col_brent].shift(30)
    df['Dolar_Lag_30'] = df[col_dolar].shift(30)

    # ML Prophet
    df_ml = df[['ds', 'PS_Europa', 'Brent_Lag_30']].dropna().rename(columns={'PS_Europa': 'y'})
    modelo = Prophet(daily_seasonality=False, yearly_seasonality=True)
    modelo.add_regressor('Brent_Lag_30')
    modelo.fit(df_ml)

    futuro = modelo.make_future_dataframe(periods=30)
    df_reg_total = df[['ds', 'Brent_Lag_30']].ffill()
    futuro = futuro.merge(df_reg_total, on='ds', how='left').ffill()
    previsao = modelo.predict(futuro)

    # Merge Final
    final_df = previsao[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].merge(
        df, on='ds', how='left'
    )
    
    return final_df

# O Power BI lerá este objeto
dataset = gerar_dados_bi()