import streamlit as st
import cohere
import os
from dotenv import load_dotenv
load_dotenv()

COHERE_KEY=os.getenv("COHERE_KEY")

# Set up Cohere client
co = cohere.Client(COHERE_KEY)

base_prompt_topic= 'Given a department and a list of favorite courses in engineering , this program will generate project topic ideas.\n\nDepartment: Mechanical Engineering\nFavorite Courses: Thermodynamics, Heat and mass transfer\nProject Topic: Refrigeration Using waste heat in cars.\n\n--SEPARATOR--\n\nDepartment: Mechanical Engineering\nFavorite Courses: Heat and mass transfer, Engineering drawing\nProject Topic: Analysis on effectiveness of a double heat exchanger with fin.\n\n--SEPARATOR--\n\nDepartment: Mechanical Engineering\nFavorite Courses: Metallurgy, Mechanics of fluid\nProject Topic: Aerodynamic modelling of wind Turbine Blades\n\n--SEPARATOR--\n\nDepartment: Civil Engineering\nFavorite Courses: Strength of Materials, Civil Engineering Materials\nProject Topic: The effect of untreated sugarcane ash on the setting time and compressive strength of concrete mix\n\n--SEPARATOR--\n\nDepartment: Civil Engineering\nFavorite Courses: Concrete technology, Theory of structures\nProject Topic: Geometric Design of Highway\n\n--SEPARATOR--\n\nDepartment: Civil Engineering\nFavorite Courses: Soil mechanics, Environmental engineering\nProject Topic: The effect of Environment on bond resistance between concrete and steel reinforcement\n\n--SEPARATOR--\n\nDepartment: Electronics Engineering\nFavorite Courses: Circuit and systems, Physical and applied electronics\nProject Topic: UltraSonic Radar Project\n\n--SEPARATOR--\n\nDepartment: Electronics Engineering\nFavorite Courses: Electromagnetism\nProject Topic: Antenna Design\n\n--SEPARATOR--\n\nDepartment: Electrical Engineering\nFavorite Courses: Power Systems, Electrical Machines\nProject Topic: Solar wireless Electric Vehicle charging system\n\n--SEPARATOR--\n\nDepartment: Electrical Engineering\nFavorite Courses: Measurement and instrumentation\nProject Topic: E-bike speed controller systems\n\n--SEPARATOR--\n\nDepartment: Materials Engineering\nFavorite Courses: Engineering composites, Industrial metallurgy\nProject Topic: Glass Hybrid Fibres Epoxy Composite Material\n\n--SEPARATOR--\n\nDepartment: Materials Engineering\nFavorite Courses: Degradation of Metals and alloy, Advanced materials processing\nProject Topic: Investigating the degradation of Epoxy Resin Nanocomposite Exposed to different environment\n\n--SEPARATOR--\n\nDepartment: Agricultural and Bio-Resource Engineering\nFavorite Courses: Machinery and Food engineering\nProject Topic: Performance Evaluation of a solar powered poultry egg incubator\n\n--SEPARATOR--\n\nDepartment: Chemical Engineering\nFavorite Courses: Industry Chemistry\nProject Topic: Comparative study of Physicochemical analysis of borehole water in a municipal\n\n--SEPARATOR--\n\nDepartment: Chemical Engineering\nFavorite Courses: Petroleum Engineering\nProject Topic: Identification of well problems using well testing\n\n--SEPARATOR--\n\nDepartment: Computer Engineering\nFavorite Courses: Embedded systems, Circuit Analysis\nProject Topic: Water level controller using a microcontroller\n\n--SEPARATOR--\n\nDepartment: Mechanical Engineering\nFavorite Topics: Computer Aided Design(CAD), Control Systems, Automation\nProject Topic: Design and analysis of automated truck cabin suspension system\n\n--SEPARATOR--\n\nDepartment: Mechanical Engineering\nFavorite Topics: Computer Aided Design(CAD), Control Systems, Automation\nProject Topic: Detached-Eddy Simulations of Active Control systems on a simplified car geometry\n\n--SEPARATOR--\n\nDepartment: Mechanical Engineering\nFavorite Topics: Strength of materials, Solid mechanics, Internal Combustion Engine\nProject Topic: Transient Heat Conduction in a Solidifying Alloy\n\n--SEPARATOR--\n\nDepartment: Mechanical Engineering\nFavorite Topics: Strength of materials, Solid mechanics, Internal Combustion Engine\nProject Topic: Power Generation from Internal Combustion Engine using ATG\n\n--SEPARATOR--\n\nDepartment:'

