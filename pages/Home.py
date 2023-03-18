# Troubleshooting Streamlit
# pip install --upgrade streamlit
# pip install --upgrade streamlit==1.11.1
# pip install pydeck==0.7.1
# pip install pipreqs 


import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import time
from datetime import datetime
from io import StringIO
import pickle

st.markdown("""# Home Page.""")

# st.markdown("# Text Elements")
# st.title("Title")
# st.header("Header")
# st.subheader("Subheader")
# st.write("Standard text")

# Markdown Equivalent
# st.markdown("""# Title
# ## Header
# ### Subheader
# Standard text""")

# st.caption("Caption")
# st.code("""Sample Code
# print('Hello World')
# a = 1234""")
# st.latex(r'''
#     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
#     \sum_{k=0}^{n-1} ar^k =
#     a \left(\frac{1-r^{n}}{1-r}\right)
#     ''')

st.markdown("## Text Input")
search = st.text_input('Search a client!')
st.write('Showing search results for:', client)

# st.markdown("## Text Area")
# txt = st.text_area('Text to analyze', '''
#     It was the best of times, it was the worst of times, it was
#     the age of wisdom, it was the age of foolishness, it was
#     the epoch of belief, it was the epoch of incredulity, it
#     was the season of Light, it was the season of Darkness, it
#     was the spring of hope, it was the winter of despair, (...)
# ''')


st.markdown("# Message Boxes")
st.info("This is a purely informational message")
st.success("This is a success message!")
st.exception("NameError('Error name is not defined')")
st.warning("This is a warning message")
st.error("This is an error message")

# st.markdown("# ALL DONE")
# if st.button('Done'):
#     st.balloons()
#     st.snow()