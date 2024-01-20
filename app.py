import streamlit as st

from PIL import Image

import datetime

st.title('Hello we are learning Streamlit!!!!')

st.header('This is a header')

st.subheader('this is a sub-header')

st.text('Hello GUYS!!!')

st.markdown("**Streamlit** is a widely used GUI for machine learning apps")
html_string = "<h3>this is an html string</h3>"

st.markdown("<h3><u>this is an html string</u></h3>", unsafe_allow_html=True)

st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

st.success("This is a success symbol")

st.info("general information")

st.warning('Try to Avoid')

st.error('CHORIE LAT!!!!')

exp=ZeroDivisionError("trying to divide by 0")
st.exception(exp)


st.write("I am texting")

st.write(range(10))

img=Image.open('simage.png')
st.image(img,width=200)

if st.checkbox("show/hide"):
    st.text('Showing the data')

status=st.radio("Select gender: ",('Female','Male'))

if status == 'Male':
    st.success('I am a MALE')
else:
     st.success('I am a FEMALE')


h=st.selectbox("Hobbies: ",['Movie','Football','travelling','songs'])

st.write('your hobbey is ',h)

h1=st.multiselect("Hobbies AGAIN: ",['Movie','Football','travelling','songs','teaching'])

st.write('your hobbeies are  ',len(h1),'MY HOBIES!!!!!')


st.button("CLICK me ")


if(st.button("againn click me")):
    st.text("BUTTON CLICKED!!!!!")

x=st.text_input('enter your name',"type here!!!!")

if st.button('submit'):
    r=x.title()
    st.success(r)

level=st.slider('select the level',1,10)

st.text('Selected {}'.format(level))

st.write("check out this [link](http://www.ibm.com)")

d=st.radio('whats your favourite lanhuage?',('C','C++','JAVA','PYTHON'))

if d=='C':
    st.write("You selected "+d)
elif d=='C++':
    st.write("You selected "+d)
elif d=='JAVA':
    st.write("You selected "+d)
else:
    st.write('You selected PYTHON')

age=st.slider("please enter your age",min_value=0,max_value=100,value=22)
st.write('your age is '+str(age))


dt=st.date_input('whats your birthday',datetime.date(2000,1,1),datetime.date(1980,1,1),datetime.datetime.now())

st.write('your bday is ',dt)

tm=st.time_input("kotai eli re",datetime.time(0,0))

st.write('ami elam at  ',tm)


