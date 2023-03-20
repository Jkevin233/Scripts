import pdftotext


with open("2023-03-18.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)

contents = pdf[10]

with open("result.txt", "w") as f:
    f.write(contents)
