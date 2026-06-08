import os
import uuid
import streamlit as st

from langchain_core.messages import HumanMessage

from graph.graph import graph

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Agentic AI Research Assistant",
    page_icon="🤖",
    layout="wide"
)

# ==================================================
# SESSION STATE
# ==================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "thread_id" not in st.session_state:
    st.session_state.thread_id = str(uuid.uuid4())

if "pdf_ingested" not in st.session_state:
    st.session_state.pdf_ingested = False

if "uploaded_filename" not in st.session_state:
    st.session_state.uploaded_filename = None

# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.title("🤖 Agentic AI")

    st.markdown("""
    Multi-Agent Research Assistant

    Powered By:
    - LangGraph
    - LangChain
    - Groq
    - Tavily
    - ChromaDB
    - RAG
    """)

    st.divider()

    uploaded_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    # ==========================================
    # PDF INGESTION
    # ==========================================

    if uploaded_file:

        current_filename = uploaded_file.name

        if (
            not st.session_state.pdf_ingested
            or st.session_state.uploaded_filename != current_filename
        ):

            os.makedirs(
                "uploads",
                exist_ok=True
            )

            file_path = os.path.join(
                "uploads",
                current_filename
            )

            with open(file_path, "wb") as f:
                f.write(
                    uploaded_file.getbuffer()
                )

            try:

                from rag.ingest import ingest_pdf

                with st.spinner(
                    "Indexing PDF..."
                ):

                    chunks = ingest_pdf(
                        file_path
                    )

                st.session_state.pdf_ingested = True

                st.session_state.uploaded_filename = (
                    current_filename
                )

                st.success(
                    f"PDF Indexed Successfully ({chunks} chunks)"
                )

            except Exception as e:

                st.error(
                    f"PDF Ingestion Failed:\n{str(e)}"
                )

    if st.session_state.pdf_ingested:

        st.success(
            f"Loaded: {st.session_state.uploaded_filename}"
        )

    st.divider()

    # ==========================================
    # CLEAR CHAT
    # ==========================================

    if st.button(
        "🗑️ Clear Chat",
        use_container_width=True
    ):

        st.session_state.messages = []

        st.session_state.thread_id = (
            str(uuid.uuid4())
        )

        st.rerun()

# ==================================================
# HEADER
# ==================================================

st.title(
    "🤖 Agentic AI Research Assistant"
)

st.caption(
    "Web Search + RAG + Multi-Agent Workflow"
)

# ==================================================
# CHAT HISTORY
# ==================================================

for msg in st.session_state.messages:

    with st.chat_message(
        msg["role"]
    ):
        st.markdown(
            msg["content"]
        )

# ==================================================
# CHAT INPUT
# ==================================================

query = st.chat_input(
    "Ask anything..."
)

# ==================================================
# USER QUERY
# ==================================================

if query:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )

    with st.chat_message(
        "user"
    ):
        st.markdown(query)

    with st.chat_message(
        "assistant"
    ):

        placeholder = st.empty()

        try:

            with st.spinner(
                "Thinking..."
            ):

                result = graph.invoke(
                    {
                        "query": query,
                        "messages": [
                            HumanMessage(
                                content=query
                            )
                        ]
                    },
                    config={
                        "configurable": {
                            "thread_id":
                            st.session_state.thread_id
                        }
                    }
                )

                answer = result.get(
                    "final_answer",
                    "No answer generated."
                )

                placeholder.markdown(
                    answer
                )

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer
                    }
                )

                # ==================================
                # SOURCES
                # ==================================

                sources = result.get(
                    "sources",
                    []
                )

                if sources:

                    with st.expander(
                        "📚 Sources"
                    ):

                        for source in sources:

                            st.write(
                                f"• {source}"
                            )

                # ==================================
                # DEBUG PANEL
                # ==================================

                with st.expander(
                    "⚙️ Workflow Details"
                ):

                    st.json(
                        result
                    )

        except Exception as e:

            error_message = (
                f"Error: {str(e)}"
            )

            placeholder.error(
                error_message
            )

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": error_message
                }
            )