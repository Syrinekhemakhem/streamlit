import streamlit as st
st.title("Hello Gomycode")
st.header("En-tete")   
st.subheader("Sous-Titre")
st.text("Ceci est un texte")
st.markdown("<h1>###ceci est un markdown</h1>",unsafe_allow_html=True)  #je peux mettre des lien shtml
st.success("Success")
st.info("information")
st.warning("Warning")
st.error("Error")
exp=ZeroDivisionError("Trying ti divide by Zero")
st.exception(exp)

status=st.radio("Select Gender:",('Male','Female'))
if(status=='Male'):
    st.success("Male")
else:
    st.success("Female")

hobby=st.selectbox("Hobbies:",
                   ['Dancing','Reading','Sports'])   #on choisit juste une seule des catégories 

hobbies=st.multiselect("Hobbies:",
                   ['Dancing','Reading','Sports']) 
st.write("You selected",len(hobbies),"Hobbies")   #je peux selectionner plusieurs hoobie et il me donne le nombre que j'ai selectionné
st.write("You selected",hobbies,"as Hobbies")
for i in hobbies: 
    st.write("You selected",i,"as Hobbies")  #si je veux la faire apparaitre plus joliment et non dans une liste 

level=st.slider("Select the level",1,5)
st.text('Selected:{}'.format(level)) #pour qu'elle me mette le level dans les {}

st.button("Click me for no reason")
if(st.button("About")):                              #si je veux qu'une fois que je clique sur mon bouton, un autre truc apparait 
    st.text('Welcome to Gomycode!!!')
''''''
#name=st.text_input("Enter Your name","Type Here...")    #input
#if(st.button('Submit')):
#    result=name.title()
#    st.success("You entered" + result)


#st.title("Greeting App1")

#Name1=st.text_input("Enter Your name",key='ex1)    #input  sans  le mot 'type here' c'est plus simple
#if(st.button('Greet Me')):
#    result=Name1.title()
#    st.success("Hello", + result, "Welcome to the streamlit world!")
#else:
#    st.warning("Please enter your name")

st.title("Greeting App2")

Name2=st.text_input("Enter Your name","Type Here...",key='ex2')    #input
if(st.button('Greet Me')):
    result=Name2.title()
    if Name2=="Type Here..." or len(Name2)==0:
        st.warning("Please enter your name")
    else:
        
        st.success(f"Helle {Name2} , welcome")

