import streamlit as st
import requests
import pandas as pd

def map_names_to_ids(selected_names, name_id_mapping):
    if isinstance(selected_names, list):
        return [name_id_mapping[name] for name in selected_names]
    else:
        return [name_id_mapping[selected_names]]

# Título da aplicação
st.title("Previsão do Modelo")

# Suponha que você tenha um dataframe champs com as colunas "name" e "id"
champs = pd.read_csv("/opt/render/project/src/output_etl/champs_output_etl.csv")
participants = pd.read_csv("/opt/render/project/src/output_etl/participants_output_etl.csv")

# Inputs para coletar dados do usuário
positions = st.selectbox("Escolha 5 roles:", list(participants["position"].unique()))
bans = st.multiselect("Escolha 3 bans:", list(champs["name"].unique()))
pick = st.selectbox("Escolha 1 pick:", list(champs["name"].unique()))

# Escolher a posição da coluna alvo (onde o valor True deve ser colocado)
#target_column_index = st.selectbox("Escolha a posição da coluna alvo:", range(len(df_model.columns)))

# Botão para fazer a previsão
if st.button("Fazer Previsão"):
    # Mapear nomes para IDs usando o dataframe champs
    bans_ids = map_names_to_ids(bans, dict(zip(champs["name"], champs["id"])))
    picks_ids = map_names_to_ids(pick, dict(zip(champs["name"], champs["id"])))

    # Criar payload com dados de entrada
    payload = {
        "picks": picks_ids,
        "positions": positions,
        "bans": bans_ids,
        #"target_column_index": target_column_index
    }

    # Exibir o conteúdo do payload no console do Streamlit
    st.write("Conteúdo do payload:", payload)

    # Fazer uma solicitação POST para a API
    response = requests.post("https://api-predict-ickm.onrender.com/predict", json=payload)

    # Exibir resultado da previsão
    if response.status_code == 200:
        result = response.json()
        result_formatted = round((float(result['output']) * 100), 2) 
        st.success(f"Previsão do Modelo: {result_formatted} % de chance de vitória")
    else:
        st.error(f"Erro ao fazer a previsão. Código de status: {response.status_code}")
