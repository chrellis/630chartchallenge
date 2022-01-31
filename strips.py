import plotly.express as px

fig = px.scatter(x=["boy", "boy","boy","boy","girl" ,"girl" ,"girl" ,"girl"], y=['chenault', 'emiliano', 'morgan', 'tristan', "amour", 'natasha', 'ablah', 'amara'])

fig.update_layout(
    title='Strip Plot for Friend Genders',
    xaxis=dict(
        title='Gender',
    ),
    yaxis=dict(
        title='Name',
    ),
    paper_bgcolor='rgb(243, 243, 243)',
    plot_bgcolor='rgb(243, 243, 243)',
)


fig.show()