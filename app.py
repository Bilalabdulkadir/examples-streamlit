import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Bilal MSc AI Portfolio",
    page_icon="🎓",
    layout="wide"
)

# Header
st.title("Bilal Abdulkadir Muhammed")
st.subheader("MSc Artificial Intelligence | University of the West of England (UWE Bristol)")

# About Me
st.markdown("""
## 👨‍💻 About Me

I am an MSc Artificial Intelligence student at UWE Bristol with interests in:

- 🤖 Machine Learning
- 📊 Data Science
- 📈 Statistical Inference
- 🔬 Reproducible Research
- 📉 Data Visualisation
- 🐍 Python Programming
- 📚 R Programming
- 🌐 AI Application Development

My work focuses on combining statistical methods, machine learning, and data-driven decision making to solve real-world problems.
""")

# Projects
st.markdown("---")
st.header("🚀 Featured Projects")

st.markdown("""
### 📖 Week 4 Harvard Referencing Notebook
Academic notebook demonstrating referencing workflows, citation management, and reproducible documentation.

### 📑 Week 4 Advanced Task Referencing Dataset
Dataset supporting referencing, academic writing, and citation management exercises.

### 💰 Kickstarter Statistical Analysis
Statistical inference project involving:

- Exploratory Data Analysis (EDA)
- Hypothesis Testing
- Chi-Square Analysis
- Research Planning

### 🌸 Iris Dataset Analysis
Data visualisation project using ggplot2 featuring:

- Histograms
- Boxplots
- Scatterplots
- Statistical Summaries

### 📊 Multiple Regression Analysis
Advanced regression modelling including:

- Variable Selection
- AIC Comparison
- Model Diagnostics
- Bootstrapping
""")

# Skills
st.markdown("---")
st.header("🛠 Technical Skills")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
### Programming
✅ Python  
✅ R  
✅ SQL  

### Data Science
✅ Pandas  
✅ NumPy  
✅ ggplot2  
✅ tidyverse  
""")

with col2:
    st.markdown("""
### AI & Analytics
✅ Machine Learning  
✅ Statistical Inference  
✅ Data Visualisation  
✅ Reproducible Research  

### Tools
✅ GitHub  
✅ Kaggle  
✅ Streamlit  
✅ Posit Connect Cloud  
""")

# Education
st.markdown("---")
st.header("🎓 Education")

st.markdown("""
**MSc Artificial Intelligence**  
University of the West of England (UWE Bristol)

Focus Areas:
- Machine Learning
- Statistical Inference
- Data Science
- Research Methods
- AI Applications
""")

# Portfolio Links
st.markdown("---")
st.header("🔗 Portfolio Links")

st.markdown("""
- 🌐 Portfolio Website: https://bilalmuhammed-msc-ai-portfolio.share.connect.posit.cloud
- 💻 GitHub: https://github.com/Bilalabdulkadir
- 📊 Kaggle: https://www.kaggle.com/bilalabdulkadir1
- 🔗 LinkedIn: https://www.linkedin.com/in/bilalabdulkadir
""")

# Footer
st.markdown("---")
st.caption(
    "Bilal Abdulkadir Muhammed | MSc Artificial Intelligence Portfolio | UWE Bristol"
)
