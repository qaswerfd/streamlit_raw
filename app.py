import requests
import streamlit as st
#from streamlit_lottie import st_lottie
from PIL import Image

import sys
import os

# Path to the directory you want to add
#my_module_dir = r"C:\Users\Qaswe\Anaconda3\envs\streamlit_env\my_app\MYCV_APP\personal-cv-streamlit-template-main"

# Ensure the directory exists
#if os.path.isdir(my_module_dir):
#  sys.path.append(my_module_dir)
#else:
#  print(f"Directory '{my_module_dir}' does not exist.")

import streamlit as st


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Personal Webpage", page_icon=":tada:", layout="wide",initial_sidebar_state="collapsed")
st.sidebar.header("Main")
st.sidebar.success("Main page only for now")

#def load_lottieurl(url):
#    r = requests.get(url)
#    if r.status_code != 200:
#        return None
#    return r.json()


# Use local CSS
#def local_css(file_name):
#    with open(file_name) as f:
#        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


#local_css(r"C:\Users\Qaswe\Anaconda3\envs\streamlit_env\my_app\MYCV_APP\styles\style.css")

# ---- LOAD ASSETS ----
#lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_iv4dsx3q.json")
#img_contact_form = Image.open(r"C:\Users\Qaswe\Anaconda3\envs\streamlit_env\my_app\MYCV_APP\personal-cv-streamlit-template-main\images/yt_contact_form.png")
#img_lottie_animation = Image.open(r"C:\Users\Qaswe\Anaconda3\envs\streamlit_env\my_app\MYCV_APP\personal-cv-streamlit-template-main\images/yt_lottie_animation.png")

# ---- HEADER SECTION ----
with st.container():
    
    st.title("Hi, I am George :wave:")
    st.subheader("A technologist in the UK")
    st.write(
        "I am passionate about finding ways to use Python and BI tools to be more efficient and effective in business settings."
    )
    st.write("I have worked in many roles, across multiple businesses, across 2 continents and am keen to do more! I follow my nose :nose: and its taken me to some amazing places and allowed me to meet many people from different walks of life. Check out my LinkedIn (https://www.linkedin.com/in/george-karous-614778154/. This is a demo of the tech more than a finished CV so please refer to my LinkedIn over this in the first instance. :smile: ")



with st.container():
    st.subheader("My Timeline so far")
    
    from streamlit_timeline import st_timeline
    import datetime
    # Get today's date
    today = datetime.date.today()
    # Format the date as YYYY-MM-DD
    formatted_date = today.strftime("%Y-%m-%d")


    items = [
        {"id": 1, "content":"Born", "start": "1998-08-03", "Summary": "Born in Brighton, schooled at Deepdean, St Christopher's and Brighton College"},
        {"id": 2, "content": "Durham Uni", "start": "2016-09-06","Summary": "Went to Durham University to study B.Eng General Enigneering, then went on to complete a M.Sc in Advanced Mechanical Engineering"},
        {"id": 3, "content": "Flexio", "start": "2020-10-18", "Summary": "Joined Flexio after Uni"},
        {"id": 4, "content": "Siemens Healthineers", "start": "2021-02-01", "Summary": "Joined Siemens Healthineers"},
        {"id": 5, "content": "AstraZeneca", "start": "2021-09-06", "Summary": "Joined AstraZeneca on the Technology Leadership Graduate Scheme"},
        {"id": 6, "content": "AstraZeneca US", "start": "2023-04-01", "Summary": "Went to Maryland, USA with Astrazeneca"},
        {"id": 7, "content": "Now", "start": formatted_date, "Summary": "Working in the Digital, Strategy and Change team in Operations. Working on Zenon implementation, digitalisation and learning from my business colleagues"}
    ]

    timeline = st_timeline(items, groups=[], options={}, height="300px")
    st.subheader("Selected item")
    st.write(timeline)



    

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Education")
        #st.write("##")
        st.write(
            """
            I studied at Durham University, I completed a B.Eng in General engineering with a mechanical/ electrical specialisation. I then completed an M.Sc in Advanced Mechanical Engineering culminating in an individual final project where I created a method for segmenting CT scans and extracting brain aneurysm models. I simulated these using hyperelastic wall and shear thinnning viscosity models to achieve a realistic simulation. See the images:
            - Skills: CFD and CSD and Financial Simulation, Data, Autonomy, Research, Coding, BI, Automation, Report Writing and Benefits Analysis.
            - Softwares: Matlab, Ansys suite, Abaqus, Openfoam, Solidworks, OnShape, Paraview.
            - Accreditations recieved: General Engineering B.Eng: 2.1 classification, M.Sc Advanced Mechanical Engineering (with Aerodynamics) Distinction classification. 
            """
        )
        #st.write("[YouTube Channel >](https://youtube.com/c/CodingIsFun)")
    with right_column:
        #st_lottie(lottie_coding, height=300, key="coding")

        
        st.image(r'C:\Users\Qaswe\Anaconda3\envs\streamlit_env\my_app\MYCV_APP\personal-cv-streamlit-template-main\images\vortices.PNG', width = 250)
        st.image(r'C:\Users\Qaswe\Anaconda3\envs\streamlit_env\my_app\MYCV_APP\personal-cv-streamlit-template-main\images\ICA.PNG', width = 250)
        st.image(r'C:\Users\Qaswe\Anaconda3\envs\streamlit_env\my_app\MYCV_APP\personal-cv-streamlit-template-main\images\WSS.PNG', width = 250)
# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("Companies I have worked for:")
    #st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(r'C:\Users\Qaswe\Anaconda3\envs\streamlit_env\my_app\MYCV_APP\personal-cv-streamlit-template-main\images\AZ.png', width = 275)
    with text_column:
        st.subheader("AstraZeneca")
        st.write(
            """
            Joined the AstraZeneca Technology Leadership Graduate Scheme, I have worked sequentially through the value chain of the business, across 2 continents and in Business and IT roles.
            I started in R&D IT as a project manager, moved into PT&D Modelling & Simulations as an automation engineer / data scientist. Moved into a communications officer role in Enterprise data & AI, moved to the US to work in OPS IT Biologics as a Business Analyst. I returned to the UK to work in Commercial IT - Patient, then to OPS Digital, strategy & change as a hybrid data analyst / project manager.
            
            I have worked across numerous modalities, Oligonucleotides, Oral Solid Dosage, Biologics, Cell Therapy, Injectable solid dose. I have also worked across packing, 
            """
        )
   
        #st.markdown("[Watch Video...](https://youtu.be/TXSOitGoINE)")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(r'C:\Users\Qaswe\Anaconda3\envs\streamlit_env\my_app\MYCV_APP\personal-cv-streamlit-template-main\images\Siemenspng.png')
    with text_column:
        st.subheader("Siemens Healthineers")
        st.write(
            """
            Joined Siemens in the Finance department, with a focus on automation and simplification. I reported into the GB CFO, working on healcount reporting, digitalisation (vision, project capturing and triage)
            """
        )
        #st.markdown("[Watch Video...](https://youtu.be/FOULV9Xij_8)")



with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(r'C:\Users\Qaswe\Anaconda3\envs\streamlit_env\my_app\MYCV_APP\personal-cv-streamlit-template-main\images\flex.png')
    with text_column:
        st.subheader("Flexio")
        st.write(
            """
            Worked with a Telehealth Physiotherapy start up. Performed roles such as data scientist, also marketing and animation.
            """
        )
        #st.markdown("[Watch Video...](https://youtu.be/FOULV9Xij_8)")

#with st.container():
#    image_column, text_column = st.columns((1, 2))
#    with image_column:
#        st.image(r'C:\Users\Qaswe\Anaconda3\envs\streamlit_env\my_app\MYCV_APP\personal-cv-streamlit-template-main\images\Glencore_logo.svg.PNG')
#        
#    with text_column:
#        st.subheader("Glencore Nickel")
#        st.write(
#            """
#            I worked for the Nickel division in Glencore International AG, out in Switzerland, where I worked with refinery data and created an automation script to rank key recycled and bulk material contributors to refinery infeed.
#            """
#       )

