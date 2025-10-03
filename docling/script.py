from docling.document_converter import DocumentConverter
import logging
import os

input_dir = "./rsc/"  # file path or URL
output_dir = "./out/"
filename = 'EN_intesa_san_paolo__2024_Annual_report.pdf'

in_path = input_dir + filename
out_path = output_dir + filename.replace('.pdf', '.md')

os.makedirs(output_dir, exist_ok=True)

converter = DocumentConverter()
doc = converter.convert(in_path).document

md_content = doc.export_to_markdown()

print(f"Writing markdown content into {out_path} ...")
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(md_content)