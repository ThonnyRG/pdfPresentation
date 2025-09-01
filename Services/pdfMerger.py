from pathlib import Path
from typing import List
from PyPDF2 import PdfMerger


class PDFMergerService:
    @staticmethod
    def mergePdfs(pdf_paths: List[Path], outputPath: Path):
        merger = PdfMerger()
        
        try:
            for pdfPath in pdf_paths:
                if pdf_paths.exists():
                    merger.append(str(pdf_paths))
                else:
                    print(f"Warning: PDF file not found {pdfPath}")
            
            merger.write(str(outputPath))
            return outputPath
        
        finally:
            merger.close()  
        
        