# import streamlit as st
# from llama_index.core import VectorStoreIndex, Settings
# from llama_index.readers.file import PDFReader
# from llama_index.embeddings.langchain import LangchainEmbedding
# from langchain.embeddings import HuggingFaceEmbeddings
# from PIL import Image
# import os
# import pdfplumber

# def extract_text_pagewise(pdf_path):
#     page_texts = []
#     with pdfplumber.open(pdf_path) as pdf:
#         for page in pdf.pages:
#             text = page.extract_text()
#             page_texts.append(text if text else "")
#     return page_texts

# def get_image_name(name_base, image_folder):
#     for file in os.listdir(image_folder):
#         if file.startswith(name_base):
#             return os.path.join(image_folder, file)
#     return None

# # Set page config
# st.set_page_config(page_title="Aarogya Sparsha - Yoga Remedies", layout="wide")

# # Use a lightweight local model for embeddings
# embed_model=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2", model_kwargs={"device": "cpu"})
# Settings.embed_model = embed_model
# Settings.llm = None

# # Load Yoga book document from PDF
# try:
#     documents = PDFReader().load_data("data.pdf")
#     index = VectorStoreIndex.from_documents(documents) if documents else None
#     query_engine = index.as_query_engine() if index else None
# except Exception as e:
#     st.error(f"⚠️ Error loading PDF: {e}")
#     documents, index, query_engine = None, None, None

# # Sidebar Navigation
# st.sidebar.title("Navigation")

# # Custom title in bold and colorful
# st.sidebar.markdown(
#     """
#     <div style="text-align: center; font-size: 24px; font-weight: bold; color: #4CAF50;">
#         AAROGYA SPARSHA
#     </div>
#     """, 
#     unsafe_allow_html=True
# )

# if "page" not in st.session_state:
#     st.session_state.page = "Home"

# if st.sidebar.button("🏠 Home"):
#     st.session_state.page = "Home"
# if st.sidebar.button("✨ Benefits of Yoga"):
#     st.session_state.page = "Benefits of Yoga"
# if st.sidebar.button("🧘 Yoga Postures"):
#     st.session_state.page = "Yogas"
# if st.sidebar.button("💬 AI Chatbot"):
#     st.session_state.page = "AI Chatbot"
# if st.sidebar.button("🌟 Conclusion"):
#     st.session_state.page = "Conclusion"

# # Page Rendering
# if st.session_state.page == "Home":
#     st.title("🧘‍♂️ Introduction to Yoga")
#     st.write("""
#     Yoga is an ancient practice that unites the mind, body, and spirit through physical postures, breath control, and meditation. 
#     Practiced for over 5,000 years, yoga is deeply rooted in Indian traditions and philosophy. The word "yoga" is derived from the 
#     Sanskrit word "Yuj," meaning "to unite." 

#     This book will explore 19 essential yoga poses, their benefits, techniques, and disease remedies to guide you toward a healthier lifestyle.
#     """)

# elif st.session_state.page == "Benefits of Yoga":
#     st.title("✨ Benefits of Yoga")
#     st.write("""
#     **Physical Benefits:**
#     - Increases flexibility and strength
#     - Improves posture and balance
#     - Enhances cardiovascular and respiratory health

#     **Mental Benefits:**
#     - Reduces stress and anxiety
#     - Improves focus and concentration
#     - Enhances mood and emotional stability

#     **Spiritual Benefits:**
#     - Encourages self-awareness and inner peace
#     - Enhances the connection between mind and body
#     """)

# elif st.session_state.page == "Yogas":
#     st.title("🧘‍♂️ Yoga Postures")
#     st.write("Here are some effective Yoga postures dynamically retrieved from the book.")
#     pdf_path = r"C:\\Users\\abhij\\AAROGYA-SPARSHA\\data.pdf"
#     image_folder = r"C:\\Users\\abhij\\AAROGYA-SPARSHA\\images"
#     pages = extract_text_pagewise(pdf_path)

#     for idx, content in enumerate(pages):
#         if 5 <= idx + 1 <= 19:
#             content_to_add = content[8:] if content and len(content) > 8 else content
#             content_to_add = "\n" + "-" * 10 + "\n" + content_to_add
#             content_to_add = content_to_add.replace("Benefits", "\nBenefits")
#             content_to_add = content_to_add.replace("Steps", "\nSteps")
#             content_to_add = content_to_add.replace("Disease Remedy", "\nDisease Remedy")
#             content_to_add = content_to_add.replace("\u2022", "\n\u2022")

