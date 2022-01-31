import plotly.graph_objects as go


fig = go.Figure([go.Bar(x = [1, 2, 3, 4], y = [31.1,50.7, 64.6, 76.5 ])])


fig.update_layout(
    title='Years at Andover vs Probability of Alcohol Consumption',
    xaxis=dict(
        title='Years at PA',
    ),
    yaxis=dict(
        title='Percent of Class That Has Consumed Alcohol',
    ),
    paper_bgcolor='rgb(243, 243, 243)',
    plot_bgcolor='rgb(243, 243, 243)',
)
fig.show()