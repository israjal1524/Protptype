# This code requires Streamlit, which must be installed in your environment:
# pip install streamlit

try:
    import streamlit as st

    st.set_page_config(page_title="LeapLaunch MVP", layout="centered")
    st.title("LeapLaunch - MVP Prototype")
    st.markdown("Your Career Navigator for the U.S. Job Market")

    st.header("Career Path Navigator")
    degree = st.text_input("Your Degree Program", "e.g. MS in Computer Science")
    skills = st.text_input("Your Key Skills", "e.g. Python, SQL, Machine Learning")
    interest = st.selectbox("Industries of Interest", ["Technology", "Finance", "Healthcare", "Consulting", "Design"])

    if st.button("Suggest Career Paths"):
        st.subheader("Suggested Career Paths")
        st.markdown(f"Based on your degree in **{degree}** and skills in **{skills}**, we suggest exploring opportunities in the **{interest}** industry such as:")
        st.markdown("""
        - Business/Data Analyst at companies with H1B sponsorship  
        - Product Internships in mid-sized tech startups  
        - STEM OPT-eligible roles with strong growth trajectory
        """)

    st.header("Visa-Friendly Job Listings")
    st.markdown("Here are sample curated job opportunities for international students:")
    st.markdown("""
    - Software Engineer Intern - Google (H1B Friendly)  
    - Data Analyst - Deloitte (OPT/CPT Eligible)  
    - Product Manager - Amazon (STEM OPT)  
    """)

    st.header("Resume Optimizer")
    resume_text = st.text_area("Paste your resume text below")
    if st.button("Score My Resume"):
        score = min(100, len(resume_text.strip()) // 20)
        feedback = "Strong Resume" if score > 70 else ("Needs Improvement" if score > 40 else "Revise Heavily")
        st.markdown(f"**Score:** {score}/100 - {feedback}")

except ModuleNotFoundError as e:
    print("Streamlit is not installed in this environment.")
    print("Install it with: pip install streamlit")
