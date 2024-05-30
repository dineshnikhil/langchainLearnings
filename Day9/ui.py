import streamlit as st

# Set the page configuration
st.set_page_config(layout="centered", page_title="Streamlit UI")

# Title
st.title("Streamlit UI")

# Create the layout with columns
col1, col2, col3 = st.columns([4, 1, 4])

# Input field
with col1:
    input_text = st.text_area("Input Field", height=300)

# Button to perform action
with col2:
    if st.button("Go"):
        # Perform some action
        st.write("Button clicked!")

# Output field
with col3:
    output_text = st.text_area("Output Field", height=300)

# Chat Interface
st.write("### Chat Interface")
chat_input = st.text_input("Enter your message:")
if st.button("Send"):
    st.write(f"User: {chat_input}")
    # Here you can add the logic to generate and display the response
