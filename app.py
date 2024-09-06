from dash import Dash, html

app = Dash(__name__)

app.layout = [html.Div(children='Hello World')]

if__name__ == '__main__':
app.run(debug=True)
