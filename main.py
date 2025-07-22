import streamlit as st


# st.title("This is a title")

st.title("Student Application Form")

# st.subheader("This is a subheader")

# st.markdown("This is a markdown")

# st.code("""for i in range(1,5):
#                 print(i)""")


# dataset = ad.read_csv("knl")              # Here this line of code is not working

# st.dataframe(dataset)                     # Here this line of code is not working


name = st.text_input("Enter your name:")
fname = st.text_input("Enter your father name:")
mname = st.text_input("Enter your mother name:")
address = st.text_area("Enter your address:")
class_data = st.selectbox("Enter your class",("select",1,2,3,4,5,6,7,8,9,10,11,12))
button = st.button("submit")

if button :
    st.markdown(f"""
                name:{name}\n
                fname:{fname}\n
                mname:{mname}\n
                address:{address}\n
                class:{class_data}
                """)
