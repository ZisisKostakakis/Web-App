from pathlib import Path
from platform import platform

import streamlit as st
from PIL import Image

# --- Path Settings
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "cv.pdf"
icon_pic = current_dir / "assets" / "icon.png"

# --- General Settings
PAGE_TITLE = "Digital Resume | Zisis Kostakakis"
PAGE_ICON = ":wave:"
NAME = "Zisis Kostakakis"
DESCRIPTION = '''Junior Software Engineer, working on development of python machine learning code'''
EMAIl = "Kostakakiszisis@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn":  "https://www.linkedin.com/in/zisis-kostakakis-5b85961b7/",
    "GitHub": "https://github.com/ZisisKostakakis?tab=repositories",
}
PROJECTS = {
    "CameraOCR - IOS App - Optical Character Recognition (Apple Vision, Swift), Machine Learning (Python), Server/API (Python)",
    "Connect-5-game - Java App - Game that makes use of GUI and AI (Minimax Algorithm)"
}

st.set_page_config(page_title = PAGE_TITLE, page_icon = PAGE_ICON)

# --- Load CSS, PDF
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
icon_pic = Image.open(icon_pic).rotate(180)

    


# --- Hero Section
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(icon_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(label = "Download CV",
                       data = PDFbyte,
                       file_name = resume_file.name,
                       mime = "application/octet-stream")
    st.write("Email: ", EMAIl)
    
# --- Soccial Media Section
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA)*3, gap ="small")
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})\n")
    
# --- Experience Section
st.write("#")
st.subheader("Experience & Qualifications")
st.write("✅", "6 Years of experience in the field of IT")
st.write("✅", "Experience in multiple technologies (Python, Java, Swift, AWS, C++)")    
st.write("✅", "Experience in multiple fields (Machine Learning, Web Development, Mobile Development)")
st.write("---")

# --- Skills Section
st.write("#")
st.subheader("Skills")
st.write("💻", "Programming: Python, Java, Swift, C++")
st.write("🖥", "Web Development: Flask, React")    
st.write("📱", "Mobile Development: IOS")
st.write("🤖", "Machine Learning: Scikit-learn, Pandas, Numpy")
st.write("🔐", "Cloud: AWS")
st.write("📈","Git", "Github", "Jira", "Agile", "Scrum","Bitbucket")

st.write("---")

# --- Work Section
st.write("#")
st.subheader("Work History")

# --- Job 1
st.write("🚧","**Junior Software Engineer | Storm Harvester**")
st.write("▶️", "August 2022 - Present")
st.write('''Working on development of python machine learning code by predicting the weather conditions''')
st.write("---")

#Accomplishments
st.write("#")
st.write("## Accomplishments")
st.write("🏆","**Bachelor's Degree with First Class Honours in Computer Science | Brunel University London**")
