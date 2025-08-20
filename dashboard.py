import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np
import plotly.express as px


# -------------------------------------------------
# 1. Page config
# -------------------------------------------------
st.set_page_config(
    page_title="Best Games Dashboard",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -------------------------------------------------
# 2. Load & preprocess
# -------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("Best_Games_of_All_Time.csv")
    df["Launch_date"] = pd.to_datetime(df["Launch_date"], errors="coerce")
    df["Year"] = df["Launch_date"].dt.year
    df["Metascore"] = pd.to_numeric(df["Metascore"], errors="coerce")
    df = df.dropna(subset=["Metascore", "Year"])
    df["Decade"] = (df["Year"] // 10) * 10
    return df

df = load_data()

# -------------------------------------------------
# 3. Header
# -------------------------------------------------
st.title("🎮 Best Games of All Time — Interactive Dashboard")
st.markdown("Explore 500+ top-rated video games across 3 decades.")

# -------------------------------------------------
# 4. KPI Row
# -------------------------------------------------
kpi1, kpi2, kpi3 = st.columns(3)
kpi1.metric("Total Games", len(df))
kpi2.metric("Avg Metascore", f"{df['Metascore'].mean():.1f}")
kpi3.metric("Top Score", df["Metascore"].max())

# -------------------------------------------------
# 5. Filters
# -------------------------------------------------
with st.sidebar:
    st.header("🔍 Filters")
    score_range = st.slider("Metascore range", 70, 100, (70, 100))
    year_range  = st.slider("Year range", int(df["Year"].min()), int(df["Year"].max()), (1995, 2025))
    rating_sel  = st.multiselect("ESRB Rating", options=sorted(df["Rating"].dropna().unique()), default=sorted(df["Rating"].dropna().unique()))

mask = (
    (df["Metascore"] >= score_range[0]) &
    (df["Metascore"] <= score_range[1]) &
    (df["Year"] >= year_range[0]) &
    (df["Year"] <= year_range[1]) &
    (df["Rating"].isin(rating_sel))
)
filtered = df[mask]

# -------------------------------------------------
# 6. Charts
# -------------------------------------------------

st.subheader("📈 Metascore vs Year (Density)")
fig = px.density_heatmap(
        filtered,
        x="Year",
        y="Metascore",
        nbinsx=30,
        nbinsy=20,
        color_continuous_scale="Viridis",
        height=400
)
fig.update_layout(margin=dict(l=0, r=0, t=30, b=0))
st.plotly_chart(fig, use_container_width=True)


st.subheader("📈 Metascore vs Year (Jittered)")
fig = px.strip(
        filtered,
        x="Year",
        y="Metascore",
        color="Rating",
        hover_name="Name",
        color_discrete_map={
            "E": "#4daf4a", "E10+": "#377eb8", "T": "#ff7f00",
            "M": "#e41a1c", "K-A": "#984ea3"
        },
        stripmode="overlay",  # keeps jitter
        height=400
)
fig.update_layout(margin=dict(l=0, r=0, t=30, b=0))
st.plotly_chart(fig, use_container_width=True)



st.subheader("📈 Metascore vs Year (Top-N per Year)")
top_n = st.slider("Show top-N games per year", 1, 10, 3)

top_each = (filtered.sort_values("Metascore", ascending=False)
                    .groupby("Year")
                    .head(top_n))

fig = px.scatter(
        top_each,
        x="Year",
        y="Metascore",
        color="Rating",
        hover_name="Name",
        size="Metascore",
        color_discrete_map={
            "E": "#4daf4a", "E10+": "#377eb8", "T": "#ff7f00",
            "M": "#e41a1c", "K-A": "#984ea3"
        },
        height=400
)
fig.update_layout(margin=dict(l=0, r=0, t=30, b=0))
st.plotly_chart(fig, use_container_width=True)


st.subheader("🎯 Top 10 Highest Rated")
top10 = filtered.nlargest(10, "Metascore")[["Name", "Metascore"]]
st.dataframe(top10.style.highlight_max(subset=["Metascore"], color="#ff4b4b"))

# -------------------------------------------------
# 7. Row 2 – Heatmap & Word Cloud
# -------------------------------------------------

st.subheader("🔥 Heatmap: Games per Decade & Tier")
tier = pd.cut(filtered["Metascore"], bins=[0,85,90,95,100], labels=["Good","Great","Superb","Perfect"])
heat = filtered.groupby(["Decade", tier]).size().unstack(fill_value=0)
fig2 = px.imshow(heat.T, aspect="auto", color_continuous_scale="YlOrRd")
fig2.update_layout(height=350, margin=dict(l=0, r=0, t=30, b=0))
st.plotly_chart(fig2, use_container_width=True)


st.subheader("💬 Word Cloud from Game Details")
text = " ".join(filtered["Details"].dropna().astype(str))
wc = WordCloud(width=600, height=350, background_color="white", colormap="plasma").generate(text)
fig3, ax = plt.subplots(figsize=(6,3.5))
ax.imshow(wc, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig3)

