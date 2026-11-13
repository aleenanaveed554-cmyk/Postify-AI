import streamlit as st
from groq import Groq
from PIL import Image
import base64
import json

st.set_page_config(
    page_title="Postify AI",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------
# PREMIUM BLACK + GOLD THEME
# -----------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');

:root {
    --gold: #D9A441;
    --gold-light: #F6D98B;
    --gold-dark: #9B6A16;
    --black: #050505;
    --panel: #0D0D0D;
    --panel-2: #121212;
    --white: #F7F4EE;
    --muted: #B8B2A8;
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 80% 10%, rgba(217,164,65,.10), transparent 28%),
        radial-gradient(circle at 10% 90%, rgba(217,164,65,.07), transparent 28%),
        #050505;
    color: var(--white);
}

[data-testid="stHeader"] {
    background: transparent;
}

[data-testid="stSidebar"] {
    background:
        linear-gradient(180deg, #070707 0%, #0B0B0B 55%, #050505 100%);
    border-right: 1px solid rgba(217,164,65,.35);
}

[data-testid="stSidebar"] * {
    color: var(--white);
}

.block-container {
    max-width: 1500px;
    padding-top: 1.5rem;
    padding-bottom: 2rem;
}

.hero {
    text-align: center;
    padding: 12px 10px 24px;
}

.logo {
    font-family: 'Playfair Display', serif;
    font-size: clamp(3rem, 7vw, 5.8rem);
    line-height: 1;
    font-weight: 700;
    color: var(--gold-light);
    text-shadow: 0 0 28px rgba(217,164,65,.22);
    letter-spacing: -2px;
}

.tagline {
    margin-top: 10px;
    font-size: clamp(1.2rem, 2vw, 1.8rem);
    font-weight: 600;
    color: #F5F2EC;
}

.subtitle {
    margin-top: 8px;
    color: var(--muted);
    font-size: 1rem;
}

.badge {
    display: inline-block;
    margin-top: 16px;
    padding: 8px 16px;
    border: 1px solid rgba(217,164,65,.7);
    border-radius: 999px;
    color: var(--gold-light);
    background: rgba(217,164,65,.07);
    font-size: .85rem;
}

.section-title {
    font-family: 'Playfair Display', serif;
    color: var(--gold-light);
    font-size: 1.65rem;
    font-weight: 700;
    margin: 8px 0 14px;
}

.card {
    background: linear-gradient(145deg, rgba(20,20,20,.96), rgba(8,8,8,.98));
    border: 1px solid rgba(217,164,65,.38);
    border-radius: 22px;
    padding: 22px;
    box-shadow: 0 18px 55px rgba(0,0,0,.30), inset 0 0 24px rgba(217,164,65,.025);
    margin-bottom: 18px;
}

.mini-card {
    background: #0D0D0D;
    border: 1px solid rgba(217,164,65,.34);
    border-radius: 16px;
    padding: 18px;
    margin: 10px 0;
}

.mini-title {
    color: var(--gold-light);
    font-size: 1.05rem;
    font-weight: 700;
    margin-bottom: 8px;
}

.result {
    color: #F6F2EA;
    font-size: 1rem;
    line-height: 1.65;
    white-space: pre-wrap;
}

.feature {
    text-align: center;
    padding: 12px 5px;
    color: #E8E2D7;
}

.feature-icon {
    font-size: 1.35rem;
    color: var(--gold-light);
}

.feature-title {
    color: var(--gold-light);
    font-weight: 700;
    margin-top: 5px;
}

.feature-text {
    color: var(--muted);
    font-size: .85rem;
}

.stButton > button {
    background: linear-gradient(135deg, #F5D27F, #C28A25);
    color: #090909 !important;
    border: 1px solid #F1CC73;
    border-radius: 13px;
    min-height: 48px;
    font-weight: 800;
    box-shadow: 0 8px 28px rgba(217,164,65,.18);
    transition: .2s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 35px rgba(217,164,65,.30);
}

div[data-testid="stTextInput"] input,
div[data-testid="stSelectbox"] div,
div[data-testid="stTextArea"] textarea {
    background: #101010 !important;
    color: #F7F4EE !important;
    border-color: rgba(217,164,65,.45) !important;
    border-radius: 12px !important;
}

label {
    color: #E9E3D8 !important;
    font-weight: 600 !important;
}

[data-testid="stFileUploader"] {
    background: #0C0C0C;
    border: 1px dashed rgba(217,164,65,.55);
    border-radius: 15px;
    padding: 8px;
}

div[data-testid="stAlert"] {
    border-radius: 12px;
}

.footer {
    margin-top: 26px;
    padding: 18px 8px;
    border-top: 1px solid rgba(217,164,65,.25);
}

.sidebar-brand {
    text-align: center;
    padding: 10px 4px 24px;
}

.sidebar-brand .name {
    font-family: 'Playfair Display', serif;
    color: var(--gold-light);
    font-size: 2rem;
    font-weight: 700;
}

.sidebar-brand .small {
    color: var(--muted);
    font-size: .82rem;
}

.sidebar-promo {
    margin-top: 25px;
    padding: 18px 14px;
    border: 1px solid rgba(217,164,65,.35);
    border-radius: 16px;
    background: linear-gradient(145deg, rgba(217,164,65,.10), rgba(0,0,0,.15));
}

.sidebar-promo-title {
    color: var(--gold-light);
    font-weight: 700;
    line-height: 1.4;
}

.sidebar-promo-text {
    color: var(--muted);
    font-size: .82rem;
    margin-top: 7px;
}

@media (max-width: 900px) {
    .logo { font-size: 3.3rem; }
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# SIDEBAR
# -----------------------------
with st.sidebar:
    st.markdown("""
    <div class="sidebar-brand">
        <div style="font-size:2rem;">♛</div>
        <div class="name">Postify AI</div>
        <div class="small">Create • Inspire • Share</div>
    </div>
    """, unsafe_allow_html=True)

    page = st.radio(
        "Navigation",
        ["🏠 Home", "ℹ️ About", "📖 How It Works", "⭐ Features"],
        label_visibility="collapsed",
    )

    st.markdown("""
    <div class="sidebar-promo">
        <div class="sidebar-promo-title">Turn Your Ideas Into Stunning Social Media Content</div>
        <div class="sidebar-promo-text">Create polished captions, headlines, hashtags and CTAs in seconds.</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("**Instagram　 Facebook　 TikTok**")

# -----------------------------
# HERO
# -----------------------------
st.markdown("""
<div class="hero">
    <div class="logo">Postify AI</div>
    <div class="tagline">Smart Social Media Content Studio</div>
    <div class="subtitle">Create Professional Posts, Captions &amp; Hashtags with AI</div>
    <div class="badge">✨ Powered by Groq AI</div>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# ABOUT / HOW IT WORKS / FEATURES
# -----------------------------
if page != "🏠 Home":
    if page == "ℹ️ About":
        st.markdown('<div class="card"><div class="section-title">About Postify AI</div><div class="result">Postify AI is a premium social media content assistant designed to turn a simple idea, business topic, or poster into ready-to-use social media copy.</div></div>', unsafe_allow_html=True)
    elif page == "📖 How It Works":
        st.markdown('<div class="card"><div class="section-title">How It Works</div><div class="result">1. Upload an optional image.<br>2. Enter your topic or business.<br>3. Select a platform and content style.<br>4. Click Generate Content.<br>5. Copy your headline, caption, hashtags and CTA.</div></div>', unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="card">
            <div class="section-title">Features</div>
            <div class="result">
            ✨ AI Caption Generator<br>
            👑 Professional Headline Generator<br>
            #️⃣ Smart Hashtag Generator<br>
            📣 Call-to-Action Generator<br>
            🖼️ Optional Image Understanding<br>
            📱 Instagram, Facebook & TikTok support<br>
            🖤 Premium Black & Gold interface
            </div>
        </div>
        """, unsafe_allow_html=True)
    st.stop()

# -----------------------------
# MAIN WORKSPACE
# -----------------------------
left, right = st.columns([1, 1.08], gap="large")

with left:
    st.markdown('<div class="section-title">✨ Create Your Content</div>', unsafe_allow_html=True)
    st.markdown('<div class="card">', unsafe_allow_html=True)

    uploaded = st.file_uploader(
        "Upload Image (Optional)",
        type=["jpg", "jpeg", "png", "webp"],
        help="Upload a poster or product/event image if you want the AI to consider it."
    )

    if uploaded:
        image = Image.open(uploaded)
        st.image(image, caption="Uploaded image", use_container_width=True)

    topic = st.text_input(
        "Enter Your Topic / Business",
        placeholder="e.g. Birthday Sale, Fashion Brand, Restaurant, Wedding Event"
    )

    platform = st.selectbox(
        "Select Platform",
        ["Instagram", "Facebook", "TikTok"]
    )

    style = st.selectbox(
        "Content Style",
        ["Professional", "Luxury", "Creative", "Minimal", "Friendly", "Promotional", "Elegant"]
    )

    generate = st.button("✨ Generate Content →", use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="section-title">⭐ Your Generated Content</div>', unsafe_allow_html=True)

    if generate:
        if not topic.strip() and not uploaded:
            st.warning("Please enter a topic/business or upload an image.")
        else:
            try:
                api_key = st.secrets["GROQ_API_KEY"]
                client = Groq(api_key=api_key)

                system_prompt = """You are Postify AI, a professional social media copywriter.
Return ONLY valid JSON with exactly these keys:
headline, caption, hashtags, call_to_action.
Do not use markdown fences.
Create concise, polished, platform-appropriate content.
Respect the selected style.
Hashtags must be a single space-separated string.
"""

                user_text = f"""
Create social media content for:
Topic/Business: {topic.strip() or "Infer from the uploaded image"}
Platform: {platform}
Style: {style}

Requirements:
- Headline: short and memorable
- Caption: engaging, professional and natural
- Hashtags: 5 to 10 relevant hashtags
- Call to Action: short and persuasive
"""

                if uploaded:
                    image_bytes = uploaded.getvalue()
                    encoded = base64.b64encode(image_bytes).decode("utf-8")
                    mime = uploaded.type or "image/png"

                    content = [
                        {"type": "text", "text": user_text},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:{mime};base64,{encoded}"
                            },
                        },
                    ]
                else:
                    content = user_text

                response = client.chat.completions.create(
                    model="qwen/qwen3.8-27b",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": content},
                    ],
                    temperature=0.7,
                    max_completion_tokens=750,
                    response_format={"type": "json_object"},
                )

                raw = response.choices[0].message.content
                data = json.loads(raw)

                headline = data.get("headline", "")
                caption = data.get("caption", "")
                hashtags = data.get("hashtags", "")
                cta = data.get("call_to_action", "")

                st.session_state["postify_result"] = {
                    "headline": headline,
                    "caption": caption,
                    "hashtags": hashtags,
                    "cta": cta,
                }

            except KeyError:
                st.error("GROQ_API_KEY is missing. Add it to Streamlit Secrets.")
            except json.JSONDecodeError:
                st.error("The AI returned an unexpected format. Please try again.")
            except Exception as e:
                st.error(f"Something went wrong: {e}")

    result = st.session_state.get("postify_result")

    if result:
        for title, icon, value, key in [
            ("Caption", "🖼️", result["caption"], "caption"),
            ("Headline / Title", "♛", result["headline"], "headline"),
            ("Hashtags", "#", result["hashtags"], "hashtags"),
            ("Call to Action", "📣", result["cta"], "cta"),
        ]:
            st.markdown(
                f'<div class="mini-card"><div class="mini-title">{icon} {title}</div><div class="result">{value}</div></div>',
                unsafe_allow_html=True
            )
            st.code(value, language=None)

        if st.button("↻ Generate New Content", use_container_width=True):
            st.session_state.pop("postify_result", None)
            st.rerun()
    else:
        st.markdown("""
        <div class="card">
            <div class="result" style="text-align:center; padding:55px 10px;">
                Your AI-generated headline, caption, hashtags and CTA will appear here.
                <br><br>
                <span style="color:#D9A441;">✨ Ready when you are.</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("""
<div class="footer">
<div class="card" style="margin-bottom:0;">
<div class="feature">
<div class="feature-icon">⚡</div>
<div class="feature-title">AI-Powered with Groq</div>
<div class="feature-text">Fast content generation</div>
</div>
<div class="feature">
<div class="feature-icon">💎</div>
<div class="feature-title">Premium Design</div>
<div class="feature-text">Luxury black & gold UI</div>
</div>
<div class="feature">
<div class="feature-icon">🛡️</div>
<div class="feature-title">Secure & Reliable</div>
<div class="feature-text">API key stays in secrets</div>
</div>
<div class="feature">
<div class="feature-icon">🚀</div>
<div class="feature-title">Social Ready</div>
<div class="feature-text">Instagram • Facebook • TikTok</div>
</div>
</div>
</div>
""", unsafe_allow_html=True)
