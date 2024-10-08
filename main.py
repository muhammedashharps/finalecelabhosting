import streamlit as st

st.set_page_config(
    page_title="Download ECE Lab Companion App",
    page_icon="📱",
    layout="wide"
)


page_bg_img = '''

<style> 
[data-testid="stHeader"] {
background-color: white;
}

</style

'''
st.markdown(page_bg_img,unsafe_allow_html =True)
# Set page config




# Custom CSS with improved color scheme
st.markdown("""
<style>
    body {
        color: #1E1E1E;
        background-color: #F5F5F5;
    }
    .main {
        padding: 2rem;
        border-radius: 10px;
        background-color: #FFFFFF;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 8px;
        border: none;
        transition-duration: 0.4s;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stDownloadButton>button {
        background-color: #007BFF;  /* Changed to blue color */
        color: white;                /* Set text color to white */
        font-weight: bold;           /* Make text bold */
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 20px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 10px;
        border: none;
        transition-duration: 0.4s;
    }
    .stDownloadButton>button:hover {
        background-color: #0056b3;  /* Darker blue on hover */
    }
    .feature-box {
        background-color: #F0F8FF;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    h1, h2, h3 {
        color: #2C3E50;
    }
    .footer-text {
        color: black;                 /* Set footer text color to black */
    }
    .warning-text {
        color: red;                  /* Change to the desired color for the warning */
        font-weight: bold;           /* Make warning text bold */
    }
    p {
        color: white;
    }
    .border {
        border-bottom: 2px solid #007BFF;  /* Add a blue bottom border */
        margin: 20px 0;                     /* Add margin for spacing */
    }
</style>
""", unsafe_allow_html=True)

# Header
st.title("📱 ECE Lab Companion App")
st.subheader("Your go-to app offering easy access to lab manuals, virtual labs, and skill-building resources.")

# App description

st.divider()

# Main content
col1, col2 = st.columns([2, 1])

with col1:
    st.header("🌟 Key Features")

    features = [
        ("📘 Lab Manuals", ""),
        ("🔬 Virtual Labs", ""),
        ("📝 Exam Preparation", ""),
        ("🛠️ Project Ideas", ""),
        ("📊 Practical Electronics Resources", "")
    ]

    st.markdown("<br>", unsafe_allow_html=True)

    for icon, feature in features:
        with st.container():
            st.markdown(f"""
            <div class="feature-box">
                <h3>{icon} {feature.split(':')[0]}</h3>
                <p>{feature}</p>
            </div>
            """, unsafe_allow_html=True)



with col2:
    # Placeholder for app screenshot
    st.image("appphoto.png", caption="ECE Lab Companion App",
             use_column_width=True)

st.download_button(label="Click Here To Download",
                       data=open("labcompanion.apk", "rb").read(),
                       # Change "labcompanion.apk" to the name of your APK file
                       file_name="labcompanion.apk",
                       mime="application/vnd.android.package-archive", )

# Additional information
st.divider()

# Add a border above the warning
st.markdown('<div class="border"></div>', unsafe_allow_html=True)

# Warning message
st.markdown('<div class="warning-text">If you encounter any errors while installing the app, please contact us at ecelabcompanion@gmail.com, muhammedashharps@gmail.com</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown('<p class="footer-text">© 2024 ECE Lab Companion. All rights reserved.</p>', unsafe_allow_html=True)
st.markdown('<p class="footer-text">2026 Batch, ECE Department, NSS College Of Engineering</p>', unsafe_allow_html=True)
