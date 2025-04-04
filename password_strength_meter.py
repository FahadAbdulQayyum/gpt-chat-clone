import streamlit as st

def analyze_password(password):
    good_to_include = ['@', '!', '%', '$', '#', '^', '&', '*', '(', ')', '-', '+', '=', '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/', '~', '`']
    
    # Count how many special characters are in the password
    special_count = sum(1 for char in password if char in good_to_include)
    
    # Calculate the meter: each special character adds 10% (capped at 100%)
    meter = min(special_count * 10, 100)
    
    password_length = len(password)
    
    return [meter, password_length]

# Function to create a custom progress bar with color
def colored_progress_bar(percentage, color="green"):
    # Ensure percentage is within [0, 100]
    percentage = max(0, min(100, percentage))
    
    # Define the HTML/CSS for the progress bar
    html_code = f"""
    <div style="background-color: #e0e0e0; width: 100%; height: 25px; border-radius: 5px;">
        <div style="background-color: {color}; width: {percentage}%; height: 100%; border-radius: 5px; text-align: center; line-height: 25px; color: white; font-weight: bold;">
            {percentage:.0f}%
        </div>
    </div>
    """
    # Render the HTML using Streamlit's markdown
    st.markdown(html_code, unsafe_allow_html=True)

# Streamlit UI
st.title("Password Strength Meter")

# Input field for the password
password = st.text_input("Enter your password:", type="password")

if password:
    # Analyze the password and get the meter value
    [meter, password_length] = analyze_password(password)
    
    # Determine the color based on the strength
    if meter < 30:
        color = "red"
    elif 30 <= meter < 70:
        color = "orange"
    else:
        color = "green"
    
    # Display the colored progress bar
    st.subheader("Password Strength:")
    colored_progress_bar(meter, color)
    
    # Provide feedback based on the strength
    if password_length < 8:
        st.warning("❌ Password should be at least 8 characters long.")
    elif password_length > 8 and meter < 30:
        st.warning("Weak Password! Consider adding more special characters.")
    elif password_length > 8 and 30 <= meter < 70:
        st.info("Moderate Password. It's okay, but could be stronger.")
    elif password_length > 8 and 70 <= meter < 100:
        st.success("Strong Password! Good job!")