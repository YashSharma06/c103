import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")
fig = px.scatter(df,x="Population", y = "InternetUsers", color="Country", size="Percentage", size_max=80)
fig.show()