import streamlit as st
from streamlit_option_menu import option_menu
from streamlit.components.v1 import html
import requests
from streamlit_lottie import st_lottie
import json
import base64
from PIL import Image
from streamlit_extras.mention import mention
from streamlit_extras.app_logo import add_logo

st.set_page_config(page_title="Kushal Agrawal", page_icon = "🧑‍💻",layout= "wide",initial_sidebar_state="auto")

st.markdown('<style>'+open('style/style.css').read()+'</style>',unsafe_allow_html=True)

def load_lottie(filepath:str):
    with open(filepath,"r") as f:
        return json.load(f) 

def show_pdf(file_path):
        with open(file_path,"rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="400" height="600" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)

def pdf_link(pdf_url, link_text="Click here to view PDF"):
    href = f'<a href="{pdf_url}" target="_blank">{link_text}</a>'
    return href

kushal_img = Image.open("./images/kushal_linkedin.png")
linkedin_img = Image.open("./images/linkedin.png")
email_img = Image.open("./images/email.png")
github_img = Image.open("./images/github.png")
dboy_img = Image.open("./images/3d boy.png")
sn_src_img = Image.open("./images/sumeetrahul.png")
src_img = Image.open("./images/st_conrads.png")
iet_img = Image.open("./images/Iet.png")
contact_img = Image.open("./images/contact.png")
iit_img = Image.open("./images/iit_jodhpur.jpg")
techuplabs_img = Image.open("./images/techuplabs_logo.jpeg")
resume_img = Image.open('./images/resume.png')
moa_img = Image.open("./images/moa.jpg")
casava_img = Image.open("./images/casava.jpg")
am_exp_img = Image.open("./images/am_exp.png")
ranzcr_img = Image.open("./images/ranzcr.jpg")
umoja_img = Image.open("./images/umoja.jpg")
codegpt_img = Image.open("./images/codegpt.png")
memegpt_img = Image.open("./images/memegpt.jpg")
sentiment_img = Image.open("./images/sentiment.jpg")
timeseries_img = Image.open("./images/time_series.jpg")
sitegpt_img = Image.open("./images/sitegpt.png")

def social_icons(width=24,height=24,**kwargs):
    icon_template = '''
        <a href="{url}" target="_blank" style="margin-right: 20px; color:#7ad3f6">
            <img src="{icon_src}" alt="{alt_text}" width="{width}" height="{height}">
        </a>
        '''

    icons_html = ""
    for name, url in kwargs.items():
        icon_src ={
            "linkedin":"https://img.icons8.com/ios-filled/50/000000/linkedin.png",
            "github":"https://img.icons8.com/ios-filled/50/000000/github.png",
            "kaggle":"https://img.icons8.com/windows/32/000000/kaggle.png",
            "email":"https://img.icons8.com/ios-glyphs/30/000000/new-post.png"
        }.get(name.lower())

        if icon_src:
            icons_html += icon_template.format(url=url,icon_src=icon_src,alt_text=name.capitalize(),width=width,height=height)

    return icons_html     

def load_gif(path:str):
    file_ = open(path, "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()   
    return data_url

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('bg.jpg')

def skill_txt(a,b):
    col1,col2 = st.columns([2,4])
    with col1:
        st.markdown(f'<p style="font-size: 20px;">{a}</p>', unsafe_allow_html=True)
    with col2:
        b_no_commas = b.replace(',', '')
        st.markdown(b_no_commas)
        
#Sidebar: If using streamlit_option_menu
with st.sidebar:
    with st.container():
        l,m,r=st.columns((0.75,2,1))
        with l:
            st.empty()
        with m:
            st.image(kushal_img,width=175)
        with r:
            st.empty()
    
    choose = option_menu("Kushal Agrawal",
                         ["About Me","Experience","Technical Skills","Education","Projects","Competitions","Resume","Contact"],
                         icons=['person fill','clock history','tools','book half','clipboard','trophy fill','paperclip','envelope'],
                         menu_icon='mortarboard',
                         default_index=0,
                         styles={
        "container": {"margin": "0 0 0 5px", "background-color": "#7ad3f6",'border-radius': '0px','color':'black'},
        "icon": {"font-size": "20px","color":"rgb(16, 0, 186)"}, 
        "nav-link": {"font-size": "17px", "text-align": "left", "margin":"0px", "--hover-color": "#eee",'color':'black'},
        "nav-link-selected": {"font-size": "17px","background-color": "#5eafcf",'color':'white'},
    }
    )
    linkedin_url = "https://www.linkedin.com/in/kushal-agrawal-36a387168/"
    kaggle_url = "https://www.kaggle.com/kushal1506"
    github_url = "https://github.com/kushal150699"
    email_url =  "mailto:kushal.codes.ai@gmail.com"
    with st.container():
        l,m,r = st.columns((0.25,2,0.25))
        with l:
            st.empty()
        with m:
            st.markdown(
                social_icons(30,30,LinkedIn=linkedin_url,Github=github_url,Kaggle=kaggle_url,Email=email_url),
                unsafe_allow_html=True)
        with r:
            st.empty()    

st.write('<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True)
st.title(":black[Kushal Agrawal]")

if choose == "About Me":
    #aboutme.createPage()
    with st.container():
        left_column, middle_column, right_column = st.columns((1,0.1,0.5))
        with left_column:
            st.header("About Me")
            st.subheader("Aspiring Machine Learning Engineer")
            st.markdown('<p class="big-font">👋🏻 Hello, I am Kushal Agrawal, currently immersed in the dynamic realm of Artificial Intelligence as an M.Tech student at IIT Jodhpur. Having prior relevant experiences in tech, I am constantly seeking unique internships to broaden my horizons before embarking on my AI career upon post graduation.</p>', unsafe_allow_html=True)
            st.markdown('<p class="big-font">🏋🏻 In addition, I like to exercise in the gym, run, write, play video games and... enjoy eating good food in my free time!</p>', unsafe_allow_html=True)
            st.markdown('<p class="big-font">👨🏼‍💻 Academic interests: Data Science , Machine Learning, Computer Vision , Natural language Processing</p>', unsafe_allow_html=True)
            st.markdown('<p class="big-font">💭 Ideal Career Prospects: Data Scientist, ML Engineer , AI Developer</p>', unsafe_allow_html=True)
            st.write("📄 [Resume](https://spc.iitj.ac.in/media/resume/Kushal_Agrawal_M23CSA011_5126_IITJodhpur.pdf)")
        with middle_column:
            st.empty()
        with right_column:
            st.image(dboy_img,width=275)

if choose=="Experience":
    st.header("Experience")
    with st.container():
        image_column,text_column = st.columns((1,5))
        with image_column:
            st.image(techuplabs_img)
        with text_column:
            st.subheader("Machine Learning Engineer, [TechUp Labs](https://www.techuplabs.com/)") 
            st.write("*January to June 2023* | [*Experience letter*](https://drive.google.com/file/d/1cQdgzMQYqcgJu2M-NuMkGQDjWVOebTmy/view?usp=sharing)")
            st.markdown("""
                        - Took 6 active building projects / AI Tools from research to development to completion in under 4 months. 
                        - Created "OneForAll CodeGPT," an all-in-one application for resolving various code-related issues using LLM's.within 1 week. 
                        - Utilized LLM's to develop "MemeCap," a meme generation tool capable of creating memes from random or personal images within 1 week. 
                        - Designed and implemented a Site chatbot that allows users to communicate with their website using a sitemap within 4 days. 
                        - Build API's to automate 100% of repetitive work. Developed DataStudio dashboards that increased HR efficiency by 25%.         
                        
                        `Python` `Langchain` `Streamlit` `ChatGPT` `LLM's` `Vector databases` `Amazon EC2` `FastAPI` 
                        """)   
    st.markdown("")        
    with st.container():
        image_column,text_column = st.columns((1,5))
        with image_column:
            st.image(techuplabs_img)
        with text_column:
            st.subheader("Machine Learning Intern, [TechUp Labs](https://www.techuplabs.com/)") 
            st.write("*October 2022 to January 2023* | [*Experience letter*](https://drive.google.com/file/d/1cQdgzMQYqcgJu2M-NuMkGQDjWVOebTmy/view?usp=sharing)")
            st.markdown("""
                        - Worked on User Data Analysis to find behavioural pattern of users.
                        - Worked on some internal projects including Time series forecasting , Sentiment analysis on Audio and Text data.       
                        
                        `Python` `Matplotlib` `Pandas` `TimeSeries Forecasting` `FastAPI` `LSTM` `Transformers`
                        """)   

elif choose == "Technical Skills":

    st.header("Technical Skills")
    skill_txt("Programming Languages","`Python`, `C`")
    skill_txt("Data Visualization", "`matplotlib`, `seaborn`, `Plotly`, `Google Analytics`")
    skill_txt("Cloud Platforms", "`Amazon Web Services`, `Streamlit Cloud`, `Hugging Face`")
    skill_txt("Version Control", "`Git`, `Docker`")
    skill_txt("Design and Front-end Development","`HTML`, `CSS`, `Streamlit` `Gradio`")
    skill_txt("Machine Learning Frameworks", "`Numpy`, `Pandas`, `Scikit-Learn`, `Pytorch` ")
    skill_txt("Natural Language Processing", "`NLTK`, `Word2Vec`, `TF-IDF`, `Transformers` `LSTM` `RNN`")
    skill_txt("Computer Vision", "`OpenCV`, `scikit-image`, `CNN`, `Transfer Learning`, `GAN`, `VAE`")
    skill_txt("Miscellaneous", "`Microsoft Office`, `Microsoft Powerpoint`")

elif choose == "Education":
    st.header("Education")
    with st.container():
        image_column, text_column = st.columns((1,2.5))
        with image_column:
            st.image(iit_img)
        with text_column:
            st.subheader("M.Tech - [Indian Institute of Technology , Jodhpur](https://www.iitj.ac.in/) (2023-present)")
            st.write("Relevant Coursework : Machine Learning , Artificial Intelligence , Deep Learning , Computer Vision , ML-Ops , DL-Ops , Autonomous Systems")
            st.markdown(""" 
            - CGPA/Percentage -  7.71 CGPA
            """)
    with st.container():
        image_column, text_column = st.columns((1,2.5))
        with image_column:
            st.image(iet_img)
        with text_column:
            st.subheader("B.Tech - [Institute of Engineering and Technology , Lucknow](https://www.ietlucknow.ac.in/) (2018-2022)")
            st.write("Relevant Coursework: Major: Mechanical Engineering , Minor: Python programming , Data Structure and Alogorithms , Artificial Intelligence")
            st.markdown(""" 
            - CGPA/Percentage -  8.41 CGPA
            - Volunteer (MechFest)
            """)
    # with st.container():
    #     image_column, text_column = st.columns((1,2.5))
    #     with image_column:
    #         st.image(sn_src_img)
    #     with text_column:
    #         st.subheader("Senior Secondary - [Sumeet Rahul Goel Memorial School](https://srgms.org/) (2017)")
    #         st.write("Coursework: English , Mathematics , Physics , Chemistry , Painting")
    #         st.markdown(""" 
    #         - CGPA/Percentage - 90 %
    #         """)
    # with st.container():
    #     image_column, text_column = st.columns((1,2.5))
    #     with image_column:
    #         st.image(src_img)
    #     with text_column:
    #         st.subheader("Secondary - [St. Conrad's Inter College](https://www.conrads.in//) (2015)")
    #         st.write("Coursework: English , Hindi , Mathematics , Science , History , Civics and Geography , Computer Applications")
    #         st.markdown(""" 
    #         - CGPA/Percentage - 95.2 % 
    #         """)

elif choose == "Projects":
    st.header("Projects")
    with st.container():
        image_column,text_column = st.columns((1,3))
        with image_column:
            st.image(codegpt_img)
        with text_column:
            st.header("[OneForALL CodeGPT](https://www.linkedin.com/posts/kushal-agrawal-36a387168_chatgpt-openai-ai-activity-7067746929627062272-w9kN?utm_source=share&utm_medium=member_desktop)")
            st.write(""" 
                    - An all-in-one application for resolving various code-related issues.
                    - Functionalities: Bug Fixer | Code Commenter | Code Generator | Code Optimizer | Code Converter | Code Explainer | Documentation Generator | Error Diagnostician | Follow Ups 
                    - Tools & technologies used: GPT | ChatGPT API | Prompt Engineering | Streamlit App """)
    st.markdown("")        
    with st.container():
        image_column,text_column = st.columns((1,3))
        with image_column:
            st.image(memegpt_img)
        with text_column:
            st.header("[MemeGPT](https://www.linkedin.com/posts/kushal-agrawal-36a387168_business-project-salesforce-activity-7065287187126190081-qRG5?utm_source=share&utm_medium=member_desktop)")
            st.write("""
                    - Takes two types of input either image file or image URL . Then converts it into a meme image , once image is generated you can also download the meme image.         
                    - Tools & technologies used:
                    1) Image to caption :-Hugging Face -> Salesforce/blip-image-captioning-base model
                    2) got-3.5-turbo :- for generating meme caption using the ai image description and user image description. Though the user image description is optional . 
                    - GPT | ChatGPT API | Prompt Engineering | Streamlit App  
                    """)   
    st.markdown("")        
    with st.container():
        image_column,text_column = st.columns((1,3))
        with image_column:
            st.image(sitegpt_img)
        with text_column:
            st.header("SiteGPT")
            st.write("""
                    - Takes two types of input either URL to website sitemap or URL filter pattern . Then extracts the data from the site.
                    - Once the data is extracted frome the web and converted into database , you can start querying the data. 
                    - Tools and Technologies Used: GPT | ChatGPT API | Prompt Engineering | Streamlit App  
                    """)        
    st.markdown("")        
    with st.container():
        image_column,text_column = st.columns((1,3))
        with image_column:
            st.image(am_exp_img)
        with text_column:
            st.header("[American Express - Default Prediction](https://www.kaggle.com/competitions/amex-default-prediction)")
            st.write("""
                    - Developed a 2 Stage stacking of Boosting and Neural Network models to predict the credit card default on train dataset of 
                    approx 5.5 million samples and test dataset of approx 1 million samples. 
                    """)
            mention(label="Github Repo",icon="github",url="https://github.com/kushal150699/Amex")     
    st.markdown("")
    with st.container():
        image_column,text_column = st.columns((1,3))
        with image_column:
            st.image(sentiment_img)
        with text_column:
            st.header("[Tweet Sentiment Extraction A.K.A Question Answering](https://www.kaggle.com/competitions/tweet-sentiment-extraction)")
            st.write("""
                    - Extraction of text that determines the sentiment of the tweet.
                    - Tools & technologies used: BERT | RoBerta | Plotly 
                    """) 
            mention(label="Kaggle",icon="",url="https://www.kaggle.com/code/kushal1506/tweet-sentiment-extraction-a-k-a-questionanswering/notebook") 
    st.markdown("")        
    with st.container():
        image_column,text_column = st.columns((1,3))
        with image_column:
            st.image(timeseries_img)
        with text_column:
            st.header("TimeSeries Forecasting")
            st.write("""
                    - TimeSeries Forecasting on S&P 500 Historical Data
                    - Technologies used : ARIMA | LSTM | Plotly | Matplotlib | Seaborn | Statsmodels 
                    """)                                       
            mention(label="Kaggle",icon="",url="https://www.kaggle.com/code/kushal1506/timeseries-s-p500-stockanalysis-arima-lstm") 

elif choose == "Competitions":
    st.header("Competitions")
    with st.container():
        image_column,text_column = st.columns((1,3))
        with image_column:
            st.image(moa_img,width=215)
        with text_column:
            st.header("[Mechanisms of Action (MoA) Prediction](https://www.kaggle.com/competitions/lish-moa)")
            st.write(""" 
                     - Secured Rank 47/4373  
                     - Determined mechanism of action of a new drug based on the gene expression and cell viability information. 
                     - Tech used: RandomForestClassifier , Exploratory Data Analysis | Feature Engineering | Ensemble | Pytorch """)
            mention(label="Github Repo",icon="github",url="https://github.com/kushal150699/Kaggle-MOA-Prediction/blob/main/moa-prediction-complete-walkthrough-eda-ensemble.ipynb")
    st.markdown("")        
    with st.container():
        image_column,text_column = st.columns((1,3))
        with image_column:
            st.image(casava_img)
        with text_column:
            st.header("[Cassava Leaf Disease Classification](https://www.kaggle.com/competitions/cassava-leaf-disease-classification)")
            st.write("""
                    - Secured Rank 111/3900 
                    - Classified each cassava image into four disease categories 
                    - Tech Used: ResNet | EfficientNet | DataAugmentation. 
                    """)   
    st.markdown("")        
    with st.container():
        image_column,text_column = st.columns((1,3))
        with image_column:
            st.image(am_exp_img)
        with text_column:
            st.header("[American Express - Default Prediction](https://www.kaggle.com/competitions/amex-default-prediction)")
            st.write("""
                    - Secured Solo Rank 1742 / 4874 
                    - Developed a 2 Stage stacking of Boosting and Neural Network models to predict the credit card default on train dataset of 
                    approx 5.5 million samples and test dataset of approx 1 million samples. 
                    """)
            mention(label="Github Repo",icon="github",url="https://github.com/kushal150699/Amex")     
    st.markdown("")
    with st.container():
        image_column,text_column = st.columns((1,3))
        with image_column:
            st.image(ranzcr_img)
        with text_column:
            st.header("[RANZCR CLiP - Catheter and Line Position Challenge](https://www.kaggle.com/competitions/ranzcr-clip-catheter-line-classification)")
            st.write("""
                    - Secured Rank 144 / 15474 
                    - Classified the presence and correct placement of tubes on chest x-rays to save lives
                    - Tech Used: Resnet | Seresnet | EfficientNet | Ensemble
                    """) 
    st.markdown("")        
    with st.container():
        image_column,text_column = st.columns((1,3))
        with image_column:
            st.image(umoja_img)
        with text_column:
            st.header("[UmojaHack India: Income Prediction Challenge](https://zindi.africa/competitions/umojahack-india-2022)")
            st.write("""
                    - Secured Solo Rank 17/232 participants 
                    - Income prediction challenge (binary classification) on a highly imbalanced datsaset. 
                    """)                                       

elif choose == "Resume":   
    resume_url = "https://spc.iitj.ac.in/media/resume/Kushal_Agrawal_M23CSA011_5126_IITJodhpur.pdf"
    st.header("Resume")
    with st.container():
        resume_column,image_column = st.columns((3,2))
    with resume_column:  
        st.markdown('<p class="big-font">In case your current browser cannot display the PDF documents, do refer to the hyperlink below!</p>', unsafe_allow_html=True)
        st.markdown(pdf_link(resume_url, "**Resume**"), unsafe_allow_html=True)  
        show_pdf("Kushal_resume.pdf")
        with open("Kushal_resume.pdf", "rb") as file:
            btn = st.download_button(
                label="Download Resume",
                data=file,
                file_name="Kushal_resume.pdf",
                mime="application/pdf"
            )
    with image_column:
        st.image(resume_img)        

elif choose == "Contact":
    st.header("Contact")
    with st.container():
        text_column , mid , image_column = st.columns((1,0.1,0.5))
        with text_column:
            st.write("Let's stay in touch! Feel free to drop me a line at kushal.codes.ai@gmail.com, or simply use the form below. I look forward to connecting with you!")

            contact_form = """<form action="https://formsubmit.co/kushal.codes.ai@gmail.com" method="POST">
                            <input type="hidden" name="_captcha" value="false">
                            <input type="hidden" name="_cc" value="m23csa011@gmail.com">
                            <input type="hidden" name="_template" value="table">
                            <input type="text" name="name" placeholder="Your name" required>
                            <input type="email" name="email" placeholder="Your email" required>
                            <textarea name="message" placeholder="Your message here"></textarea>
                            <button type="submit">Send</button>
                        </form> 
                        """
            st.markdown(contact_form,unsafe_allow_html=True)
            st.markdown("")
            st.write("Alternatively, feel free to check out my social accounts below!")
            linkedin_url = "https://www.linkedin.com/in/kushal-agrawal-36a387168/"
            kaggle_url = "https://www.kaggle.com/kushal1506"
            github_url = "https://github.com/kushal150699"
            email_url =  "mailto:kushal.codes.ai@gmail.com"
            with st.container():
                l,m,r = st.columns((0.25,2,0.25))
                with l:
                    st.empty()
                with m:
                    st.markdown(
                        social_icons(30,30,LinkedIn=linkedin_url,Github=github_url,Kaggle=kaggle_url,Email=email_url),
                        unsafe_allow_html=True)
                with r:
                    st.empty()    

        with mid:
            st.empty()
        with image_column:
            st.image(contact_img)        