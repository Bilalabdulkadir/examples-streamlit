import streamlit as st

st.set_page_config(
    page_title="Bilal MSc AI Portfolio",
    page_icon="🎓",
    layout="wide"
)

st.title("Bilal Abdulkadir Muhammed")
st.subheader("MSc Artificial Intelligence | UWE Bristol")

st.markdown("""
## About Me

I am an MSc Artificial Intelligence student at UWE Bristol with interests in:

- Machine Learning
- Data Science
- Statistical Inference
- Reproducible Research
- Data Visualisation
""")

st.header("Featured Projects")

st.markdown("""
### Week 4 Harvard Referencing Notebook
Kaggle notebook demonstrating academic referencing workflows and reproducible documentation.

### Week 4 Advanced Task Referencing Dataset
Dataset supporting referencing and citation management exercises.

### Kickstarter Statistical Analysis
Statistical inference project involving exploratory data analysis, hypothesis testing, and research planning.

### Iris Dataset Analysis
Data visualisation using ggplot2, including histograms, boxplots, and scatterplots.

### Multiple Regression Analysis
Model development, variable selection, AIC comparison, and interpretation.
""")

st.header("Technical Skills")

skills = [
    "Python",
    "R",
    "ggplot2",
    "tidyverse",
    "Statistical Inference",
    "Machine Learning",
    "Streamlit",
    "GitHub",
    "Kaggle",
    "Reproducible Research"
]

for skill in skills:
    st.write("✅", skill)

st.header("Portfolio Links")

st.markdown("""
- GitHub: https://github.com/Bilalabdulkadir
- Kaggle: https://www.kaggle.com/bilalabdulkadir1
- LinkedIn: https://www.linkedin.com/in/bilalabdulkadir
- Portfolio: https://bilalmuhammed-msc-ai-portfolio.share.connect.posit.cloud
""")
