import pandas as pd
import streamlit as st
import joblib
import locale

st.set_page_config(
    page_title="ValorAuto", 
    page_icon="",
    layout="wide",
    menu_items={
        'Get Help': 'mailto:kensleyw@gmail.com',
        'Report a bug': "mailto:kensleyw@gmail.com",
         'About': "**Objetivo** Construir uma máquina preditiva para prever o preço de venda dos carros da empresa. Esse processo de previsão vai automatizar e otimizar a definição dos preços dos carros que serão vendidos pelo app."
         }
    )

## altera o style da página
st.markdown("""
    <style>
    .st-emotion-cache-z5fcl4 {
        padding: 2rem 1rem 10rem;
        padding-left: 5rem;
        padding-right: 5rem;
    }
    </style>
""", unsafe_allow_html=True)

st.header("ValorAuto App")
st.write("Precificação inteligente, transparência total, e o caminho certo para a valorização do seu carro!")

st.markdown("****")
st.subheader("**Preencha os dados do seu veículo:**")

col1, col2 = st.columns(2, gap='large')
# Mapeamento de valores numéricos para rótulos descritivos
mapeamento_rotulos = {-3: "Risco Muito Alto", -2: "Risco Alto", -1: "Risco Moderado", 0: "Sem Risco", 1: "Risco Baixo", 2: "Risco Muito Baixo", 3: "Risco Mínimo"}

# Adicione o slider
portas = col1.selectbox("Portas", options=['2', '4+'])

potencia = col1.number_input(label="Potência (cv)", min_value=0)

carroceria = col1.selectbox("Carroceria", options=['Hatch', 'Sedan', 'Conversível', 'Wagon'])

risco = col2.select_slider("Nível de Segurança", options=list(mapeamento_rotulos.keys()), format_func=lambda valor: mapeamento_rotulos[valor], value=0)

turbo = col2.checkbox("Motor Turbo")

diesel = col2.checkbox("Combustivel Diesel")

tracao = col2.radio("Tração", options=['Dianteira', 'Traseira', '4 x 4'])

btn_analise = col1.button("Realizar análise")

st.markdown("****")

def transforma_dados_dataframe():
    dic_dados = {}

    dic_dados['risco'] = risco
    dic_dados['turbo'] = turbo
    dic_dados['portas_4mais'] = 1 if portas == '4+' else 0
    dic_dados['potencia'] = potencia
    dic_dados['combustivel_diesel'] = diesel
    dic_dados['carroceria_conversível'] = 1 if carroceria == 'Conversível' else 0
    dic_dados['carroceria_hatch'] = 1 if carroceria == 'Hatch' else 0
    dic_dados['carroceria_sedan'] = 1 if carroceria == 'Sedan' else 0
    dic_dados['tracao_4x4'] = 1 if tracao == '4 x 4' else 0
    dic_dados['tracao_traseira'] = 1 if tracao == 'Traseira' else 0

    return pd.DataFrame([dic_dados])

def realizar_analise(dados):
    modelo = joblib.load("modelo.joblib")
    
    resultado = modelo.predict(dados)
    return resultado 
if btn_analise:
    st.subheader("Resultado da análise")
    veiculo = transforma_dados_dataframe()
    
    resultado = realizar_analise(veiculo)[0]*10 

    valor_formatado = "{:,.2f}".format(resultado).replace("," , "-").replace(".", ",").replace("-", ".")

    st.success(f"Valor aproximado do veículo: **R$ {valor_formatado}**")

    st.write("**Dados enviados**")
    st.dataframe(veiculo, hide_index=True)
