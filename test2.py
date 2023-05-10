from docx import Document
from docx.shared import Inches

# Open a new document
doc = Document()

# Add a table with one row and two cells
table = doc.add_table(rows=1, cols=2)
table.autofit = False

# Set the width of each column
column_width = Inches(3.5)
table.columns[0].width = column_width
table.columns[1].width = column_width

# Get the second column and change its width
first_column = table.columns[0]
first_column.width = Inches(6)  # Modify the width as desired

# Get the second column and change its width
second_column = table.columns[1]
second_column.width = Inches(2)  # Modify the width as desired


# Get the first row of the table
row = table.rows[0]

# Add content to the first column
left_cell = row.cells[0]
left_paragraph = left_cell.paragraphs[0]
left_paragraph.add_run("Bundesamt für Fremdenwesen und Asyl - Direktion")
left_paragraph.add_run("Modecenterstraße 22")
left_paragraph.add_run("1030 Wien")

# Add content to the second column
right_cell = row.cells[1]
right_paragraph = right_cell.paragraphs[0]
right_paragraph.add_run("Right column content")

# Save the document
doc.save('path_to_save_document.docx')
