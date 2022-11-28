# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 16:26:27 2021

@author: gauri
"""

import streamlit as st

st.title('Simple Streamlit App')
st.text('Type a number in the box below')
n = st.number_input('Number', step=1)
st.write(f'{n} + 1 = {n+1}')
s = st.text_input('Type a name in the box below')
st.write(f'Hello {s}')