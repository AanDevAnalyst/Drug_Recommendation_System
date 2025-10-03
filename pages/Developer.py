import streamlit as st

def show_developer_page():
    st.title("👨‍💻 Meet The Developer")

    st.markdown("""
    ### About Abduljabbar Nuhu: Developer & Data Analyst/ Data Scientist
    Hello, I'm Abduljabbar Nuhu, your Data Scientist with 2 years of experience in the field.  
    I am passionate about harnessing the power of technology to make a positive impact on people's lives.  
    Allow me to share a bit about my journey in the world of artificial intelligence and machine learning.
    """)

    st.markdown("### My Expertise")
    st.write("""
    With a strong academic background in electronics with physics and a deep fascination for AI and ML,  
    I embarked on a journey that has taken me across various challenges overcomed, working on diverse and innovative projects.  
    Over the years, I've had the privilege of involving myself in various internship projects that have pushed the boundaries of what's possible in AI and ML.
    """)

    st.markdown("### A Commitment to Excellence")
    st.write("""
    My work is driven by a commitment to excellence and a belief that technology should be accessible and beneficial to everyone.  
    Whether it's developing predictive models, creating intelligent algorithms, or designing user-friendly interfaces,  
    I strive for solutions that are both cutting-edge and user-centric.
    """)

    st.markdown("### Passion for Health Tech")
    st.write("""
    The development of Drug Recommender represents a convergence of my passion for AI and my dedication to improving healthcare accessibility.  
    I believe that AI has the potential to transform the way we approach healthcare, making it more personalized and informative.  
    This platform is a testament to that vision.
    """)

    st.markdown("### Join Me on this Journey")
    st.write("""
    I invite you to explore Drug Recommender and experience firsthand the fusion of AI and healthcare.  
    Together, we can empower individuals with knowledge, promote well-being, and contribute to a brighter and healthier future.
    """)

    # New section for Linktree
    st.markdown("---")
    st.subheader("🔗 Connect with Me")
    st.write("You can find all my important links, projects, and socials here:")
    st.markdown("[🌐 Visit my Linktree](https://linktr.ee/aandevanalyst)")

    st.info("✨ Thank you for visiting the developer’s page!")

# To make this page run directly when selected in Streamlit's sidebar navigation
if __name__ == "__main__":
    show_developer_page()
