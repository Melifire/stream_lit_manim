import streamlit as st
import pandas as pd
import numpy as np
from manim import *

start_shape = Square()
end_shape = Square()
start_color = '#00f900'
end_color = '#00f900'

class GenScene(Scene):
    def construct(self):
        background = Rectangle(
            width=1920,
            height=1080,
            stroke_width=0,
            fill_color="#111111",
            fill_opacity=1
        )
        self.add(background)

        start_shape.set_fill(start_color, opacity=0.5)
        start_shape.set_stroke(start_color, width=4)
        end_shape.set_fill(end_color, opacity=0.5)
        end_shape.set_stroke(end_color, width=4)

        self.wait()
        self.play(ReplacementTransform(start_shape, end_shape))
        self.wait()



def main():
    global start_shape, end_shape, start_color, end_color

    st.title('Custom Manim in Streamlit')
    status = st.status("Rendering...")

    col1, col2 = st.columns(2)

    with col1:
        col1.header('Start')
        start_shape_in = st.selectbox('Select starting shape', ['Square', 'Circle'])
        if start_shape_in == 'Square':
            start_shape = Square()
        else:
            start_shape = Circle()

        start_color = st.color_picker('Starting Color', '#00f900')

    with col2:
        col2.header('End')
        shape_select = st.selectbox('Select a shape', ['Square', 'Circle'])
        if shape_select == 'Square':
            end_shape = Square()
        else:
            end_shape = Circle()
    
        end_color = st.color_picker('Ending Color', '#00f900')


    scene = GenScene()
    scene.render()
    st.video("media/videos/1080p60/GenScene.mp4", start_time=1)
    status.update(label="Done!", state="complete", expanded=False)

if __name__=="__main__":
    main()