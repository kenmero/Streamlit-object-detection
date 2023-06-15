import json
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
import streamlit as st

# with open('./config/secret.json') as f:
#     secret = json.load(f)
    
# KEY = secret['KEY']
# ENDPOINT = secret['ENDPOINT']

# computervision_client = ComputerVisionClient(ENDPOINT, CognitiveServicesCredentials(KEY))
computervision_client = ComputerVisionClient(
    st.secrets['ENDPOINT'], CognitiveServicesCredentials(st.secrets['KEY']))
