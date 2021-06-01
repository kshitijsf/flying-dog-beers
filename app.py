import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

# ########### Define your variables
beers=['Chesapeake Stout', 'Snake Dog IPA', 'Imperial Porter', 'Double Dog IPA']
ibu_values=[35, 60, 85, 75]
abv_values=[5.4, 7.1, 9.2, 4.3]
color1='darkred'
color2='orange'
mytitle='Beer Comparison'
tabtitle='beer!'
myheading='Flying Dog Beers'
label1='IBU'
label2='ABV'
githublink='https://github.com/austinlasseter/flying-dog-beers'
sourceurl='https://www.flyingdog.com/beers/'

########### Set up the chart
bitterness = go.Bar(
    x=beers,
    y=ibu_values,
    name=label1,
    marker={'color':color1}
)
alcohol = go.Bar(
    x=beers,
    y=abv_values,
    name=label2,
    marker={'color':color2}
)

beer_data = [bitterness, alcohol]
beer_layout = go.Layout(
    barmode='group',
    title = mytitle
)

beer_fig = go.Figure(data=beer_data, layout=beer_layout)

# customer = pd.read_csv('customer.csv')
# VALID_USERNAME_PASSWORD_PAIRS = {'hello': 'world'}

# customer_options = [{'label': i, 'value': i} for i in customer['Customer Name'].unique()]

# raw_country_list = customer['Country Name'].unique()
# cleaned_country_list = [x for x in raw_country_list if str(x) != 'nan']
# country_options = [{'label': i, 'value': i} for i in cleaned_country_list]

# employee_options = [{'label': i, 'value': i} for i in customer['Employee '].unique()]

# data_options = [{'label':'Customer Name', 'value':'Customer Name'}, {'label':'Country', 'value':'Country'}, {'label':'Employee', 'value':'Employee'}]

# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])
# server = app.server
# auth = dash_auth.BasicAuth(
#     app,
#     VALID_USERNAME_PASSWORD_PAIRS
# )
#print(cleaned_country_list)
# app.layout = html.Div([
#     html.H1('Customer Database for Traders'),
#     html.Label('Sing Fuels Proprietary Data', style={"fontSize": "20px"}),
#     #dcc.Dropdown(id='dropdown',options=[{'label': '', 'value': ''}], value='Search'),
#     dbc.Row([
#         dbc.Col(
#             [html.Label('Search by Customer Name:'),
#             dcc.Dropdown(id='customer-dropdown',
#             options=customer_options, placeholder='Customer Name'
#             )
#             ]),
#         dbc.Col(
#             [html.Label('Search by Country:'),
#             dcc.Dropdown(id='country-dropdown',
#             options=country_options, placeholder='Country'
#             )
#             ]),
#         # dbc.Col(
#         #     [html.Label('Search by Employee:'),
#         #     dcc.Dropdown(id='employee-dropdown',
#         #     options=employee_options, placeholder='Employee'
#         #     )
#         #     ])
#     ]),
#     dash_table.DataTable(id='customer-info',
#     columns=[{'name':col, 'id':col} for col in customer.columns])#,data=customer.to_dict('records'))
# ])

# @app.callback(
#     Output('customer-info', 'data'),
#     Input('customer-dropdown', 'value'),
#     Input('country-dropdown', 'value'),
#     #Input('employee-dropdown', 'value')
# )

# def update_table_by_customer_name(selected_customer, selected_country):
#     print(selected_customer, selected_country)
#     filtered_customer = customer[customer['Customer Name'] == selected_customer]
#     if (selected_country is None):# & (selected_employee is None):
#         filtered_customer = customer[customer['Customer Name'] == selected_customer]
#     elif (selected_customer is None): #& (selected_employee is None):
#         filtered_customer = customer[customer['Country Name'] == selected_country]
#     # elif (selected_customer is None) & (selected_country is None):
#     #     filtered_customer = customer[customer['Employee '] == selected_employee]
#     elif (not(selected_customer is None)) & (not(selected_country is None)):# & (selected_employee is None):
#         filtered_customer = customer[(customer['Customer Name'] == selected_customer) & (customer['Country Name'] == selected_country)]
#     # elif (not(selected_customer is None)) & (selected_country is None) & (not(selected_employee is None)):
#     #     #print((not(selected_customer is None)) & (selected_country is None) & (not(selected_employee is None)))
#     #     filtered_customer = customer[(customer['Customer Name'] == selected_customer) & (customer['Employee '] == selected_employee)]
#     # elif (selected_customer is None) & (not(selected_country is None)) & (not(selected_employee is None)):
#     #     filtered_customer = customer[(customer['Country Name'] == selected_country) & (customer['Employee '] == selected_employee)]
#     # elif (not(selected_country is None)) & (not(selected_employee is None)) & (not(selected_customer is None)):
#     #     filtered_customer = customer[(customer['Country Name'] == selected_country) & (customer['Employee '] == selected_employee) & (customer['Customer Name'] == selected_customer)] 

#     return filtered_customer.to_dict('records')
########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='flyingdog',
        figure=beer_fig
    ),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A('Data Source', href=sourceurl),
    ]
)

if __name__ == '__main__':
    app.run_server()
