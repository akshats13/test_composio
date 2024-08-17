# Clone the repository 

git clone [repository-url]  
cd [repository-directory]

# Set up a virtual environment 

python -m venv venv
venv\Scripts\activate

# Instatll dependencies

pip install -r requirements.txt

# Run the tests 

python -m unittest test_tools.py

# To use the tool , utilzie this code sample 

from custom_tools import PdfReaderTool

tool = PdfReaderTool()
text = tool.read_pdf('path to your pdf file')
metadata = tool.extract_metadata('path to your pdf file')

print("Text Content:", text)
print("Metadata:", metadata)

