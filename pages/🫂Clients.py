import streamlit as st
import pandas as pd
st.markdown("# Clients")


st.write("""Here you may find information about our clients!
""")

df = pd.read_csv("Customers.csv") 

df.fillna({'Name': 'Unknown', 'Category': 'Unknown', 'Age': 0 , 'Satisfaction': 0}, inplace=True)

client = st.text_input('Client Name:', "Enter a client's name!")
if client != "Enter a client's name!":
    st.write('Showing ', client)
if client:
    df = df[df["Name"].str.contains(client, case=False)]

# Show results
if not df.empty:
    st.write(df[["Category", "Age", "Satisfaction"]])
else:
    st.write("No results found.")