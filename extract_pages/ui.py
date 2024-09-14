import streamlit as st

from extract_pages import extract_pdf
from page_range import PageRange
from page_single import PageSingle


# Function to manage the app's state
def show_transformation():
    # Initialize session state
    if "rows" not in st.session_state:
        st.session_state.rows = []

    st.title("Extract Pagess")
    st.write("This tool is to help to extract page from a given PDF")

    pdf_file_path = st.text_input("PDF File Path")

    # Button to add a new row
    l, r = st.columns(2)
    if l.button("Add Row"):
        st.session_state.rows.append(len(st.session_state.rows))

    if r.button("Extract") and pdf_file_path:
        pages = []

        for i in st.session_state.rows:
            selection = st.session_state[f"dropdown_{i}"]
            if "Single" == selection:
                page = st.session_state[f"single_{i}"]
                pages.append(PageSingle(single_page=page))
            else:
                from_page = st.session_state[f"from_{i}"]
                to_page = st.session_state[f"to_{i}"]
                pages.append(PageRange(from_page=from_page, to_page=to_page))

        with st.empty():
            st.write(f"Extracting now. Please wait")
            output_file_name = extract_pdf(pdf_file_path=pdf_file_path, pages=pages)
            st.write(f"Completed extract and created as {output_file_name}")

    # Display rows with drop-down and delete button
    if st.session_state.rows:
        for i in st.session_state.rows:
            cols = st.columns([3, 1])
            with cols[0]:
                selected = st.selectbox(
                    f"Row {i + 1}",
                    ["Single", "Range"],
                    key=f"dropdown_{i}",
                )
                if selected == "Range":
                    from_page, to_page = st.columns(2)
                    from_page.number_input("From", key=f"from_{i}", step=1)
                    to_page.number_input("To", key=f"to_{i}", step=1)

                elif selected == "Single":
                    st.number_input("Page", key=f"single_{i}", step=1)

            with cols[1]:
                if st.button(f"Delete Row {i + 1}", key=f"delete_{i}"):
                    st.session_state.rows.remove(i)
                    st.rerun()  # Refresh to update rows


if __name__ == "__main__":
    show_transformation()
