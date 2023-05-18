import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from collections import namedtuple
import pandas as pd

HEADER_COLS = 3
CONS_ICON = "images/cons.png"
VOTE_ICON = "images/vote.png"
AGENT_ICON = "images/agent.png"

Metric = namedtuple("Metric", field_names=["name", "value"])


def generate_metrics(metric_map, key):
    val = metric_map.get(key, None)
    if len(val) > 1:
        key = "ALL"
    else:
        key = val[0]

    return Metric(name=key, value=len(val))


class Header:
    def __init__(self, constituencies, pollingbooths, agents):
        """
        constituencies : dict
        pollingbooths : dict
        agents: dict

        """
        self.title = "Voter Data Analytics Dashboard"
        self.constituencies = constituencies
        self.pollingbooths = pollingbooths
        self.agents = agents
        self.metrics_constituencies = generate_metrics(
            constituencies, "constituency_name"
        )
        self.metrics_pollingbooths = generate_metrics(pollingbooths, "polling_booth")
        self.metrics_agents = generate_metrics(agents, "agent_name")

    def render(self):
        header_left, title_mid, header_right = st.columns([1, 2, 2], gap="small")
        with header_left:
            col1, col2 = st.columns(2)
            with col1:
                st.image(image=CONS_ICON, use_column_width="Auto")
                st.write(self.metrics_constituencies.name)
            with col2:
                st.image(image=VOTE_ICON, use_column_width="Auto")
                st.write(self.metrics_pollingbooths.name)

        with title_mid:
            st.title(self.title)

        with header_right:
            col3, col4, col5 = st.columns(3)
            with col3:
                st.metric(label="Constituency", value=self.metrics_constituencies.value)
            with col4:
                st.metric(label="Polling Booth", value=self.metrics_pollingbooths.value)
            with col5:
                st.image(image=AGENT_ICON, use_column_width="Auto")
                st.write(self.metrics_agents.name)
        st.divider()

class KPIMetrics:
    def __init__(self, metrics) -> None:
        self.metrics = metrics

    def render(self):
        cols = st.columns(len(self.metrics.keys()) * [1], gap="medium")
        for i, key in enumerate(self.metrics):
            with cols[i]:
                st.metric(label=key, value=self.metrics.get(key, ""))
         

class ChartsSection:
    def __init__(
        self, chart_metrics, gauge_metrics, table_metrics, piechart_metrics
    ) -> None:
        self.chart_metrics = chart_metrics
        self.gauge_metrics = gauge_metrics
        self.table_metrics = table_metrics
        self.piechart_metrics = piechart_metrics

    def render(self):
        cols = st.columns(len(self.chart_metrics.keys()) * [1], gap="small")
        for i, key in enumerate(self.chart_metrics):
            with cols[i]:
                data = self.chart_metrics[key]["data"]
                chart_type = self.chart_metrics[key].get("chart_type", "table")

                if chart_type == "bar":
                    df = pd.DataFrame(data)
                    fig = px.bar(
                        df,
                        x=self.chart_metrics[key]["x"],
                        y=self.chart_metrics[key]["y"],
                        title=key,
                    )
                    fig.update_layout(autosize=False, width=200, height=300)
                    st.plotly_chart(fig, use_container_width=True)
                elif chart_type == "gauge":
                    fig = go.Figure(
                        go.Indicator(
                            mode="gauge+number+delta",
                            value=data.get("value", 2),
                            delta={"reference": data.get("reference", 1)},
                            gauge={"axis": {"range": [None, 5]}},
                            domain={"x": [0, 1], "y": [0, 1]},
                            title={"text": key},
                        )
                    )
                    fig.update_layout(autosize=True, width=300, height=400)
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    df = pd.DataFrame(data)
                    st.dataframe(df, use_container_width=False, width=400, height=200)
 

        gcols = st.columns(len(self.gauge_metrics.keys()) * [1], gap="small")
        for i, key in enumerate(self.gauge_metrics):
            with gcols[i]:
                data = self.gauge_metrics[key]["data"]
                chart_type = self.gauge_metrics[key].get("chart_type", "table")
                if chart_type == "gauge":
                    fig = go.Figure(
                        go.Indicator(
                            mode="gauge+number+delta",
                            value=data.get("value", 2),
                            delta={"reference": data.get("reference", 1)},
                            gauge={"axis": {"range": [None, 5]}},
                            domain={"x": [0, 1], "y": [0, 1]},
                            title={"text": key},
                        )
                    )
                    fig.update_layout(autosize=False, width=300, height=400)
                    st.plotly_chart(fig, use_container_width=True)
 
        pcols = st.columns(len(self.piechart_metrics.keys()) * [1], gap="small")
        for i, key in enumerate(self.piechart_metrics):
            data = self.piechart_metrics[key]["data"]
            chart_type = self.piechart_metrics[key].get("chart_type", "table")
            labels = data["labels"]
            values = data["values"]
            with pcols[i]:
                if chart_type == "donut":
                    fig = go.Figure(
                        data=[go.Pie(labels=labels, values=values, hole=0.3)]
                    )
                    fig.update_layout(
                        #legend=dict(yanchor="bottom", y=0.99, xanchor="right", x=0.01),
                        title_text=key,
                        autosize=False,
                        width=300,
                        height=400,
                    )
                    st.plotly_chart(fig, use_container_width=True)
 

class MainPage:
    def __init__(self, header, detail):
        self.header = header
        self.detail = detail

    def render_page(self):
        pass