#             st.write(content_to_add)

#             # Extract yoga name from the heading (before the first bracket)
#             heading_line = content.split("\n")[0]
#             name = heading_line.split(")")[0].strip()[8:]
#             name = name + ")".strip()
#             if name[0] == " ":
#                 name = name[1:]
#             image_path = os.path.join(image_folder, name + ".jpg")

#             if image_path:
#                 st.image(image_path, caption=name, use_container_width=True)

# elif st.session_state.page == "AI Chatbot":
#     st.title("💬 AI Chatbot for Yoga Remedies")
#     st.write("Ask any question about yoga remedies, postures, or health benefits!")
#     user_query = st.text_input("Type your question here:")

#     if user_query:
#         if query_engine:
#             try:
#                 query_engine = index.as_query_engine(similarity_top_k=1, response_mode="compact")
#                 response = query_engine.query("Give Information about " + user_query)
#                 if response and response.response:
#                     st.write("### 🍵 Answer:")
#                     st.write(response.response)
#                     st.info("➡️ Explore the **Yoga Postures** section for more related details!")
#                 else:
#                     st.warning("⚠️ No relevant answer found. Try rephrasing your query.")
#             except Exception as e:
#                 st.error(f"⚠️ Chatbot error: {e}")
#         else:
#             matched_text = [doc.text for doc in documents if user_query.lower() in doc.text.lower()]
#             if matched_text:
#                 st.write("### 🔍 Found in Document:")
#                 for text in matched_text[:3]:
#                     st.write(f"- {text[:200]}...")
#             else:
#                 st.warning("⚠️ No relevant answer found. Try rephrasing your query.")

# elif st.session_state.page == "Conclusion":
#     st.title("🌟 Conclusion")
#     st.write("""
#     Yoga is more than just exercise; it is a holistic approach to well-being that harmonizes the mind, body, and spirit. 
#     Consistent practice can lead to profound improvements in your physical health, mental clarity, and spiritual growth.

#     Start your journey today towards a balanced and healthier life with yoga!
#     """)




import streamlit as st
from llama_index.core import VectorStoreIndex, Settings
from llama_index.readers.file import PDFReader
from llama_index.embeddings.langchain import LangchainEmbedding
from langchain.embeddings import HuggingFaceEmbeddings
from PIL import Image
import os
import pdfplumber

def extract_text_pagewise(pdf_path):
    page_texts = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            page_texts.append(text if text else "")
    return page_texts

def get_image_name(name_base, image_folder):
    for file in os.listdir(image_folder):
        if file.startswith(name_base):
            return os.path.join(image_folder, file)
    return None

# Set page config
st.set_page_config(page_title="Aarogya Sparsha - Yoga Remedies", layout="wide")

# Use a lightweight local model for embeddings
embed_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2", model_kwargs={"device": "cpu"})
Settings.embed_model = embed_model
Settings.llm = None

# Load Yoga book document from PDF
try:
    documents = PDFReader().load_data("data.pdf")
    index = VectorStoreIndex.from_documents(documents) if documents else None
    query_engine = index.as_query_engine() if index else None
except Exception as e:
    st.error(f"⚠️ Error loading PDF: {e}")
    documents, index, query_engine = None, None, None

# Sidebar Navigation with Custom Title
st.sidebar.title("Navigation")

# Custom title in bold, large font, and green color at the top of the sidebar
st.sidebar.markdown(
    """
    <div style="text-align: center; font-size: 30px; font-weight: bold; color: #4CAF50;">
        AAROGYA SPARSHA
    </div>
    """, 
    unsafe_allow_html=True
)

if "page" not in st.session_state:
    st.session_state.page = "Home"

if st.sidebar.button("🏠 Home"):
    st.session_state.page = "Home"
if st.sidebar.button("✨ Benefits of Yoga"):
    st.session_state.page = "Benefits of Yoga"
if st.sidebar.button("🧘 Yoga Postures"):
    st.session_state.page = "Yogas"
if st.sidebar.button("💬 AI Chatbot"):
    st.session_state.page = "AI Chatbot"
