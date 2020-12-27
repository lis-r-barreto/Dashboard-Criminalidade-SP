# imporat pacotes
import streamlit as st
import pandas as pd
import pydeck as pdk

# carregar os meus dados
df = pd.read_csv('criminalidade_sp_2.csv')


# dashboard
st.title("Criminalidade em São Paulo")
st.markdown(
    """
    A **criminalidade** é um problema recorrente no Brasil.
    Buscamos sempre formas de diminuir esses índices e usando técnicas de Ciências de Dados conseguimos 
    entender melhor o que está acontecendo e gerar insights que direcionem ações capazes de diminuir os 
    índices de criminalidade.
    """
)

# sidebar
st.sidebar.info("Foram carregadas {} linhas.".format(df.shape[0]))

if st.sidebar.checkbox("Ver tabela com dados"):
    st.header("Raw Data")
    st.write(df)

df.time = pd.to_datetime(df.time)
ano_selecionado = st.sidebar.slider("Selecione um ano", 2010, 2018, 2015)
df_selected = df[df.time.dt.year == ano_selecionado]

# st.map(df_selected)
# mapa
st.subheader("Mapa da Criminalidade")
# st.map(df)
st.pydeck_chart(pdk.Deck(
    initial_view_state=pdk.ViewState(
        latitude=-23.567145	,
        longitude=-46.648936,
        zoom=8,
        pitch=50
    ),
    layers=[
        pdk.Layer(
            'HexagonLayer',
            data=df_selected[['latitude', 'longitude']],
            get_position='[longitude,latitude]',
            auto_highlight=True,
            elevation_scale=50,
            pickable=True,
            elevation_range=[0, 3000],
            extruded=True,
            coverage=1
        )
    ],
))
