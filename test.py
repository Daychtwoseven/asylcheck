from docx import Document
from docx.shared import Pt, Inches

document = Document()

p = document.add_paragraph("")
p.add_run("I.").bold = True
p.alignment = 1
document.add_paragraph("In außen näher bezeichneter Angelegenheit gibt der Beschwerdeführer bekannt, die Held Berdnik Astner & Partner Rechtsanwälte GmbH, Rooseveltplatz 10, 1090 Wien, mit seiner rechtsfreundlichen Vertretung im Säumnisbeschwerdeverfahren beauftragt und bevollmächtigt zu haben. Die außen angeführte Rechtsanwaltskanzlei beruft sich gemäß § 8 Abs 1 RAO iVm § 10 AVG auf die ihr erteilte Vollmacht.")

p = document.add_paragraph("")
p.add_run("II.").bold = True
p.size = Pt(4)
p.alignment = 1

document.add_paragraph("Infolge des Ablaufs der Entscheidungsfrist erhebt der Beschwerdeführer nachstehende")
p = document.add_paragraph("")
p.add_run("SÄUMNISBESCHWERDE").bold = True
p.alignment = 1
for run in p.runs:
    run.font.size = Pt(14)

document.add_paragraph("an das Bundesverwaltungsgericht und führt hierzu an:")

