from docling.document_converter import DocumentConverter
import os
import sys
import subprocess
from datetime import datetime

def run_with_full_logging():
    input_dir = "./rsc/"
    output_dir = "./out/"
    logs_dir = "./logs/"
    filename = 'EN_enel__integrated-annual-report_2024.pdf'
    
    in_path = input_dir + filename
    out_path = output_dir + filename.replace('.pdf', '.md')
    log_file_path = os.path.join(logs_dir, filename.replace('.pdf', '.log'))
    
    os.makedirs(logs_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)
    
    # Create a script content that will be executed
    script_content = f'''
from docling.document_converter import DocumentConverter
import os

converter = DocumentConverter()
doc = converter.convert("{in_path}").document

md_content = doc.export_to_markdown()

with open("{out_path}", 'w', encoding='utf-8') as f:
    f.write(md_content)
'''
    
    # Write the script to a temporary file
    temp_script = "./temp_docling_script.py"
    with open(temp_script, 'w', encoding='utf-8') as f:
        f.write(script_content)
    
    try:
        # Run the script and capture ALL output
        print(f"Running docling conversion and logging to: {log_file_path}")
        
        with open(log_file_path, 'w', encoding='utf-8') as log_file:            
            # Run python script and capture output
            process = subprocess.Popen(
                [sys.executable, temp_script],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                universal_newlines=True,
                bufsize=1
            )
            
            # Read output line by line and write to both console and file
            for line in process.stdout:
                print(line, end='')  # Display on console
                log_file.write(line)  # Write to log file
                log_file.flush()
            
            process.wait()
            
            if process.returncode == 0:
                print(f"\nConversion completed successfully!")
                log_file.write(f"\n\nConversion completed with return code: {process.returncode}\n")
            else:
                print(f"\nConversion failed with return code: {process.returncode}")
                log_file.write(f"\n\nConversion failed with return code: {process.returncode}\n")
        
        print(f"Full log saved to: {log_file_path}")
        
    finally:
        # Clean up temporary script
        if os.path.exists(temp_script):
            os.remove(temp_script)

if __name__ == "__main__":
    run_with_full_logging()