"""
OneClick Lending Dashboard - Streamlit App
Ejecutar con: streamlit run app.py

Dependencias necesarias:
pip install streamlit pandas plotly

O crear requirements.txt con:
streamlit==1.32.2
pandas==2.2.1
plotly==5.19.0
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Configuración de página
st.set_page_config(
    page_title="OneClick Lending - Font Mercedes Isabel",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS personalizado para responsive
st.markdown("""
<style>
    .main {
        padding: 0rem 0.5rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .status-good {
        color: #00cc00;
        font-weight: bold;
    }
    .status-warning {
        color: #ff9900;
        font-weight: bold;
    }
    .status-critical {
        color: #ff0000;
        font-weight: bold;
    }
    h1, h2, h3 {
        color: #1e3d59;
    }
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
        font-size: 0.9rem;
    }
    @media (max-width: 768px) {
        .main {
            padding: 0rem 0.2rem;
        }
        h1 {
            font-size: 1.5rem;
        }
        h2 {
            font-size: 1.2rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Header
st.title("📊 OneClick Lending")
st.markdown("### Font Mercedes Isabel - CUIT: 27-03770388-0")
st.markdown("---")

# Crear tabs principales
tab1, tab2, tab3, tab4, tab5 = st.tabs(["📈 Resumen", "💰 Créditos", "🏞️ Campos", "🐄 Hacienda", "💵 Flujos"])

with tab1:
    # Métricas principales
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Score Nosis", "650", "Observado")
        st.metric("Ranking DCAC", "#15 de 10,000", "")
    with col2:
        st.metric("Créditos Totales", "$88,512", "4 créditos")
        st.metric("Estado Actual", "Al día ✅", "")
    
    # Estado de aprobación
    st.markdown("### 🎯 Estado de Aprobación")
    st.error("**NO APROBADO** - Cumple con 7 de 8 métricas (88%)")
    
    # Métricas críticas
    with st.expander("Ver métricas detalladas"):
        metrics_data = {
            "Métrica": ["Transacciones", "Pagos - Créditos", "Créditos en Bancos", 
                       "Deuda/Activos", "Deuda/Stock cría", "Servicio de deuda"],
            "Estado": ["⚠️ Límite", "⚠️ Límite", "✅ OK", "✅ OK", "⚠️ Límite", "❌ Crítico"],
            "Valor": ["En límite", "En límite", "2", "4.3%", "25%", "1"]
        }
        df_metrics = pd.DataFrame(metrics_data)
        st.dataframe(df_metrics, use_container_width=True, hide_index=True)

with tab2:
    st.markdown("### 💳 Historial Crediticio")
    
    # Resumen de créditos
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Tasa promedio", "50%", "")
        st.metric("Demora promedio", "+8 días", "")
    with col2:
        st.metric("Total en créditos", "$88,512", "")
        st.metric("Promedio por crédito", "$22,128", "")
    
    # Gráfico de pagos
    fig_pagos = go.Figure(data=[
        go.Pie(
            labels=['A Término', 'Con Demora'],
            values=[2, 2],
            hole=.5,
            marker_colors=['#00cc00', '#ff9900']
        )
    ])
    fig_pagos.update_layout(height=300, showlegend=True)
    st.plotly_chart(fig_pagos, use_container_width=True)
    
    # Evolución de transacciones
    st.markdown("### 📊 Evolución de Transacciones")
    years = [2019, 2020, 2021, 2022, 2023, 2024]
    transactions = [800, 5000, 8000, 10000, 12500, 15000]
    
    fig_trans = go.Figure()
    fig_trans.add_trace(go.Bar(x=years, y=transactions, marker_color='#4a86e8'))
    fig_trans.update_layout(height=300)
    st.plotly_chart(fig_trans, use_container_width=True)

with tab3:
    st.markdown("### 🌾 Activos Inmobiliarios")
    
    # Resumen de campos
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total hectáreas", "5,534", "")
    with col2:
        st.metric("Hectáreas agrícolas", "3,319", "")
    with col3:
        st.metric("Valor estimado", "$10.6M USD", "")
    
    # Tabla de campos
    st.markdown("### 📍 Detalle de Campos")
    campos_data = {
        "Localidad": ["Hale", "Carmen de Areco", "Olavarría", "Mari Lauquen"],
        "Hectáreas": [2300, 232, 982, 1920],
        "Tipo": ["Mixto", "Agrícola", "Mixto", "Mixto"],
        "Estado": ["Propio", "Propio", "En arrendamiento", "Propio"]
    }
    df_campos = pd.DataFrame(campos_data)
    st.dataframe(df_campos, use_container_width=True, hide_index=True)
    
    # Valuación
    st.markdown("### 💵 Valuación de Campos")
    val_data = {
        "Campo": ["Hale", "Carmen de Areco"],
        "$/ha agrícola": ["$6,750", "$12,500"],
        "Valor Total": ["$8.1M", "$2.9M"]
    }
    df_val = pd.DataFrame(val_data)
    st.dataframe(df_val, use_container_width=True, hide_index=True)

with tab4:
    st.markdown("### 🐮 Stock Ganadero")
    
    # Métricas principales
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total cabezas", "8,388", "")
    with col2:
        st.metric("Valor total", "$3.6M USD", "")
    with col3:
        st.metric("Valor stock cría", "$2.2M USD", "")
    
    # Composición del stock
    st.markdown("### 📊 Composición del Stock")
    stock_data = {
        "Categoría": ["Vacas", "Vaquillonas", "Novillos", "Terneros", "Terneras", "Otros"],
        "Cantidad": [2905, 1547, 1046, 1416, 1374, 100],
        "Valor USD": ["$1.6M", "$1.0M", "$0.9M", "$0.7M", "$0.5M", "$0.1M"]
    }
    df_stock = pd.DataFrame(stock_data)
    st.dataframe(df_stock, use_container_width=True, hide_index=True)

with tab5:
    st.markdown("### 💰 Flujo de Fondos")
    
    # Resumen anual
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Ingresos totales", "$4.0M", "")
        st.metric("Egresos totales", "$3.4M", "")
    with col2:
        st.metric("Resultado neto", "$638K", "+18.8%")
        st.metric("Necesidad de crédito", "$547K", "")
    
    # Gráfico de flujos mensuales
    st.markdown("### 📈 Flujo Mensual")
    
    months = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
    ingresos = [0, 1613, 1357, 423, 0, 0, 0, 203, 162, 0, 0, 249]
    egresos = [122, 732, 486, 258, 82, 173, 78, 198, 547, 100, 337, 253]
    
    fig_flujo = go.Figure()
    fig_flujo.add_trace(go.Bar(name='Ingresos', x=months, y=ingresos, marker_color='#00cc00'))
    fig_flujo.add_trace(go.Bar(name='Egresos', x=months, y=egresos, marker_color='#ff6666'))
    fig_flujo.update_layout(barmode='group', height=350)
    st.plotly_chart(fig_flujo, use_container_width=True)
    
    # Ratios financieros
    st.markdown("### 📊 Ratios Financieros")
    ratios_data = {
        "Indicador": ["Deuda/Activo total", "Deuda/Stock cría", "Deuda/Campo", "Garantías reales"],
        "Valor": ["3.8%", "25%", "5.1%", "$12.8M USD"]
    }
    df_ratios = pd.DataFrame(ratios_data)
    st.dataframe(df_ratios, use_container_width=True, hide_index=True)

# Footer
st.markdown("---")
st.markdown("##### 📅 Abril 2025 | deCampo Campo & Riverwood Ag")
