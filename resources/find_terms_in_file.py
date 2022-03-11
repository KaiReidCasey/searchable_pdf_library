search_term_file = open("search_terms.csv", "r")
# https://pdfgrep.org/ may be helpful for searching the PDF
# https://soft.rubypdf.com/software/pdfgrep-windows-version
# may be a Windows version

# pdf_to_search = open("pdfs/searchable_pdf_000.pdf", "r")

search_terms = search_term_file.readlines()

print("\nThese are the names to search for:\n")
for term in search_terms:
	print(term.strip(", \n"))

search_term_file.close()
