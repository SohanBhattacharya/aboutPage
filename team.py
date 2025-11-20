import streamlit as st
import time
from PIL import Image, ImageDraw, ImageOps


st.set_page_config(page_title="WhiteDragon AI", layout="wide")



# Path to your downloaded image
image_path = "Dragon Image.png"
# Load the image
img = Image.open(image_path)
# Create two columns: one for the image, one for the text
col1, col2= st.columns([0.4, 5])

with col1:
    st.image(img, width=100, caption="", use_column_width=False)

with col2:
    st.markdown(
        "<h2 style='margin: 0; display: flex; align-items: center;'>WhiteDragon AI Teams</h2>",
        unsafe_allow_html=True,
    )


# CSS to make the image circular
st.markdown(
    """
    <style>
        img {
            border-radius: 10%;
        }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown("---")



# Typing animation
placeholder = st.empty()
text = "Welcome to Our Teams Section! Here are the list of members who were responsible for bringing this project to life."

for i in range(len(text) + 1):
    placeholder.markdown(
        f"<p style='font-size:20px; font-weight:300; font-family:Segoe UI, sans-serif;'>{text[:i]}</p>",
        unsafe_allow_html=True
    )
    time.sleep(0.05)

st.markdown("---")
# Function to round the corners of an image
def round_corners(img, radius=40):
    img = img.convert("RGBA")

    # Create rounded mask
    mask = Image.new("L", img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle(
        [(0, 0), img.size],
        radius=radius,
        fill=255
    )

    # Apply mask to image
    rounded_img = ImageOps.fit(img, img.size)
    rounded_img.putalpha(mask)
    return rounded_img
#-----------------------SOHAN BHATTACHARYA---------------------------------------------

img_path = r"C:\Users\sukan\Desktop\Deploy Chatbot\sohan.jpeg"

# Create 2 columns
col1, col2 = st.columns([1,3])

with col1:
    original_img = Image.open(img_path)

    # Apply rounded corners (modify radius as needed)
    rounded_img = round_corners(original_img, radius=1000)

    st.image(rounded_img, use_container_width=True)

with col2:
    st.title("Sohan Bhattacharya: [Team Lead]")
    st.markdown(
        "<h1 style='font-size:20px; font-style: italic'>Full Stack Web Developer, Machine Learning Engineer</h1>",
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <p style="font-family: Monaco, monospace; font-size:16px; line-height:1.6;">
        Through this project, I gained hands-on experience in managing a clean codebase, refactoring modules, and performing rigorous testing to ensure performance. One major challenge was selecting the right ML or DL algorithm, which I solved by analyzing the problem in depth and comparing real-world use cases. I also learned to maintain a scalable code structure and strengthened my leadership skills while coordinating tasks and guiding the team.</p>
        """,
        unsafe_allow_html=True
    )

#-----------------------------------------PRABHAT SHAW---------------------------------------------------
st.markdown("---")
img_path = r"C:\Users\sukan\Desktop\Deploy Chatbot\prabhat.jpeg"

# Create 2 columns
col1, col2 = st.columns([3,1])

with col1:
    st.title("Prabhat Shaw: ")
    st.markdown(
        "<h1 style='font-size:20px; font-style: italic'>UI & UX Designer - I</h1>",
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <p style="font-family: Monaco, monospace; font-size:16px; line-height:1.6;">
        While designing the UI/UX for the stock analysis and prediction model, we struggled to simplify complex financial data into a clean interface. Choosing clear chart visuals without overcrowding information was challenging. We also had difficulty making the design easy for non-technical users. Frequent model updates forced us to revise our layouts repeatedly. Coordination with the development team was initially tough. Through prototyping and constant communication, we overcame these issues and built a smooth, user-friendly design.
        </p>
        """,
        unsafe_allow_html=True
    )

with col2:
    original_img = Image.open(img_path)

    # Apply rounded corners (modify radius as needed)
    rounded_img = round_corners(original_img, radius=1000)

    st.image(rounded_img, use_container_width=True)


#----------------------ANTAR PAUL---------------------------------------------------
st.markdown("---")
img_path = r"C:\Users\sukan\Desktop\Deploy Chatbot\antar.jpeg"

# Create 2 columns
col1, col2 = st.columns([1,3])

with col1:
    original_img = Image.open(img_path)

    # Apply rounded corners (modify radius as needed)
    rounded_img = round_corners(original_img, radius=1000)

    st.image(rounded_img, use_container_width=True)

with col2:
    st.title("Antar Paul:")
    st.markdown(
        "<h1 style='font-size:20px; font-style: italic'>UI & UX Designer - II</h1>",
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <p style="font-family: Monaco, monospace; font-size:16px; line-height:1.6;">
        During the UI/UX development of the stock analysis platform,
         we encountered difficulties in translating dense financial 
         information into a clean and easy-to-understand interface. 
         Achieving a balance between informative charts and a minimal, 
         uncluttered layout proved challenging, especially while ensuring 
         the design remained intuitive for users without technical expertise. 
         Ongoing changes in the backend logic forced repeated adjustments to 
         our screens. Initial communication gaps also slowed down our workflow. 
         However, through continuous prototyping, user feedback, and strong team 
         coordination, we ultimately delivered a streamlined and highly accessible user experience.""",
        unsafe_allow_html=True
    )

st.markdown("---")
