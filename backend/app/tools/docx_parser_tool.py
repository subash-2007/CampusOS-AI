import io
import logging
from typing import Dict, Any

logger = logging.getLogger("CampusOS.DOCXParserTool")

class DOCXParserTool:
    """Tool for extracting raw text and structure from Microsoft Word (.docx) documents."""
    def __init__(self):
        self.name = "DOCX Parser Tool"
        self.description = "Parses Word document paragraphs and headings."

    async def execute(self, docx_bytes: bytes) -> Dict[str, Any]:
        if not docx_bytes:
            return {"status": "error", "extracted_text": "", "paragraph_count": 0}
        
        extracted_text = ""
        try:
            import docx
            doc = docx.Document(io.BytesIO(docx_bytes))
            paragraphs = [p.text.strip() for p in doc.paragraphs if p.text.strip()]
            extracted_text = "\n".join(paragraphs)
        except Exception as e:
            logger.warning(f"docx extraction fallback: {e}")
            extracted_text = docx_bytes.decode("utf-8", errors="ignore")

        return {
            "status": "success",
            "extracted_text": extracted_text,
            "word_count": len(extracted_text.split()),
            "has_content": bool(extracted_text.strip())
        }

docx_parser_tool = DOCXParserTool()
