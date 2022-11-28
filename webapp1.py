# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 16:48:02 2021

@author: gauri
"""

import streamlit as st
add_selectbox = st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)
checkbox_val = st.checkbox("Form checkbox")
n = st.number_input('Number', step=1)
s = st.text_input('Type a name in the box below')
submit_button = st.button(label='Submit')

if submit_button:
    st.write(add_selectbox)
    st.write(checkbox_val)
    st.write(n)
    st.write(s)