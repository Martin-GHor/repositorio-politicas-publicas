import streamlit as st
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Exported Streamlit Responses', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

st.title('Streamlit to PDF Exporter')

# Sample responses that would typically come from Streamlit 
response_data = [
    {'question': 'What is your name?', 'response': 'Alice'},
    {'question': 'How old are you?', 'response': '30'},
    {'question': 'What is your favorite programming language?', 'response': 'Python'},
]

pdf = PDF()  
pdf.add_page()  

pdf.set_font('Arial', '', 12)
for item in response_data:
    pdf.cell(0, 10, f"{item['question']}: {item['response']}", ln=True)

# Save PDF to a file
pdf_file_name = 'exported_responses.pdf'
pdf.output(pdf_file_name)
st.success('PDF exported successfully!')

st.download_button('Download PDF', pdf_file_name)