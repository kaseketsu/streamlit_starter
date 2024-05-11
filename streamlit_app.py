import openai
import streamlit as st
import pandas as pd
import openai as op
openai_api_key = st.sidebar.text_input('请输入你的openai_api_key',key = 'chatbot_api_key',type = 'password')
st.title('💬Chatbot')
if 'messages' not in st.session_state:
    st.session_state['messages'] = [{'role':'assistant','content':'How are you today'}]
for msg in st.session_state['messages']:
    st.chat_message(msg['role']).write(msg['content'])
prompt = st.chat_input()
if prompt is not None:
    if not openai_api_key:
        st.info("error:请输入open_ai_api_key")
        st.stop()
    openai.api_key = openai_api_key
    st.session_state['messages'].append({'role':'user','content':prompt})
    st.chat_message('user').write(prompt)
    response = openai.ChatCompletion.create(model = 'gpt-3.5-turbo',messages = st.session_state['messages'],
                                        tmperature = 0.7,max_tokens = 1000)
    answer = response['choices'][0].message.content
    st.session_state['messages'].append({'role':'assistant','content':answer})
    st.chat_message('assistant').write(answer)
