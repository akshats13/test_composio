import unittest
from custom_tools import PdfReaderTool

class TestPdfReaderTool(unittest.TestCase):
    def test_read_pdf(self):
        tool = PdfReaderTool()
        file_path = "pdf-sample.pdf"
        text = tool.read_pdf(file_path)
        print(f"Output of read_pdf: {text}")
        self.assertIsNotNone(text)

    def test_extract_metadata(self):
        tool = PdfReaderTool()
        file_path = "pdf-sample.pdf"
        metadata = tool.extract_metadata(file_path)
        print(f"Output of extract_metadata: {metadata}")
        self.assertIsNotNone(metadata)

    def test_handle_tool_call(self):
        tool = PdfReaderTool()
        tool_call = {"input": {"action": "read_pdf", "file_path": "pdf-sample.pdf"}}
        text = tool.handle_tool_call(tool_call)
        print(f"Output of handle_tool_call with action'read_pdf': {text}")
        self.assertIsNotNone(text)

    def test_handle_tool_call_invalid_action(self):
        tool = PdfReaderTool()
        tool_call = {"input": {"action": "invalid_action", "file_path": "pdf-sample.pdf"}}
        try:
            tool.handle_tool_call(tool_call)
        except ValueError as e:
            print(f"Error message for invalid action: {e}")
        else:
            self.fail("Expected ValueError for invalid action")

if __name__ == "__main__":
    unittest.main()