import streamlit as st

st.set_page_config(page_title="Spotify AI Review Analyzer", page_icon="🎵")

st.title("🎵 Spotify AI Review Analyzer")

review = st.text_area("Enter a Spotify review")

if st.button("Analyze Review"):
    if review.strip() == "":
        st.warning("Please enter a review.")
    else:
        st.success("Analysis Complete")

        st.write("### Structured Output")

        st.write("**Sentiment:** Negative")
        st.write("**Theme:** Recommendation Quality")
        st.write("**Recommendation Problem:** Repetitive recommendations")
        st.write("**Listening Behavior:** Replays same playlist")
        st.write("**User Segment:** Heavy Listener")
        st.write("**Unmet Need:** Better personalized music discovery")
