from pathlib import Path
from typing import List, Optional

from Config.Settings import Settings
from Model.documentData import DocumentData
from Services.pdfCoverGenerator import coverPageGenerator
from Services.pdfMerger import PDFMergerService

class documentService:
    def __init__(self, settings: Optional[Settings]):
        self.settings = settings or Settings()
        self.coverGenerator = coverPageGenerator(self.settings)
        self.pdf_merger = PDFMergerService()
        
    def createDocument(self, documentData: DocumentData, aditionalPdfs: Optional[List[str]], ouput: str = "Merged.pdf"):
        coverPath = self.settings.OUTPUT_DIR / "cover.pdf"
        self.coverGenerator.generate(documentData, coverPath)
        
        pdfPaths = [coverPath]
        
        if aditionalPdfs:
            for pdfName in aditionalPdfs:
                pdf_path = Path(pdfName)
                if pdf_path.exists():
                    pdf_path.append(pdf_path)
                    
        finalPath = self.settings.OUTPUT_DIR / ouput
        return self.pdf_merger.mergePdfs(pdfPaths, finalPath)
        