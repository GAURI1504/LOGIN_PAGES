# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 19:14:38 2021

@author: gauri
"""

import cv
import streamlit as st 
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
st.title("live")
run = st.checkbox('run camera')
frame_window = st.image([])
camera = cv2.VideoCapture(0)
while run:
    _, frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        minNeighbors=5,
        minSize=(30,30)
    )
    for(x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 2)
        
    frame_window.image(frame)
else:
    st.write('live ended')