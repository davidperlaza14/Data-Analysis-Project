import plotly.express as px

# Function to create a histogram of a column.
def plot_distribution(df, column):
    fig = px.histogram(df, x=column, title=f'Distribucion de {column}')
    fig.show()

# Function to create a scatter plot between two columns.
def plot_scatter(df, x_column, y_column):
    fig = px.scatter(df, x=x_column, y=y_column, title=f'{x_column} vs {y_column}')
    fig.show()