with st.container():
    st.write("---")
    st.header("Some of my 3D printing and CAD projects")

    import streamlit as st
    import pyvista as pv
    from stpyvista import stpyvista

    # Colormap options
    cmap_options = [
        'flag', 'prism', 'ocean', 'gist_earth', 'terrain',
        'gist_stern', 'gnuplot', 'gnuplot2', 'CMRmap',
        'cubehelix', 'brg', 'gist_rainbow', 'rainbow', 'jet',
        'turbo', 'nipy_spectral', 'gist_ncar'
    ]

    #option = st.selectbox("Select an option", ["Topology optimisation","GRIP", "Aneurysm segmentation"], index=1)
    option = "Aneurysm segmentation"

    if option == "GRIP":
        # Code for GRIP option
        mesh = pv.read(r"C:\Users\Qaswe\Anaconda3\envs\streamlit_env\my_app\MYCV_APP\personal-cv-streamlit-template-main\images\GRIP_blend_organised_mesh_V2.2.stl")
        


    elif option == "Aneurysm segmentation":
        # Code for Aneurysm segmentation option
        mesh = pv.read(r"C:\Users\Qaswe\Anaconda3\envs\streamlit_env\my_app\MYCV_APP\personal-cv-streamlit-template-main\images\hole in bleb.stl")
    
    elif option == "Topology optimisation":
        mesh = pv.read(r"C:\Users\Qaswe\Anaconda3\envs\streamlit_env\my_app\MYCV_APP\personal-cv-streamlit-template-main\images\file.stl")

    # Read your STL file
    #mesh = pv.read(r"C:\Users\Qaswe\Downloads\GRIP_blend_organised_mesh_V2.2.stl")
    #mesh = pv.read(r"C:\Users\Qaswe\Anaconda3\envs\streamlit_env\my_app\MYCV_APP\personal-cv-streamlit-template-main\images\GRIP_blend_organised_mesh_V2.2.stl")
    #mesh = pv.read(r"C:\Users\Qaswe\Anaconda3\envs\streamlit_env\my_app\MYCV_APP\personal-cv-streamlit-template-main\images\hole in bleb.stl")
    
    
    # Description text
    st.write(
        """
        3D Print projects: 
        Brain aneurysm CT scan model. This aneurysm was extracted from a CT scan, and using segmentation methods, an anerurysm volume was generated. I used this and fed it into a fully coupled Fluid solid interaction simulation, to improve progonosis camapbilities of clinical physicians. 
        """
    )

    # Create a PyVista plotter
    plotter = pv.Plotter(window_size=[600, 600])

    # Add a scalar field (optional)
    mesh['My scalar'] = mesh.points[:, 2] * mesh.points[:, 0]

    # Default state for show_edges and colormap
    show_edges = False
    selected_cmap = "jet"

    # Checkbox for show_edges
    #show_edges = st.checkbox("Show Edges", value=show_edges)

    # Dropdown for colormap selection
    #selected_cmap = st.selectbox("Select Colormap", cmap_options, index=cmap_options.index("jet"))

    # Update mesh visualization based on user selections
    plotter.clear()  # Clear existing mesh
    plotter.add_mesh(
        mesh,
        scalars="My scalar",
        cmap=selected_cmap,
        show_edges=show_edges,
        edge_color="#001100",
        ambient=0.2
    )

    plotter.camera_position = 'iso'

    # Display the updated visualization
    stpyvista(plotter, key="Aneurysm")

    st.write("---")
    #st.header("What I like to get up to")

    import streamlit as st
    import pyvista as pv
    from stpyvista import stpyvista

    # Colormap options
    cmap_options = [
        'flag', 'prism', 'ocean', 'gist_earth', 'terrain',
        'gist_stern', 'gnuplot', 'gnuplot2', 'CMRmap',
        'cubehelix', 'brg', 'gist_rainbow', 'rainbow', 'jet',
        'turbo', 'nipy_spectral', 'gist_ncar'
    ]

    #option = st.selectbox("Select an option", ["Topology optimisation","GRIP", "Aneurysm segmentation"], index=1)

    option = "Topology optimisation"

    if option == "GRIP":
        # Code for GRIP option
        mesh = pv.read(r"C:\Users\Qaswe\Anaconda3\envs\streamlit_env\my_app\MYCV_APP\personal-cv-streamlit-template-main\images\GRIP_blend_organised_mesh_V2.2.stl")
        


    elif option == "Aneurysm segmentation":
        # Code for Aneurysm segmentation option
        mesh = pv.read(r"C:\Users\Qaswe\Anaconda3\envs\streamlit_env\my_app\MYCV_APP\personal-cv-streamlit-template-main\images\hole in bleb.stl")
    
    elif option == "Topology optimisation":
        mesh = pv.read(r"C:\Users\Qaswe\Anaconda3\envs\streamlit_env\my_app\MYCV_APP\personal-cv-streamlit-template-main\images\file.stl")

    # Read your STL file
    #mesh = pv.read(r"C:\Users\Qaswe\Downloads\GRIP_blend_organised_mesh_V2.2.stl")
    #mesh = pv.read(r"C:\Users\Qaswe\Anaconda3\envs\streamlit_env\my_app\MYCV_APP\personal-cv-streamlit-template-main\images\GRIP_blend_organised_mesh_V2.2.stl")
    #mesh = pv.read(r"C:\Users\Qaswe\Anaconda3\envs\streamlit_env\my_app\MYCV_APP\personal-cv-streamlit-template-main\images\hole in bleb.stl")
    
    
    # Description text
    st.write(
        """
        3D Print projects: 
        Topology optimisation. I have experiemented with personal projects and have used topology optimisation studies to maximise structural integrity and minimise material usage for brackets, shelves and propellor blades.
        """
    )

    # Create a PyVista plotter
    plotter = pv.Plotter(window_size=[600, 600])

    # Add a scalar field (optional)
    mesh['My scalar'] = mesh.points[:, 2] * mesh.points[:, 0]

    # Default state for show_edges and colormap
    show_edges = False
    selected_cmap = "jet"

    # Checkbox for show_edges
    #show_edges = st.checkbox("Show Edges", value=show_edges)

    # Dropdown for colormap selection
    #selected_cmap = st.selectbox("Select Colormap", cmap_options, index=cmap_options.index("jet"))

    # Update mesh visualization based on user selections
    plotter.clear()  # Clear existing mesh
    plotter.add_mesh(
        mesh,
        scalars="My scalar",
        cmap=selected_cmap,
        show_edges=show_edges,
        edge_color="#001100",
        ambient=0.2
    )

    plotter.camera_position = 'xy'

    # Display the updated visualization
    stpyvista(plotter, key="TOP")

    st.write("---")
    #st.header("What I like to get up to")

    import streamlit as st
    import pyvista as pv
    from stpyvista import stpyvista

    # Colormap options
    cmap_options = [
        'flag', 'prism', 'ocean', 'gist_earth', 'terrain',
        'gist_stern', 'gnuplot', 'gnuplot2', 'CMRmap',
        'cubehelix', 'brg', 'gist_rainbow', 'rainbow', 'jet',
        'turbo', 'nipy_spectral', 'gist_ncar'
    ]

    #option = st.selectbox("Select an option", ["Topology optimisation","GRIP", "Aneurysm segmentation"], index=1)
    option = "GRIP"

    if option == "GRIP":
        # Code for GRIP option
        mesh = pv.read(r"C:\Users\Qaswe\Anaconda3\envs\streamlit_env\my_app\MYCV_APP\personal-cv-streamlit-template-main\images\GRIP_blend_organised_mesh_V2.2.stl")
        


    elif option == "Aneurysm segmentation":
        # Code for Aneurysm segmentation option
        mesh = pv.read(r"C:\Users\Qaswe\Anaconda3\envs\streamlit_env\my_app\MYCV_APP\personal-cv-streamlit-template-main\images\hole in bleb.stl")
    
    elif option == "Topology optimisation":
        mesh = pv.read(r"C:\Users\Qaswe\Anaconda3\envs\streamlit_env\my_app\MYCV_APP\personal-cv-streamlit-template-main\images\file.stl")

    # Read your STL file
    #mesh = pv.read(r"C:\Users\Qaswe\Downloads\GRIP_blend_organised_mesh_V2.2.stl")
    #mesh = pv.read(r"C:\Users\Qaswe\Anaconda3\envs\streamlit_env\my_app\MYCV_APP\personal-cv-streamlit-template-main\images\GRIP_blend_organised_mesh_V2.2.stl")
    #mesh = pv.read(r"C:\Users\Qaswe\Anaconda3\envs\streamlit_env\my_app\MYCV_APP\personal-cv-streamlit-template-main\images\hole in bleb.stl")
    
    
    # Description text
    st.write(
        """
        3D Print projects: 
        Webley AirPistol Grips, due to limited availability of bakolite grips, I have undertaken re-engineering projects, to replicate and improve on existing design. For this project re-engineering was the most feasible due to lack of equiptment and high fidellity models were difficult to produce.
        """
    )

    # Create a PyVista plotter
    plotter = pv.Plotter(window_size=[600, 600])

    # Add a scalar field (optional)
    mesh['My scalar'] = mesh.points[:, 2] * mesh.points[:, 0]

    # Default state for show_edges and colormap
    show_edges = False
    selected_cmap = "jet"

    # Checkbox for show_edges
    #show_edges = st.checkbox("Show Edges", value=show_edges)

    # Dropdown for colormap selection
    #selected_cmap = st.selectbox("Select Colormap", cmap_options, index=cmap_options.index("jet"))

    # Update mesh visualization based on user selections
    plotter.clear()  # Clear existing mesh
    plotter.add_mesh(
        mesh,
        scalars="My scalar",
        cmap=selected_cmap,
        show_edges=show_edges,
        edge_color="#001100",
        ambient=0.2
    )

    plotter.camera_position = 'xz'

    # Display the updated visualization
    stpyvista(plotter, key="GRIP")


