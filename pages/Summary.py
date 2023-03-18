import streamlit as st
import pickle
import pandas as pd
import time

"""# Prediction """

@st.cache

def load_model():
    with open("deploymentWorkshopModel.pkl","rb") as model:
        model = pickle.load(model)
    return model

def predict(features):
    with prediction_placeholder:
        with st.spinner("Please wait while our model is predicting..."):
            prediction = model.predict(features)
            time.sleep(3)
            flower = flowers[prediction[0]]
        st.session_state.prediction = f"Your flower is most likely a **{flower}**"

sepal_length = st.sidebar.slider("Sepal Length",min_value=4.3,max_value=7.9,value=5.8,step=0.1)
sepal_width = st.sidebar.slider("Sepal Width",min_value=4.3,max_value=7.9,value=5.8,step=0.1)
petal_length = st.sidebar.slider("Petal Length",min_value=4.3,max_value=7.9,value=5.8,step=0.1)
petal_width = st.sidebar.slider("Petal Width",min_value=4.3,max_value=7.9,value=5.8,step=0.1)

flowers = ["Setosa", "Veriscolor", "Virginica"]
features = pd.DataFrame({
    "sepal_length": [sepal_length],
    "sepal_width": [sepal_width],
    "petal_length": [petal_length],
    "petal_width": [petal_width]
})

st.write("User Input")
st.write(features)

model = load_model()

prediction = st.button("Predict", on_click=predict, args=(features,))
prediction_placeholder = st.empty()

if prediction: 
    st.write(st.session_state.prediction)
# if st.checkbox("Prediction"):
#     st.balloons()
#     st.write(f"Your flower is most likely a {flowers[model.predict(features)[0]]}")