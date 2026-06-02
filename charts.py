import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def create_churn_chart(df):
    churn_data = df['status'].value_counts().reset_index()
    fig = px.bar(churn_data, x='status', y='count', 
                color='status', 
                color_discrete_map={'Active': '#10b981', 'At Risk': '#f59e0b', 'Churned': '#ef4444'})
    fig.update_layout(height=400, showlegend=False, font_color='white')
    return fig

def create_revenue_chart():
    fig = px.line(x=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'], 
                  y=[20, 25, 30, 28, 35, 40],
                  markers=True, title="Revenue Trend")
    fig.update_traces(line_color='#10b981')
    fig.update_layout(height=400, font_color='white')
    return fig

def create_risk_pie(df):
    risk_data = df['churn_risk'].value_counts()
    fig = px.pie(values=risk_data.values, names=risk_data.index)
    fig.update_layout(height=400, font_color='white')
    return fig
