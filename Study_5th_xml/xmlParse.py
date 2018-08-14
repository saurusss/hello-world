from xml.etree.ElementTree import parse
tree = parse("note.xml")
# tree = parse(r'C:\Users\Administrator\Documents\Github\hello-world\note.xml')
note = tree.getroot()