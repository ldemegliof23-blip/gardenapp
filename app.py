import streamlit as st

import queries
from db import connect, reset

conn = connect()

st.title("Garden Beds")
st.write("Pick a page in the sidebar.")
st.dataframe(queries.beds(conn), hide_index=True)
st.dataframe(queries.status_counts(conn), hide_index=True)
st.caption(f"Logs with no bed: {queries.orphan_count(conn)}")

# RESET: throw away garden.db so the app builds a fresh one
if st.button("Reset garden"):
    conn.close()
    reset()
    st.rerun()
