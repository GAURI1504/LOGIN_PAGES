# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 16:58:19 2021

@author: gauri
"""

import streamlit as st

st.title('QR INSTRUCTOR APP')
menu = ["user","client","admin"]
choice = st.selectbox("Menu",menu)
username = st.text_input("User Name")
s = st.text_input('password',type="password")
submit_button = st.button(label='login')
if submit_button:
    st.write('login successfull')