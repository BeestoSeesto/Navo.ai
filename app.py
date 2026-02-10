"""
Navo Web Interface
Clean, simple web UI for legal situation explanations
"""

import streamlit as st
from navo import NavoExplainer

# Page config
st.set_page_config(
    page_title="Navo - Legal Situation Explainer",
    page_icon="⚖️",
    layout="centered"
)

# Custom CSS for clean design
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .subheader {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .disclaimer-box {
        background-color: #fff3cd;
        border-left: 4px solid #ffc107;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 4px;
    }
    .explanation-box {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-header">⚖️ Navo</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subheader">Understand Your Legal Situation in Plain English</div>', 
    unsafe_allow_html=True
)

# Important disclaimer at top
st.markdown("""
<div class="disclaimer-box">
    <strong>⚠️ Important:</strong> Navo does NOT provide legal advice. 
    It only explains situations in general terms to help you understand 
    what might be involved. Always consult a qualified attorney for advice 
    on your specific situation.
</div>
""", unsafe_allow_html=True)

# Main interface
st.markdown("### Describe What Happened")
st.markdown("Tell Navo about your situation in your own words. Be as detailed as you'd like.")

# Text input
user_situation = st.text_area(
    label="Your situation:",
    placeholder="Example: I got pulled over for speeding and the officer asked to search my car. I said no, but he searched it anyway and found something that wasn't mine...",
    height=200,
    label_visibility="collapsed"
)

# Analyze button
if st.button("🔍 Explain This Situation", type="primary", use_container_width=True):
    if not user_situation.strip():
        st.warning("Please describe your situation first.")
    else:
        with st.spinner("Analyzing your situation..."):
            try:
                explainer = NavoExplainer()
                explanation = explainer.explain_situation(user_situation)
                
                # Display explanation
                st.markdown("### Your Explanation")
                st.markdown(f'<div class="explanation-box">{explanation}</div>', 
                           unsafe_allow_html=True)
                
                # Bottom disclaimer
                st.markdown("""
                <div class="disclaimer-box">
                    <strong>Next Steps:</strong> This explanation is for educational purposes only. 
                    For advice on your specific situation, please consult with a licensed attorney 
                    in your jurisdiction.
                </div>
                """, unsafe_allow_html=True)
                
            except Exception as e:
                st.error(f"Error: {str(e)}")
                st.info("Make sure your ANTHROPIC_API_KEY is set in your .env file")

# Sidebar with info
with st.sidebar:
    st.markdown("## About Navo")
    st.markdown("""
    Navo helps people understand confusing legal situations by:
    
    - ✅ Explaining in plain English
    - ✅ Showing common factors
    - ✅ Listing questions to ask counsel
    - ❌ NOT giving legal advice
    - ❌ NOT telling you what to do
    - ❌ NOT predicting outcomes
    
    **Built for access to justice.**
    """)
    
    st.markdown("---")
    
    st.markdown("### Example Situations")
    st.markdown("""
    - Traffic stops
    - Eviction notices
    - Employment disputes
    - Contract confusion
    - Family law matters
    - Criminal charges
    """)
    
    st.markdown("---")
    st.markdown("**Remember:** Always consult a real attorney for legal advice.")
