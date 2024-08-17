import PyPDF2
from composio.tools.local.base import Tool

class PdfReaderTool(Tool):
    READ_PDF_ACTION = "read_pdf"
    EXTRACT_METADATA_ACTION = "extract_metadata"

    def __init__(self):
        super(PdfReaderTool, self).__init__()

    def read_pdf(self, file_path: str) -> str:
        pdf_file = open(file_path, 'rb')
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ''
        for page in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page].extract_text()
        pdf_file.close()
        return text
    
    def extract_metadata(self, file_path: str) -> dict:
        pdf_file = open(file_path, 'rb')
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        metadata = pdf_reader.metadata
        pdf_file.close()
        return metadata
    
    def _handle_input(self, tool_call: dict) -> tuple:
        if "input" not in tool_call:
            raise ValueError("Missing 'input' key in tool call")
        
        input_dict = tool_call["input"]
        
        if "action" not in input_dict or "file_path" not in input_dict:
            raise ValueError("Missing 'action' or 'file_path' key in input")
        
        action = input_dict["action"]
        file_path = input_dict["file_path"]
        
        if action not in [self.READ_PDF_ACTION, self.EXTRACT_METADATA_ACTION]:
            raise ValueError(f"Invalid action: {action}")
        
        return action, file_path
    
    def handle_tool_call(self, tool_call: dict) -> str:
        action, file_path = self._handle_input(tool_call)
        
        if action == self.READ_PDF_ACTION:
            return self.read_pdf(file_path)
        elif action == self.EXTRACT_METADATA_ACTION:
            return self.extract_metadata(file_path)