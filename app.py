import streamlit as st
import re

# App Configuration
st.set_page_config(page_title="Advanced Text Analyzer", page_icon="📜", layout="wide")

# Custom CSS for Professional Styling
st.markdown("""
    <style>
    .main-title { font-size: 2.5em; color: #2c3e50; font-weight: bold; }
    .section-header { font-size: 1.5em; color: #34495e; }
    .metric-box { background-color: #ecf0f1; padding: 10px; border-radius: 5px; }
    .stButton>button { background-color: #3498db; color: white; border-radius: 5px; }
    .stButton>button:hover { background-color: #2980b9; }
    </style>
""", unsafe_allow_html=True)

# App Title
st.markdown('<div class="main-title">📜 Advanced Text Analyzer</div>', unsafe_allow_html=True)
st.write("Analyze your text with precision and ease. Built with Streamlit by [Your Name/Company].")

# Sidebar for Options
st.sidebar.header("⚙️ Settings")
analysis_mode = st.sidebar.selectbox("Analysis Mode", ["Basic", "Advanced"])
show_charts = st.sidebar.checkbox("Show Visualizations", value=False)

# User Input Section
st.markdown('<div class="section-header">📝 Input Your Text</div>', unsafe_allow_html=True)
text = st.text_area("Type or paste your text here:", height=150, placeholder="Enter a paragraph...")

# Analyze Button and Logic
if st.button("🔍 Analyze Text", key="analyze"):
    if not text.strip():
        st.error("⚠️ Please provide some text to analyze.")
    else:
        # Basic Analysis
        words = re.split(r'\s+', text.strip())  # More robust word splitting
        word_count = len(words)
        char_count = len(text)
        vowel_count = sum(1 for char in text if char.lower() in 'aeiou')
        sentence_count = len(re.split(r'[.!?]+', text.strip())) - 1 if text.strip() else 0
        avg_word_length = round(char_count / word_count, 2) if word_count else 0
        contains_python = "python" in text.lower()

        # Advanced Analysis (if selected)
        unique_words = len(set(words))
        longest_word = max(words, key=len, default="") if words else ""

        # Display Results
        st.markdown('<div class="section-header">📊 Analysis Results</div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)

        with col1:
            st.markdown('<div class="metric-box">', unsafe_allow_html=True)
            st.metric("Total Words", word_count)
            st.metric("Total Characters", char_count)
            st.metric("Vowel Count", vowel_count)
            st.metric("Sentence Count", sentence_count)
            st.markdown('</div>', unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="metric-box">', unsafe_allow_html=True)
            st.metric("Average Word Length", f"{avg_word_length} chars")
            st.write("**Python Mentioned:** ✅ Yes" if contains_python else "**Python Mentioned:** ❌ No")
            if analysis_mode == "Advanced":
                st.metric("Unique Words", unique_words)
                st.write(f"**Longest Word:** {longest_word}")
            st.markdown('</div>', unsafe_allow_html=True)

        # Visualizations (Optional)
        if show_charts:
            st.markdown('<div class="section-header">📈 Visual Insights</div>', unsafe_allow_html=True)
            chart_data = {
                "Metric": ["Words", "Characters", "Vowels", "Sentences"],
                "Count": [word_count, char_count, vowel_count, sentence_count]
            }
            st.bar_chart(chart_data, x="Metric", y="Count")

        # Case Conversions
        st.markdown('<div class="section-header">🔠 Case Conversions</div>', unsafe_allow_html=True)
        col3, col4 = st.columns(2)
        with col3:
            st.text_area("Uppercase", text.upper(), height=100)
        with col4:
            st.text_area("Lowercase", text.lower(), height=100)

# Search & Replace Section
st.markdown('<div class="section-header">🔍 Search & Replace</div>', unsafe_allow_html=True)
col5, col6 = st.columns(2)
with col5:
    search_word = st.text_input("Search for:", placeholder="e.g., hello")
with col6:
    replace_word = st.text_input("Replace with:", placeholder="e.g., hi")

if st.button("🔄 Replace Words", key="replace"):
    if not text.strip():
        st.error("⚠️ Please enter text to modify.")
    elif not search_word:
        st.warning("⚠️ Please enter a word to search for.")
    else:
        modified_text = text.replace(search_word, replace_word)
        st.markdown('<div class="section-header">📝 Modified Text</div>', unsafe_allow_html=True)
        st.text_area("Updated Text", modified_text, height=150)

# Footer
st.markdown("---")
st.write("© 2025 [Shahmeer khan]. Powered by Streamlit.")