if st.sidebar.button("🌟 Conclusion"):
    st.session_state.page = "Conclusion"

# Page Rendering
if st.session_state.page == "Home":
    # Top Half: Image
    st.image(r"C:\Users\abhij\AAROGYA-SPARSHA\AAROGYA-SPARSHA.jpg", use_column_width=True, caption="Discover the Essence of Yoga")

    # Bottom Half: Introduction
    st.title("🧘‍♂️ Introduction to Yoga")
    st.write("""
    Yoga is an ancient practice that unites the mind, body, and spirit through physical postures, breath control, and meditation. 
    Practiced for over 5,000 years, yoga is deeply rooted in Indian traditions and philosophy. The word "yoga" is derived from the 
    Sanskrit word "Yuj," meaning "to unite." 

    This book will explore 19 essential yoga poses, their benefits, techniques, and disease remedies to guide you toward a healthier lifestyle.
    """)

elif st.session_state.page == "Benefits of Yoga":
    st.title("✨ Benefits of Yoga")
    st.write("""
    **Physical Benefits:**
    - Increases flexibility and strength
    - Improves posture and balance
    - Enhances cardiovascular and respiratory health

    **Mental Benefits:**
    - Reduces stress and anxiety
    - Improves focus and concentration
    - Enhances mood and emotional stability

    **Spiritual Benefits:**
    - Encourages self-awareness and inner peace
    - Enhances the connection between mind and body
    """)

elif st.session_state.page == "Yogas":
    st.title("🧘‍♂️ Yoga Postures")
    st.write("Here are some effective Yoga postures dynamically retrieved from the book.")
    pdf_path = r"C:\\Users\\abhij\\AAROGYA-SPARSHA\\data.pdf"
    image_folder = r"C:\Users\abhij\AAROGYA-SPARSHA\images"
    pages = extract_text_pagewise(pdf_path)

    for idx, content in enumerate(pages):
        if 5 <= idx + 1 <= 19:
            content_to_add = content[8:] if content and len(content) > 8 else content
            content_to_add = "\n" + "-" * 10 + "\n" + content_to_add
            content_to_add = content_to_add.replace("Benefits", "\nBenefits")
            content_to_add = content_to_add.replace("Steps", "\nSteps")
            content_to_add = content_to_add.replace("Disease Remedy", "\nDisease Remedy")
            content_to_add = content_to_add.replace("\u2022", "\n\u2022")

            st.write(content_to_add)

            heading_line = content.split("\n")[0]
            name = heading_line.split(")")[0].strip()[8:]
            name = name + ")"
            if name[0] == " ":
                name = name[1:]
            image_path = os.path.join(image_folder, name + ".jpg")

            if os.path.exists(image_path):
                st.image(image_path, caption=name, use_container_width=False)

elif st.session_state.page == "AI Chatbot":
    st.title("💬 AI Chatbot for Yoga Session")
    st.write("Ask any question about Yoga and its details!")
    user_query = st.text_input("Type your question here:")

    if user_query:
        if query_engine:
            try:
                query_engine = index.as_query_engine(similarity_top_k=1, response_mode="compact")
                response = query_engine.query("Give Information about " + user_query)
                if response and response.response:
                    st.write("### 🍵 Answer:")
                    st.write(response.response)
                    st.info("➡️ Explore the **Yoga Postures** section for more related details!")
                else:
                    st.warning("⚠️ No relevant answer found. Try rephrasing your query.")
            except Exception as e:
                st.error(f"⚠️ Chatbot error: {e}")
        else:
            matched_text = [doc.text for doc in documents if user_query.lower() in doc.text.lower()]
            if matched_text:
                st.write("### 🔍 Found in Document:")
                for text in matched_text[:3]:
                    st.write(f"- {text[:200]}...")
            else:
                st.warning("⚠️ No relevant answer found. Try rephrasing your query.")

elif st.session_state.page == "Conclusion":
    st.title("🌟 Conclusion")
    st.write("""
    Yoga is more than just exercise; it is a holistic approach to well-being that harmonizes the mind, body, and spirit. 
    Consistent practice can lead to profound improvements in your physical health, mental clarity, and spiritual growth .

    Start your journey today towards a balanced and healthier life with yoga!
    """)
