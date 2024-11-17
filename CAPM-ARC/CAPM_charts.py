import plotly.graph_objects as go
import plotly.express as px

def interactive_plot(df):
   
    fig = go.Figure()
    for col in df.columns[1:]:  # Assuming the first column is 'Date'
        fig.add_trace(go.Scatter(x=df["Date"], y=df[col], mode='lines', name=col))
    fig.update_layout(
        title="Interactive Stock Price Visualization",
        xaxis_title="Date",
        yaxis_title="Normalized Price",
        autosize=True,
        width=1420,
        height=500,
        margin=dict(
            l=50,
            r=50,
            t=50,
            b=50
        ),
        template="plotly_dark"
    )
    return fig


def scatter_plot(df, x_column, y_column, title="Scatter Plot", color=None):
   
    fig = px.scatter(
        df,
        x=x_column,
        y=y_column,
        color=color,
        title=title,
        template="plotly_dark",
        height=500,
        width=1200,
    )
    fig.update_layout(
        margin=dict(l=50, r=50, t=50, b=50),
        xaxis_title=x_column,
        yaxis_title=y_column,
    )
    return fig


def bar_chart(df, x_column, y_column, title="Bar Chart", color=None):
 
    fig = px.bar(
        df,
        x=x_column,
        y=y_column,
        color=color,
        title=title,
        template="plotly_dark",
        height=500,
        width=1200,
    )
    fig.update_layout(
        margin=dict(l=50, r=50, t=50, b=50),
        xaxis_title=x_column,
        yaxis_title=y_column,
    )
    return fig


def histogram(df, column, title="Histogram", nbins=20):
  
    fig = px.histogram(
        df,
        x=column,
        title=title,
        nbins=nbins,
        template="plotly_dark",
        height=500,
        width=1200,
    )
    fig.update_layout(
        margin=dict(l=50, r=50, t=50, b=50),
        xaxis_title=column,
        yaxis_title="Frequency",
    )
    return fig