base_prompt_description='This program recieves a project topic and gives a description of the project\n\nProject Topic: Mini Solar water heater\nProject description: This project involves the design and fabrication of a portable solar water heater\n\n--SEPARATOR--\n\nProject Topic: Bluetooth Gamepad for Android Gaming\nProject description: The gamepad will have a unique designed and shaped PCB in the shape of a gamepad. The PCB will have 2 x joysticks mounted on it for transmitting movement and aim commands to the phone\n\n--SEPARATOR--\n\nProject Topic: Aerodynamic Modelling of Wind turbine Blades\nProject description: The purpose of this project will be to find a simple linear modification to the shape of wind turbine blades\n\n--SEPARATOR--\n\nProject Topic: The effect of untreated sugarcane ash on the setting time and compressive strength of concrete mix\nProject description: The main objective of this work is to compare the compressive strength of concrete in which some percentages of cement had been replaced with equal weight of sugarcane ash with that of normal concrete produced from the same mix ratio, and to determine the effect of sugar cane ash on the initial and final setting time of concrete\n\n--SEPARATOR--\n\nProject Topic: Ultrasonic radar project\nProject description: Build a system that can monitor an area of limited range and alerts authorities with a buzzer as an alarm\n\n--SEPARATOR--\n\nProject Topic: Solar wireless electric vehicle charging system\nProject description: The system demonstrates how electric vehicles can be charged while moving on road, eliminating the need to stop for charging\n\n--SEPARATOR--\n\nProject Topic: Glass Hybrid fibres epoxy composite material\nProject description: This project involves the characterization of epoxy-based hybrid composites\n\n--SEPARATOR--\n\nProject Topic: Performance evaluation of a solar powered poultry egg incubator\nProject description: In this study, a solar photovoltaic powered chicken egg incubator was designed, fabricated and tested to evaluate its performance\n\n--SEPARATOR--\n\nProject Topic: Identification of well problems using well testing\nProject description: This project work is concerned with the use of well testing in identifying well problems\n\n--SEPARATOR--\n\nProject Topic:'

def generate_topic(department, favorite_topics):
    response = co.generate(
      model='xlarge',
      prompt= base_prompt_topic+" "+ department+"\nFavorite Topics: "+favorite_topics+"\nProject Topic: ",
      max_tokens=20,
      temperature=0.8,
      k=0,
      p=0.7,
      frequency_penalty=0,
      presence_penalty=0,
      stop_sequences=["--SEPARATOR--"],
      return_likelihoods='NONE')
    Project_topic = response.generations[0].text
    Project_topic = Project_topic.replace("\n\n--SEPARATOR--","").replace("\n--SEPARATOR--","").strip()
    return Project_topic

def generate_description(Project_topic):
    response = co.generate(
      model='xlarge',
      prompt=  base_prompt_description+" "+ Project_topic+"\nProject description:",
      max_tokens=50,
      temperature=0.8,
      k=0,
      p=0.7,
      frequency_penalty=0,
      presence_penalty=0,
      stop_sequences=["--SEPARATOR--"],
      return_likelihoods='NONE')
    Project_description = response.generations[0].text
    Project_description = Project_description.replace("\n\n--SEPARATOR--","").replace("\n--SEPARATOR--","").strip()
    return Project_description

st.title(" 💡 Project Idea Generator")
st.markdown('This app was built using the Generate model and endpoint provided by Cohere.' , unsafe_allow_html=False)

st.markdown(
    """<a href="https://www.cohere.ai/">Click here to visit their site and start building</a>""", unsafe_allow_html=True,
)
st.header('What is this app about?🤔')

st.markdown('The purpose of this app is to help engineering students generate creative topics for their projects based on their department. The fun part about this app is that it allows you to enter your favorite topics to be able to streamline project topic suggestions that will interest you. Cool right?😎 Let us dive right in!', unsafe_allow_html=False)

form=st.form(key="user_settings")
with form:
    department_input=st.text_input('DEPARTMENT(Enter the name of your department in full)', key='department_input')
    favorite_courses_input=st.text_input('FAVORITE COURSE(S)(If you have two or more favorite courses, please separate with commas)', key='favorite_courses_input')
    num_input=st.slider("Number of Project Topics", value=2, key='num_input', min_value=1, max_value=10)

    generate_button=form.form_submit_button('Generate Project Topic Ideas🚀')
    
    if generate_button:
        if department_input=="" or favorite_courses_input=="":
            st.error("Field cannot be blank")
            
        else:
            my_bar=st.progress(0.05)
            st.subheader('Project Ideas')
            for i in range(num_input):
                st.markdown("""---""")
                Project_topic=generate_topic(department_input, favorite_courses_input)
                Project_description= generate_description(Project_topic)
                st.markdown("#### "+ Project_topic)
                st.write(Project_description)
                my_bar.progress((i+1)/num_input)
                
st.header('About The creator👨')
st.markdown('Tobechukwu is a 400 level student of the Department of Mechanical Engineering, University of Nigeria Nsukka. He is a Machine Learning Engineer and an Artificial Intelligence enthusiast with keen interest in NLP and Computer Vision.', unsafe_allow_html=False)
