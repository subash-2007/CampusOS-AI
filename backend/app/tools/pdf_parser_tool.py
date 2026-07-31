import io
import logging
from typing import Dict, Any

logger = logging.getLogger("CampusOS.PDFParserTool")

class PDFParserTool:
    """Tool for extracting raw text, headings, and section structures from PDF files."""
    def __init__(self):
        self.name = "PDF Parser Tool"
        self.description = "Extracts structured plain text, contact info, and sections from PDF documents."

    async def execute(self, pdf_bytes: bytes) -> Dict[str, Any]:
        if not pdf_bytes:
            return {"status": "error", "extracted_text": "", "section_count": 0}
        
        extracted_text = ""
        try:
            import pypdf
            reader = pypdf.PdfReader(io.BytesIO(pdf_bytes))
            pages = [page.extract_text() for page in reader.pages if page.extract_text()]
            extracted_text = "\n".join(pages)
        except Exception as e:
            logger.warning(f"pypdf extraction failed, attempting fallback: {e}")
            try:
                extracted_text = pdf_bytes.decode("utf-8", errors="ignore")
            except Exception:
                extracted_text = ""

        lines = [line.strip() for line in extracted_text.split("\n") if line.strip()]
        return {
            "status": "success",
            "extracted_text": extracted_text,
            "line_count": len(lines),
            "word_count": len(extracted_text.split()),
            "has_content": bool(extracted_text.strip())
        }

pdf_parser_tool = PDFParserTool()
