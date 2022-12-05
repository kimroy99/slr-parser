import streamlit as st
import pdf2image
import os
import fitz


# main function
def main():
    st.title("SLR Parser")
    st.subheader("Enter Grammer and Token")
    grammer = st.text_area("Enter Grammer", height=200)
    token = st.text_area("Enter Token", height=200)
    if st.button("Parse"):
        with open('test_grammer.txt', 'w') as f:
            f.write(grammer)
        bashCommand = f"python slr.py test_grammer.txt {token}"
        os.system(bashCommand)
        pdffile = "automaton.gv.pdf"
        doc = fitz.open(pdffile)
        page = doc.load_page(0) 
        pix = page.get_pixmap()
        output = "outfile.png"
        pix.save(output)
        st.image(output, use_column_width=True)

if __name__ == "__main__":
    main()


        

