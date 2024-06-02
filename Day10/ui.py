import streamlit as st
from llm import get_bllt_pnts_frm_desc

# Set the page configuration
st.set_page_config(layout="wide", page_title="Streamlit UI")

# Title
st.title("Streamlit UI")

# Apply CSS to increase the width of the input and output text areas
st.markdown(
    """
    <style>
    .input-text-area .stTextArea textarea {
        width: 100% !important;
    }
    .output-text-area .stTextArea textarea {
        width: 100% !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize session state
if 'output_text' not in st.session_state:
    st.session_state.output_text = ''

# Create the layout with columns
col1, col2, col3 = st.columns([2, 1, 2])

# Input field
with col1:
    st.markdown('<div class="input-text-area">', unsafe_allow_html=True)
    input_text = st.text_area("Input Field", height=300)
    st.markdown('</div>', unsafe_allow_html=True)

# Button to perform action
with col2:
    if st.button("Translate now"):
        with st.spinner("Translating..."):
            # Perform some action
            response = get_bllt_pnts_frm_desc(str(input_text))
            st.session_state.output_text = str(response)

# Output field
with col3:
    st.markdown('<div class="output-text-area">', unsafe_allow_html=True)
    output_text = st.text_area("Output Field", height=300, value=st.session_state.output_text, key="output_field")
    st.markdown('</div>', unsafe_allow_html=True)
