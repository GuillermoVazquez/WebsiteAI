import os
OPENAI_API_KEY = "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"  # platform.openai.com
os.environ['OPENAI_API_KEY']= OPENAI_API_KEY

import pandas as pd
from langchain.chat_models import ChatOpenAI
from langchain.agents import create_pandas_dataframe_agent

SHEET_ID = '1fI_qEk2Bu0fR79NZvFjmEOUf1BfPSACcLwpZslz6fHU'
SHEET_NAME = 'SampleData'

url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'
df = pd.read_csv(url)

chat  = ChatOpenAI(model_name="gpt-3.5-turbo",temperature = 0.0)
agent = create_pandas_dataframe_agent(chat, df, verbose=True)