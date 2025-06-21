import os
# Explicitly add GTK to PATH if needed
os.environ['PATH'] = 'C:\\gtk3\\bin;' + os.environ['PATH']

try:
    from weasyprint import HTML
    print("WeasyPrint imported successfully!")
    html = HTML(string='<h1>Test</h1>')
    html.write_pdf('test.pdf')
    print("PDF created successfully!")
except Exception as e:
    print("Error:", e)