def from_data_file(filename):
    import pandas as pd
    url = (
        "http://raw.githubusercontent.com/streamlit/"
        "example-data/master/hello/v1/%s" % filename
    )
    return pd.read_json(url)


with st.container():
    import streamlit as st
    import pandas as pd
    import numpy as np
    import pydeck as pdk

    st.write("---")
    st.header("My Professional Journey")
    # Description text
    st.write(
        """
        I have moved around the UK many times, across countrys and across continents and each experience has added real value and learnings. 
        """
    )

    #chart_data = pd.DataFrame(
    #    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    #    columns=["lat", "lon"],
    #)
    #print(chart_data)

    data = {
    "lat": [50.827778, 54.776100,46.9480, 54.776100,50.827778, 52.205276, 53.2602, 39.135479,53.2602],
    "lon": [-0.152778, -1.573300, 7.4474,-1.573300,-0.152778, 0.119167, -2.1256, -77.194695,-2.1256],
    "lat2": [ 54.776100, 46.9480,54.776100,50.827778, 52.205276, 53.2602, 39.135479,53.2602,52.489471,],
    "lon2": [ -1.573300, 7.4474, -1.573300, -0.152778, 0.119167, -2.1256, -77.194695,-2.1256,-1.898575,]
        }

    # Create a Pandas DataFrame from the dictionary
    chart_data = pd.DataFrame(data)

    st.pydeck_chart(
        pdk.Deck(
            map_style=None,
            initial_view_state=pdk.ViewState(
                latitude=50.827778, 
                longitude=-0.152778,
                zoom=5,
                pitch=50,
            ),
            layers=[
                pdk.Layer(
                    "HexagonLayer",
                    data=chart_data,
                    get_position="[lon, lat]",
                    radius=5000,
                    auto_highlight=True,
                    elevation_scale=20,
                    pickable=True,
                    elevation_range=[0, 3000],
                    extruded=True,
                    coverage=1,
                ),
                pdk.Layer(
                    "ArcLayer",
                    data= chart_data, #from_data_file("bart_path_stats.json"),
                    get_source_position=["lon", "lat"],
                    get_target_position=["lon2", "lat2"],
                    get_source_color=[200, 30, 0, 160],
                    get_target_color=[0, 200, 200, 300],
                    auto_highlight=True,
                    width_scale=0.001,
                    get_width="outbound",
                    width_min_pixels=3,
                    width_max_pixels=30,
                ),
                pdk.Layer(
                    "ScatterplotLayer",
                    data=chart_data,
                    get_position="[lon, lat]",
                    get_color="[200, 30, 0, 160]",
                    get_radius=2000,
                ),
            ],
        )
    )

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/Qaswerfd@icloud.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

