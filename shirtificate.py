from fpdf import FPDF

class Shirtificate(FPDF):
    def header(self):
        # Set font for the header
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'CS50 Shirtificate', align='C', ln=True)

    def footer(self):

        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
    
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def create_shirtificate(name, output_filename):
    pdf = Shirtificate()
    pdf.add_page()
    pdf.set_font('Arial', size=16)
    pdf.image('shirtificate.png', x=50, y=30, w=110)
    pdf.ln(90)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 10, name, 0, 0, 'C')
    pdf.output(output_filename)

if __name__ == '__main__':
    name = input("Enter your name: ")
    output_filename = 'shirtificate.pdf'
    create_shirtificate(name, output_filename)
