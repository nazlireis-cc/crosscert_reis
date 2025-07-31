import streamlit as st
from streamlit_shadcn_ui import ui
import pandas as pd
import plotly.graph_objs as go

# Örnek: filtered_df yükle (gerçek projende bunu veri kaynağından alıyorsun)
# filtered_df = pd.read_csv("filtered_logs.csv")  # senin kendi datası olacak

# Test amaçlı örnek veri
data = {
    "ip": ["192.168.1.1", "192.168.1.2", "192.168.1.1"],
    "timestamp": ["2025-07-30 10:00:00", "2025-07-30 10:01:00", "2025-07-30 10:02:00"],
    "log_category": ["INFO", "ERROR", "WARN"],
    "log_message": ["Started", "Connection error", "Timeout occurred"]
}
filtered_df = pd.DataFrame(data)

# Streamlit başlığı
st.markdown("## Customer Log Activity Report")

# Başlık: Interactive Log Workflow Visualizer
st.markdown("### 🕸️ Interactive Log Workflow Visualizer")

# IP seçimi - shadcn-ui kullanılarak
ip_list = sorted(filtered_df['ip'].unique())
selected_ip = ui.select(
    label="Select IP address to view workflow",
    options=ip_list,
    key="ip_selectbox"
)

# Workflow çizimi fonksiyonu (örnek)
def draw_workflow(df, ip):
    df_ip = df[df['ip'] == ip]

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df_ip["timestamp"],
        y=df_ip["log_category"],
        mode="markers+lines+text",
        text=df_ip["log_message"],
        textposition="top center",
        marker=dict(color="LightSkyBlue", size=10)
    ))

    fig.update_layout(
        title=f"Workflow for IP: {ip}",
        xaxis_title="Timestamp",
        yaxis_title="Log Category",
        height=400
    )
    return fig, df_ip

# Grafik çizimi
if selected_ip:
    fig, df_selected = draw_workflow(filtered_df, selected_ip)
    st.plotly_chart(fig, use_container_width=True)