with st.container():


    st.write("---")
    st.header("My interests")
    # Description text
    st.write(
        """
        I am fascinated by technology as a whole, I enjoy researching, playing and demonstrating technology in all its applications. 

        I have a real belief in lifelong learning and believe that with enough time and interest anything can be learned and value derived from it.

        Interested in entrepaneurship and making things.

        I am a keen technical writer and have had a chapter published in a medical textbook: (textbook: https://doi.org/10.1201/9781003164609, chapter: https://www.taylorfrancis.com/chapters/edit/10.1201/9781003164609-15/digital-health-aditya-desai-george-karous?context=ubx&refId=2dcef00c-fd7c-4e99-998b-298f5c692f46) 
        
        I am interested in sport, nutrition, investing (having made trading bots and a having a diversified portfolio), sustainability and environment, engineering, technology, Medicine, Medical technology, Computer Science, aviation, all terrestrial transportation, science, philosophy, reading and much more.
        """
    )

with st.container():

    st.write("---")
    st.header("Submit Feedback")
    st.write("##")

    #sentiment_mapping = ["one", "two", "three", "four", "five"]
    #selected = st.feedback("stars")
    #if selected is not None:
    #    st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")
    from IPython.display import HTML

    sentiment_mapping = ["one", "two", "three", "four", "five"]

    selected = st.feedback("stars")

    if selected is not None:
        st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")

    # Custom CSS to increase the size of the feedback widget
    st.markdown("""
    <style>
    .stFeedback {
        font-size: 200%;
    }
    </style>
    """, unsafe_allow_html=True)

js = """
        <script>
            function scrollToTop() {
                window.scrollTo({
                    top: 0,
                    behavior: 'smooth'
                });
            }
        </script>
    """
#st.markdown(js, unsafe_allow_html=True)

#st.components.v1.html(js)

#st.markdown('<a href="#" onclick="scrollToTop()">Back to Top</a><script>window.scrollTo(0, 0);</script>', unsafe_allow_html=True)
#st.markdown("<script>window.scrollTo(0, 0);</script>", unsafe_allow_html=True)


