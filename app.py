import streamlit as str

# Set webpage configuration
str.set_page_config(
    page_title="Harsh Saxena - Professional Portfolio",
    page_icon="💼",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Clean Professional Custom CSS Styles
custom_css = """
<style>
    /* Hide Streamlit elements for a cleaner portfolio look */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Global Container */
    .resume-container {
        font-family: 'Segoe UI', sans-serif;
        color: #333333;
        background: #ffffff;
        padding: 30px;
        border-radius: 8px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
        margin-top: -50px;
    }
    
    /* Header Section */
    .header-section {
        border-bottom: 2px solid #1a365d;
        padding-bottom: 20px;
        margin-bottom: 25px;
    }
    .main-title {
        font-size: 34px;
        color: #1a365d;
        text-transform: uppercase;
        font-weight: 700;
        letter-spacing: 1px;
        margin-bottom: 5px;
    }
    .subtitle {
        font-size: 19px;
        color: #4a5568;
        font-weight: 600;
        margin-bottom: 15px;
    }
    .contact-info {
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
        font-size: 14.5px;
    }
    .contact-info a {
        color: #3182ce;
        text-decoration: none;
        font-weight: 500;
    }
    
    /* Section Headings */
    .section-title {
        font-size: 18px;
        color: #1a365d;
        text-transform: uppercase;
        border-bottom: 2px solid #e2e8f0;
        padding-bottom: 5px;
        margin-top: 25px;
        margin-bottom: 15px;
        letter-spacing: 0.5px;
        font-weight: 700;
    }
    
    /* Experience / Projects Text */
    .item-header {
        display: flex;
        justify-content: space-between;
        align-items: baseline;
        margin-bottom: 4px;
    }
    .item-title {
        font-size: 15.5px;
        font-weight: 700;
        color: #2d3748;
    }
    .item-org {
        font-size: 15px;
        font-weight: 600;
        color: #4a5568;
    }
    .item-date {
        font-size: 14px;
        color: #718096;
        font-weight: 600;
    }
    .bullet-list {
        margin-left: 20px;
        margin-bottom: 15px;
    }
    .bullet-list li {
        font-size: 14.5px;
        color: #4a5568;
        margin-bottom: 5px;
        text-align: justify;
    }
    .project-tech {
        font-size: 14px;
        color: #3182ce;
        margin-bottom: 5px;
    }
    
    /* Skills Columns styling */
    .skills-box {
        background-color: #f7fafc;
        padding: 15px;
        border-radius: 6px;
        border-left: 4px solid #3182ce;
        height: 100%;
    }
    .skills-box h3 {
        font-size: 14px;
        color: #2d3748;
        text-transform: uppercase;
        margin-bottom: 10px;
        letter-spacing: 0.5px;
        font-weight: 700;
    }
    .skills-box ul {
        list-style-type: none;
        padding-left: 0;
    }
    .skills-box li {
        font-size: 14px;
        color: #4a5568;
        margin-bottom: 6px;
    }
</style>
"""
str.markdown(custom_css, unsafe_allow_html=True)

# Main Resume View Wrapper
str.markdown('<div class="resume-container">', unsafe_allow_html=True)

# --- HEADER SECTION ---
str.markdown("""
<div class="header-section">
    <div class="main-title">Harsh Saxena</div>
    <div class="subtitle">AI / Data Science Professional & VAPT Engineer</div>
    <div class="contact-info">
        <span><strong>📞 Phone:</strong> +91 9359452007</span>
        <span><strong>✉️ Email:</strong> <a href="mailto:harshsaxena663@gmail.com">harshsaxena663@gmail.com</a></span>
        <span><strong>🔗 LinkedIn:</strong> <a href="https://linkedin.com/in/harsh-saxena777" target="_blank">harsh-saxena777</a></span>
    </div>
</div>
""", unsafe_allow_html=True)

# --- PROFESSIONAL SUMMARY ---
str.markdown('<div class="section-title">Professional Summary</div>', unsafe_allow_html=True)
str.markdown("""
<p style="font-size: 14.5px; color: #4a5568; text-align: justify; line-height: 1.6;">
    Results-driven B.Tech Computer Science student with hands-on enterprise-level internship experience specializing in end-to-end AI/ML development (NLP, Speech-to-Text) and Cyber Security infrastructure (VAPT). Proven capability in building data-driven systems, preprocessing complex structured/unstructured datasets, and validating cloud environment vulnerabilities. Enthusiastic about delivering highly reliable cognitive products and enterprise solutions within dynamic, AI-native platforms.
</p>
""", unsafe_allow_html=True)

# --- PROFESSIONAL EXPERIENCE ---
str.markdown('<div class="section-title">Professional Experience</div>', unsafe_allow_html=True)

# Job 1
str.markdown("""
<div class="item-header">
    <span class="item-title">AI/ML INTERN</span>
    <span class="item-org">Softpro Computer Technologies Pvt. Ltd</span>
</div>
<ul class="bullet-list">
    <li>Engineered predictive data models using Python to extract actionable insights from vast multi-structured enterprise data pools.</li>
    <li>Architected extraction and ingestion workflows for large-scale natural language data to achieve clean, high-fidelity inputs for downstream model layers.</li>
    <li>Collaborated on building "Softpro Analytics", implementing Cognitive features with an emphasis on Speech-to-Text systems and automated Sentiment Analysis.</li>
</ul>
""", unsafe_allow_html=True)

# Job 2
str.markdown("""
<div class="item-header">
    <span class="item-title">VAPT INTERN</span>
    <span class="item-org">DRDO, Ministry of Defence (MoD)</span>
</div>
<ul class="bullet-list">
    <li>Monitored and managed targeted cloud network traffic channels to catch baseline security deviations, effectively safeguarding data custody.</li>
    <li>Conducted system-wide vulnerability sweeps and structural penetration test scenarios to discover, document, and eliminate system exploits.</li>
    <li>Authored technical threat maps, converting sophisticated vulnerability risk metrics into highly readable product risk reporting for corporate and non-technical leadership.</li>
</ul>
""", unsafe_allow_html=True)

# --- KEY PROJECTS ---
str.markdown('<div class="section-title">Key Machine Learning & Security Projects</div>', unsafe_allow_html=True)

# Project 1
str.markdown("""
<div class="item-header"><span class="item-title">Business Analytics & Sentiment Analysis Automation Engine</span></div>
<div class="project-tech"><strong>Stack:</strong> Python, Natural Language Processing (NLP), Speech-to-Text Frameworks, Sentiment Assessment Engines</div>
<p style="font-size: 14.5px; color: #4a5568; text-align: justify; margin-bottom: 15px;">
    Designed and deployed an automated end-to-end processing architecture to dynamically map acoustic inputs from customer-consultor touchpoints into categorical behavioral signals, enabling business operations to proactively handle user engagement fluctuations.
</p>
""", unsafe_allow_html=True)

# Project 2
str.markdown("""
<div class="item-header"><span class="item-title">Enterprise Infrastructure Security Auditing (VAPT)</span></div>
<p style="font-size: 14.5px; color: #4a5568; text-align: justify; margin-bottom: 15px;">
    Constructed an exhaustive penetration sandbox matching core corporate structural systems; evaluated data containment capabilities by handling defensive cryptography assessments and testing enterprise-grade network firewalls against common cloud infrastructure vectors.
</p>
""", unsafe_allow_html=True)

# --- EDUCATION ---
str.markdown('<div class="section-title">Education</div>', unsafe_allow_html=True)
str.markdown("""
<div class="item-header">
    <span class="item-title">Bachelor of Technology (Computer Science & Engineering)</span>
    <span class="item-date">2022 - 2026</span>
</div>
<p style="font-size: 14.5px; color: #4a5568; margin-bottom: 10px;">Dr. A.P.J Abdul Kalam Technical University</p>

<div class="item-header">
    <span class="item-title">Senior Secondary School (PCM)</span>
    <span class="item-date">2021 - 2022</span>
</div>
<p style="font-size: 14.5px; color: #4a5568; margin-bottom: 10px;">Central Board of Secondary Education</p>
""", unsafe_allow_html=True)

# --- SKILLS & COMPETENCIES (Leveraging Streamlit Grid) ---
str.markdown('<div class="section-title">Skills & Competencies</div>', unsafe_allow_html=True)

col1, col2, col3 = str.columns(3)

with col1:
    str.markdown("""
    <div class="skills-box">
        <h3>AI & Software</h3>
        <ul>
            <li>Python & Dart</li>
            <li>NLP & Text Processing</li>
            <li>Predictive Modeling</li>
            <li>HTML5 & React Ecosystem</li>
            <li>Full Stack Architecture</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    str.markdown("""
    <div class="skills-box">
        <h3>Data & Cloud Security</h3>
        <ul>
            <li>Vulnerability Assessment (VAPT)</li>
            <li>Structured Data Engineering</li>
            <li>Information Integrity</li>
            <li>Agile/Scrum Environments</li>
            <li>Analytical Diagnostics</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col3:
    str.markdown("""
    <div class="skills-box">
        <h3>Languages</h3>
        <ul>
            <li>Hindi (Native proficiency)</li>
            <li>English (Professional capability)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

str.markdown('</div>', unsafe_allow_html=True)

# --- INTERACTIVE STREAMLIT INTERACTION SIDEBAR ---
with str.sidebar:
    str.title("Contact Me Directly")
    str.info("Feel free to drop a quick message to my inbox via this panel or secure a copy of my traditional layout.")
    
    # Download Button for Offline PDF Use
    # (Assuming you keep a static copy in your directory)
    try:
        with open("HarshResume.pdf", "rb") as pdf_file:
            pdf_bytes = pdf_file.read()
        str.download_button(
            label="📄 Download Traditional PDF Resume",
            data=pdf_bytes,
            file_name="Harsh_Saxena_Resume.pdf",
            mime="application/pdf"
        )
    except FileNotFoundError:
        pass
