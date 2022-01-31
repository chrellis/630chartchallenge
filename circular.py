import plotly.graph_objects as go

fig = go.Figure(data=[go.Scatter(
    x=['Fort Tejon', 'San Francisco', 'Eureka', 'Loma Prieta', 'Ridgecrest'], y=[1857, 1906, 1980, 1989, 2019 ],
    text=['magnitude: 7.9', 'magnitude: 7.9', 'magnitude: 7.3', 'magnitude: 6.9', 'magnitude: 6.4'],
    mode='markers',
    marker=dict(
        color=['rgb(93, 164, 214)', 'rgb(255, 144, 14)',  'rgb(44, 160, 101)', 'rgb(255, 65, 54)', 'rgb(252, 3, 190)'],
        size=[79, 79, 73, 69, 64],
    )
)])

fig.update_layout(
    title='Monumental California Earthquakes',
    xaxis=dict(
        title='Location',
    ),
    yaxis=dict(
        title='Year',
    ),
    paper_bgcolor='rgb(243, 243, 243)',
    plot_bgcolor='rgb(243, 243, 243)',
)

fig.show()

