import streamlit as st
import emoji
from sympy import sympify, zoo

# Function to init display
def set_initial_display():
    box_style = """
        <div style='
            font-size: 30px; 
            color: #333; 
            border: 2px solid #ccc; 
            padding: 0px 10px 0px 10px; 
            border-radius: 5px; 
            background-color: #f9f9f9;
            text-align: left;
            margin-bottom: 20px;
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);'>
        0</div>
    """
    display.markdown(box_style, unsafe_allow_html=True)

# Function to update display
def update_display(value):
    st.session_state.input_value += value
    # CSS styling for the box
    box_style = """
        <div style='
            font-size: 30px; 
            color: #333; 
            border: 2px solid #ccc; 
            padding: 0px 10px 0px 10px; 
            border-radius: 5px; 
            background-color: #f9f9f9;
            text-align: left;
            margin-bottom: 20px;
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);'>
        {}</div>
    """.format(st.session_state.input_value)
    
    display.markdown(box_style, unsafe_allow_html=True)

def calculation(equation):
    expression = sympify(equation)
    result = expression.evalf()

    if result is zoo:
        return "INF"
    elif result/int(result) == float(1):
        return str(int(result))
    else:
        return f"{result:.2f}"

def calculate_result():
    equation = st.session_state.input_value
    st.session_state.input_value = calculation(equation)

    box_style = """
        <div style='
            font-size: 30px; 
            color: #333; 
            border: 2px solid #ccc; 
            padding: 0px 10px 0px 10px; 
            border-radius: 5px; 
            background-color: #f9f9f9;
            text-align: right;
            margin-bottom: 20px;
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);'>
        {}</div>
    """.format(st.session_state.input_value)
    display.markdown(box_style, unsafe_allow_html=True)
    if st.session_state.input_value == "INF":
        st.session_state.disabled = False
        # st.session_state.input_value = ""

    st.balloons()

# Function to clear input
def clear_input():
    st.session_state.input_value = ""
    box_style = """
        <div style='
            font-size: 30px; 
            color: #333; 
            border: 2px solid #ccc; 
            padding: 0px 10px 0px 10px; 
            border-radius: 5px; 
            background-color: #f9f9f9;
            text-align: left;
            margin-bottom: 20px;
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);'>
        0</div>
    """
    display.markdown(box_style, unsafe_allow_html=True)

def visualize_button(disabled):
    # Virtual keyboard layout
    col1, col2, col3, col4 = st.columns(4)
    button_style = """
        <style>
        .stButton>button {
            font-size: 30px;
            padding: 10px;
            width: 100%;
            background-color: #f0f0f0;
            border: 1px solid #ccc;
            color: #333;
        }
        .stButton>button:hover {
            background-color: #ddd;
            border: 1px solid #bbb;
        }
        </style>
    """
    st.markdown(button_style, unsafe_allow_html=True)

    with col1:
        if st.button("7", disabled = st.session_state.disabled):
            update_display("7")
        if st.button("4", disabled = st.session_state.disabled):
            update_display("4")
        if st.button("1", disabled = st.session_state.disabled):
            update_display("1")
        if st.button("0", disabled = st.session_state.disabled):
            update_display("0")

    with col2:
        if st.button("8", disabled = st.session_state.disabled):
            update_display("8")
        if st.button("5", disabled = st.session_state.disabled):
            update_display("5")
        if st.button("2", disabled = st.session_state.disabled):
            update_display("2")
        if st.button(".", disabled = st.session_state.disabled):
            update_display(".")

    with col3:
        if st.button("9", disabled = st.session_state.disabled):
            update_display("9")
        if st.button("6", disabled = st.session_state.disabled):
            update_display("6")
        if st.button("3", disabled = st.session_state.disabled):
            update_display("3")
        if st.button("=", disabled = st.session_state.disabled):
            calculate_result()
    with col4:
        # if st.button("AC"):
        #     clear_input() # check
        if st.button("/", disabled = st.session_state.disabled):
            update_display("/")
        if st.button("\*", disabled = st.session_state.disabled):
            update_display("*")
        if st.button("\-", disabled = st.session_state.disabled):
            update_display("-")
        if st.button("\+", disabled = st.session_state.disabled):
            update_display("+")

if __name__ == '__main__':
    # Title of the app
    st.title("Calculator")

    # Creating a container for inputs to be placed side by side
    display, AC_button = st.columns([3, 1])

    # Initialize state variables to hold the input and operation
    if "input_value" not in st.session_state:
        st.session_state.input_value = ""
        set_initial_display()
    if "operation" not in st.session_state:
        st.session_state.operation = None
    if "display_value" not in st.session_state:
        st.session_state.display_value = ""
    if 'disabled' not in st.session_state:
        st.session_state.disabled = False

    if AC_button.button("AC"):
        clear_input()

    visualize_button(st.session_state.disabled)