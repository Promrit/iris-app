import pickle
import streamlit as st 

# load the model from disk
loaded_model = pickle.load(open("per_model-xxx.sav", 'rb'))

# header
st.header("ass3-app :sunglasses:")
st.write("Classification of Iris dataset using :blue[Perceptron] model :pencil:")

sepal_length = st.slider('sepal length in cm:', min_value=0.1, max_value=10.0, value=1.0)
sepal_width = st.slider('sepal width in cm:', min_value=0.1, max_value=10.0, value=1.0)
petal_length = st.slider('petal length in cm', min_value=0.1, max_value=10.0, value=1.0)
petal_width = st.slider('petal width in cm', min_value=0.1, max_value=10.0, value=1.0)

if st.button('Predict Class'):
    data = [[sepal_length, sepal_width, petal_length, petal_width]]
    pred = loaded_model.predict(data)
    st.success(f'The predicted class of the iris is {pred[0]}')