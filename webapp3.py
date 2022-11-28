# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 16:55:15 2021

@author: gauri
"""

import streamlit as st
menu = ["Home","Login","SignUp"]
choice = st.sidebar.selectbox("Menu",menu)
username = st.sidebar.text_input("User Name")
b=st.sidebar.checkbox("Login")