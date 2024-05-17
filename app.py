import streamlit as st
import json
import requests

st.title('Predict medical insurance charges')


with open('input_options.json') as f:
    side_bar_options = json.load(f)
    options = {}
    for key, value in side_bar_options.items():
        if key in ['charges']:
            options[key] = st.sidebar.selectbox(key, value)
        else:
            min_val, max_val = value
            current_value = (min_val + max_val)/2
            options[key] = st.sidebar.slider(key, min_val, max_val, value=current_value)


st.write(options)

if st.button('Predict'): 
    print('IN button')

    payload = json.dumps({'inputs': options})
    response = requests.post(
        url=f"http://134.209.38.91/invocations",
        data=payload,
        headers={"Content-Type": "application/json"},
    )
    
    prediction = response.json().get('predictions')[0]
    st.write(f'The predicted median house value is: ${prediction:,}')
