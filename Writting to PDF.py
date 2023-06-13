from reportlab.pdfgen import canvas

#Create a new pdf canvas object
with open("my_doc.pdf", "wb") as f:
    pdf = canvas.Canvas(f)

    # Add some text to the PDF
    # Note the numbers stand for indentation and must come before text.

    pdf.drawString(350, 750, "This is some text.")

    # Save the PSF
    pdf.save()



