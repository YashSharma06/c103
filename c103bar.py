import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")
fig = px.bar(df,x="Population", y = "Country")
fig.show()