# Add the numbered list
numbered_list = [1, 2, 3, 4, 5]  # Example list of numbers
for number in numbered_list:
    if number == 1:
        list_paragraph = document.add_paragraph()
        list_paragraph.style = 'List Number'
        list_run = list_paragraph.add_run("Sachverhalt").bold = True
        p = document.add_paragraph("Am [Datum der Erstbefragung bzw Datum der Ausweisausstellung] hat der Beschwerdeführer seine Erstbefragung nach dem AsylG absolviert, spätestens mit diesem Zeitpunkt hat er daher eine Entscheidung über seinen Antrag auf Zuerkennung internationalen Schutzes nach dem AsylG beantragt.")
        p.paragraph_format.left_indent = Inches(0.5)

        p = document.add_paragraph(
            "Die Aufenthaltsberechtigungskarte gem § 51 AsylG wurde dem Beschwerdeführer ausgestellt, in den letzten [Zeitraum zwischen Säumnisbeschwerde und Erstbefragung] Monaten wurde aber keine Entscheidung getroffen. Auch andere behördliche Tätigkeit wodurch die massiven Verzögerungen zu erklären sind, waren nicht erkennbar für den Beschwerdeführer. ")
        p.paragraph_format.left_indent = Inches(0.5)

        p = document.add_paragraph("Beweis:	beizuschaffender BFA-Akt")
    elif number == 2:
        list_paragraph = document.add_paragraph()
        list_paragraph.style = 'List Number'
        list_run = list_paragraph.add_run("Rechtliche Überlegungen").bold = True

        p = document.add_paragraph("Gemäß Art. 130 Abs. 1 Z 3 B-VG erkennen die Verwaltungsgerichte über Beschwerden wegen Verletzung der Entscheidungspflicht durch eine Verwaltungsbehörde.")
        p.paragraph_format.left_indent = Inches(0.5)

        p = document.add_paragraph(
            "Gemäß Art. 131 Abs. 2 B-VG erkennt das BVwG über Beschwerden gemäß Art. 130 Abs. 1 in Rechtssachen in den Angelegenheiten der Vollziehung des Bundes, die unmittelbar von Bundesbehörden besorgt werden.")
        p.paragraph_format.left_indent = Inches(0.5)

        p = document.add_paragraph(
            "GGemäß § 7 Abs. 1 Z 4 BFA-VG entscheidet das Bundesverwaltungsgericht über Beschwerden wegen Verletzung der Entscheidungspflicht des Bundesamtes für Fremdenwesen und Asyl.")
        p.paragraph_format.left_indent = Inches(0.5)

        p = document.add_paragraph(
            "Gemäß § 8 Abs. 1 VwGVG kann Beschwerde wegen Verletzung der Entscheidungspflicht gemäß Art. 130 Abs. 1 Z 3 B-VG (Säumnisbeschwerde) erst erhoben werden, wenn die Behörde die Sache nicht innerhalb von sechs Monaten, wenn gesetzlich eine kürzere oder längere Entscheidungsfrist vorgesehen ist, innerhalb dieser entschieden hat. Die Frist beginnt mit dem Zeitpunkt, in dem der Antrag auf Sachentscheidung bei der Stelle eingelangt ist, bei der er einzubringen war. Die Beschwerde ist abzuweisen, wenn die Verzögerung nicht auf ein überwiegendes Verschulden der Behörde zurückzuführen ist.")
        p.paragraph_format.left_indent = Inches(0.5)

        p = document.add_paragraph(
            "Gemäß § 9 Abs. 1 VwGVG hat eine Beschwerde zu enthalten:")
        p.paragraph_format.left_indent = Inches(0.5)


        p = document.add_paragraph(
            "1. die Bezeichnung des angefochtenen Bescheides, der angefochtenen Ausübung unmittelbarer verwaltungsbehördlicher Befehls- und Zwangsgewalt oder der angefochtenen Weisung,")
        p.paragraph_format.left_indent = Inches(0.5)

        p = document.add_paragraph(
            "2. die Bezeichnung der belangten Behörde,")
        p.paragraph_format.left_indent = Inches(0.5)

        p = document.add_paragraph(
            "3. die Gründe, auf die sich die Behauptung der Rechtswidrigkeit stützt,")
        p.paragraph_format.left_indent = Inches(0.5)

        p = document.add_paragraph(
            "4. das Begehren und")
        p.paragraph_format.left_indent = Inches(0.5)

        p = document.add_paragraph(
            "5. die Angaben, die erforderlich sind, um zu beurteilen, ob die Beschwerde rechtzeitig eingebracht ist.")
        p.paragraph_format.left_indent = Inches(0.5)

        p = document.add_paragraph(
            "Gemäß Abs. 2 Z. 3 ist belangte Behörde in den Fällen des Art. 130 Abs. 1 Z 3 B-VG jene Behörde, die den Bescheid nicht erlassen hat.")
        p.paragraph_format.left_indent = Inches(0.5)

        p = document.add_paragraph(
            "Gemäß Abs. 5 entfallen bei Beschwerden wegen Verletzung der Entscheidungspflicht gemäß Art. 130 Abs. 1 Z 3 B-VG die Angaben nach Abs. 1 Z 1 bis 3 und 5. Als belangte Behörde ist die Behörde zu bezeichnen, deren Entscheidung in der Rechtssache begehrt wurde. Ferner ist glaubhaft zu machen, dass die Frist zur Erhebung der Säumnisbeschwerde gemäß § 8 Abs. 1 abgelaufen ist.")
        p.paragraph_format.left_indent = Inches(0.5)

    elif number == 3:
        list_paragraph = document.add_paragraph()
        list_paragraph.style = 'List Number'
        list_run = list_paragraph.add_run("Antrag").bold = True

        p = document.add_paragraph(
            "Der Beschwerdeführer stellt daher den")
        p.paragraph_format.left_indent = Inches(0.5)

        p = document.add_paragraph("")
        p.add_run("ANTRAG").bold = True
        p.alignment = 1
        for run in p.runs:
            run.font.size = Pt(14)

        p = document.add_paragraph(
            "Das Bundesverwaltungsgericht möge,")
        p.paragraph_format.left_indent = Inches(0.5)

        list_items = [1, 2]  # Example list items
        # Add the list items
        for item in list_items:
            if item == 1:
                inside_list_paragraph = document.add_paragraph()
                inside_list_paragraph.paragraph_format.left_indent = Inches(1.3)
                inside_list_paragraph.style = 'List Bullet'
                list_run = inside_list_paragraph.add_run("der Säumnisbeschwerde stattgeben, die Verletzung der "
                                                         "Entscheidungspflicht von Seiten des Bundesamts für "
                                                         "Fremdenwesen und Asyl feststellen und gemäß § 28 Abs 7 1. "
                                                         "Fall VwGVG in der Sache selbst zu entscheiden; in eventu. \n")

            elif item == 2:
                inside_list_paragraph = document.add_paragraph()
                inside_list_paragraph.paragraph_format.left_indent = Inches(1.3)
                inside_list_paragraph.style = 'List Bullet'
                list_run = inside_list_paragraph.add_run("der Säumnisbeschwerde stattgeben, die Verletzung der "
                                                         "Entscheidungspflicht von Seiten des Bundesamts für "
                                                         "Fremdenwesen und Asyl feststellen und der säumigen Behörde "
                                                         "gemäß § 28 Abs 7 2. Fall VwGVG aufzutragen, den versäumten "
                                                         "Bescheid binnen 8 Wochen zu erlassen.")

p = document.add_paragraph("[Vorname Nachname]")
p.alignment = 2

# Specify the desired paper size
paper_width = 8.5  # Width in inches
paper_height = 11  # Height in inches

# Access the section properties
for section in document.sections:
    # Change the paper size
    section.page_width = Pt(paper_width * 72)
    section.page_height = Pt(paper_height * 72)
document.save("test.docx")