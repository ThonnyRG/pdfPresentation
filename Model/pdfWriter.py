# import fpdf
# import gdown
# from docx2pdf import convert
# from PyPDF2 import PdfMerger
# from datetime import date

# todays_date = date.today()
# months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

# currentMonth = months[todays_date.month - 1]
# currentYear = todays_date.year

# formatDate = f"{currentMonth} {currentYear}"

# pdf = fpdf.FPDF(format= "Letter")
# pdf.add_page()
# pdf.set_font("Arial", size=18)
# pdf.cell(0, 50,ln = 2, align = "R")
# pdf.cell(0, 10, txt = "Facultad de contaduría y administración", ln = 2, align= "R")
# pdf.cell(0, 10, txt = "Región Coatzacoalcos", ln = 1, align= "R")

# #Poner en Arial Black
# pdf.set_font("Arial", size = 14)
# pdf.cell(0, 5, txt = "Lic. en Ingeniería de Software", ln = 2, align = "R")

# pdf.set_font("Arial", style = "B", size = 24)
# pdf.cell(0, 5, ln = 1, align = "R")
# pdf.cell(0, 10, txt = "Nombre de la actividad lorem ipsum", ln = 2, align = "R")

# pdf.set_font("Arial", size = 14)
# pdf.cell(0, 5, ln = 1, align = "R")
# pdf.cell(0, 5, txt = "EE:", ln = 1, align = "R")
# pdf.cell(0, 5, txt = "Materia sample eeee lorem ipsum", ln = 2, align = "R")

# #Poner en Arial Black
# pdf.set_font("Arial", style = "B", size = 16)
# pdf.cell(0, 5, ln = 1, align = "R")
# pdf.cell(0, 5, txt = "Alumno:", ln = 1, align = "R")
# pdf.cell(0, 5, txt = "Balatro Balatrez Del Balatrin Balatren", ln = 2, align = "R")

# pdf.set_font("Arial", size = 16)
# pdf.cell(0, 5, ln = 1, align = "R")
# pdf.cell(0, 5, txt = "Facilitador:", ln = 1, align = "R")
# pdf.cell(0, 5, txt = "Magdiel Omar Mercado Carrillo", ln = 2, align = "R")

# # Obtener la fecha
# pdf.set_font("Arial", size = 16)
# pdf.cell(0, 5, ln = 1, align = "R")
# pdf.cell(0, 5, txt = str(formatDate), ln = 1, align = "R")

# pdf.set_font("Arial", size = 16)
# pdf.cell(0, 5, ln = 1, align = "R")
# pdf.cell(0, 5, txt = "Lis de Veracruz: Arte, Ciencia y luz", ln = 1, align = "R")

# pdf.image("Model/src/uvLogo.jpg", x = 160, y = 10, w = 45, h = 39)
# pdf.image("Model/src/uvFlag.png", x = 0, y = 178, w = 130, h = 100)


# pdf.output("test.pdf")

# pdfUser = "lorem-ipsum.pdf"

# x = ["test.pdf", pdfUser]

# merger = PdfMerger()

# for pdf in x:
#     merger.append(pdf)

# merger.write("final.pdf")
# merger.close()



# # pdf_generator/models/document_data.py
# from dataclasses import dataclass
# from typing import Optional
# from datetime import date

# @dataclass
# class StudentInfo:
#     name: str
#     facilitator: str
    
# @dataclass
# class CourseInfo:
#     subject_name: str
#     activity_name: str
    
# @dataclass
# class UniversityInfo:
#     faculty: str = "Facultad de contaduría y administración"
#     region: str = "Región Coatzacoalcos"
#     career: str = "Lic. en Ingeniería de Software"
#     motto: str = "Lis de Veracruz: Arte, Ciencia y luz"

# @dataclass
# class DocumentData:
#     student_info: StudentInfo
#     course_info: CourseInfo
#     university_info: UniversityInfo
#     created_date: Optional[date] = None
    
#     def __post_init__(self):
#         if self.created_date is None:
#             self.created_date = date.today()

# # pdf_generator/utils/date_formatter.py
# from datetime import date
# from typing import Dict

# class DateFormatter:
#     MONTHS: Dict[int, str] = {
#         1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril",
#         5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
#         9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
#     }
    
#     @classmethod
#     def format_spanish_date(cls, target_date: date) -> str:
#         """Formatea una fecha en español (Mes Año)"""
#         month = cls.MONTHS[target_date.month]
#         return f"{month} {target_date.year}"

# # pdf_generator/config/settings.py
# from pathlib import Path

# class Settings:
#     # Paths
#     ASSETS_DIR = Path("Model/src")
#     UV_LOGO_PATH = ASSETS_DIR / "uvLogo.jpg"
#     UV_FLAG_PATH = ASSETS_DIR / "uvFlag.png"
#     OUTPUT_DIR = Path("output")
    
#     # PDF Configuration
#     PDF_FORMAT = "Letter"
#     DEFAULT_FONT = "Arial"
    
#     # Layout Constants
#     LOGO_POSITION = {"x": 160, "y": 10, "w": 45, "h": 39}
#     FLAG_POSITION = {"x": 0, "y": 178, "w": 130, "h": 100}
    
#     def __post_init__(self):
#         self.OUTPUT_DIR.mkdir(exist_ok=True)

# # pdf_generator/services/pdf_cover_generator.py
# from abc import ABC, abstractmethod
# from fpdf import FPDF
# from pathlib import Path

# from ..models.document_data import DocumentData
# from ..utils.date_formatter import DateFormatter
# from ..config.settings import Settings

# class PDFGeneratorInterface(ABC):
#     @abstractmethod
#     def generate(self, data: DocumentData, output_path: Path) -> Path:
#         pass

# class CoverPageGenerator(PDFGeneratorInterface):
#     def __init__(self, settings: Settings):
#         self.settings = settings
        
#     def generate(self, data: DocumentData, output_path: Path) -> Path:
#         """Genera la página de portada del documento"""
#         pdf = FPDF(format=self.settings.PDF_FORMAT)
#         pdf.add_page()
        
#         self._add_header(pdf, data.university_info)
#         self._add_activity_title(pdf, data.course_info.activity_name)
#         self._add_course_info(pdf, data.course_info.subject_name)
#         self._add_student_info(pdf, data.student_info)
#         self._add_date(pdf, data.created_date)
#         self._add_university_motto(pdf, data.university_info.motto)
#         self._add_images(pdf)
        
#         pdf.output(str(output_path))
#         return output_path
    
#     def _add_header(self, pdf: FPDF, uni_info) -> None:
#         """Agrega el encabezado de la universidad"""
#         pdf.set_font(self.settings.DEFAULT_FONT, size=18)
#         pdf.cell(0, 50, ln=2, align="R")
#         pdf.cell(0, 10, txt=uni_info.faculty, ln=2, align="R")
#         pdf.cell(0, 10, txt=uni_info.region, ln=1, align="R")
        
#         pdf.set_font(self.settings.DEFAULT_FONT, size=14)
#         pdf.cell(0, 5, txt=uni_info.career, ln=2, align="R")
    
#     def _add_activity_title(self, pdf: FPDF, activity_name: str) -> None:
#         """Agrega el título de la actividad"""
#         pdf.set_font(self.settings.DEFAULT_FONT, style="B", size=24)
#         pdf.cell(0, 5, ln=1, align="R")
#         pdf.cell(0, 10, txt=activity_name, ln=2, align="R")
    
#     def _add_course_info(self, pdf: FPDF, subject_name: str) -> None:
#         """Agrega información del curso"""
#         pdf.set_font(self.settings.DEFAULT_FONT, size=14)
#         pdf.cell(0, 5, ln=1, align="R")
#         pdf.cell(0, 5, txt="EE:", ln=1, align="R")
#         pdf.cell(0, 5, txt=subject_name, ln=2, align="R")
    
#     def _add_student_info(self, pdf: FPDF, student_info) -> None:
#         """Agrega información del estudiante y facilitador"""
#         pdf.set_font(self.settings.DEFAULT_FONT, style="B", size=16)
#         pdf.cell(0, 5, ln=1, align="R")
#         pdf.cell(0, 5, txt="Alumno:", ln=1, align="R")
#         pdf.cell(0, 5, txt=student_info.name, ln=2, align="R")
        
#         pdf.set_font(self.settings.DEFAULT_FONT, size=16)
#         pdf.cell(0, 5, ln=1, align="R")
#         pdf.cell(0, 5, txt="Facilitador:", ln=1, align="R")
#         pdf.cell(0, 5, txt=student_info.facilitator, ln=2, align="R")
    
#     def _add_date(self, pdf: FPDF, target_date) -> None:
#         """Agrega la fecha formateada"""
#         formatted_date = DateFormatter.format_spanish_date(target_date)
#         pdf.set_font(self.settings.DEFAULT_FONT, size=16)
#         pdf.cell(0, 5, ln=1, align="R")
#         pdf.cell(0, 5, txt=formatted_date, ln=1, align="R")
    
#     def _add_university_motto(self, pdf: FPDF, motto: str) -> None:
#         """Agrega el lema de la universidad"""
#         pdf.set_font(self.settings.DEFAULT_FONT, size=16)
#         pdf.cell(0, 5, ln=1, align="R")
#         pdf.cell(0, 5, txt=motto, ln=1, align="R")
    
#     def _add_images(self, pdf: FPDF) -> None:
#         """Agrega las imágenes (logo y bandera)"""
#         logo_pos = self.settings.LOGO_POSITION
#         flag_pos = self.settings.FLAG_POSITION
        
#         if self.settings.UV_LOGO_PATH.exists():
#             pdf.image(str(self.settings.UV_LOGO_PATH), **logo_pos)
        
#         if self.settings.UV_FLAG_PATH.exists():
#             pdf.image(str(self.settings.UV_FLAG_PATH), **flag_pos)

# # pdf_generator/services/pdf_merger.py
# from PyPDF2 import PdfMerger
# from pathlib import Path
# from typing import List

# class PDFMergerService:
#     @staticmethod
#     def merge_pdfs(pdf_paths: List[Path], output_path: Path) -> Path:
#         """Combina múltiples PDFs en uno solo"""
#         merger = PdfMerger()
        
#         try:
#             for pdf_path in pdf_paths:
#                 if pdf_path.exists():
#                     merger.append(str(pdf_path))
#                 else:
#                     print(f"Warning: PDF file not found: {pdf_path}")
            
#             merger.write(str(output_path))
#             return output_path
        
#         finally:
#             merger.close()

# # pdf_generator/services/document_service.py
# from pathlib import Path
# from typing import List, Optional

# from ..models.document_data import DocumentData
# from .pdf_cover_generator import CoverPageGenerator
# from .pdf_merger import PDFMergerService
# from ..config.settings import Settings

# class DocumentService:
#     def __init__(self, settings: Optional[Settings] = None):
#         self.settings = settings or Settings()
#         self.cover_generator = CoverPageGenerator(self.settings)
#         self.pdf_merger = PDFMergerService()
    
#     def create_document(
#         self, 
#         document_data: DocumentData, 
#         additional_pdfs: Optional[List[str]] = None,
#         output_filename: str = "final.pdf"
#     ) -> Path:
#         """
#         Crea un documento completo con portada y PDFs adicionales
#         """
#         # Generar portada
#         cover_path = self.settings.OUTPUT_DIR / "cover.pdf"
#         self.cover_generator.generate(document_data, cover_path)
        
#         # Preparar lista de PDFs para combinar
#         pdf_paths = [cover_path]
        
#         if additional_pdfs:
#             for pdf_name in additional_pdfs:
#                 pdf_path = Path(pdf_name)
#                 if pdf_path.exists():
#                     pdf_paths.append(pdf_path)
        
#         # Combinar PDFs
#         final_path = self.settings.OUTPUT_DIR / output_filename
#         return self.pdf_merger.merge_pdfs(pdf_paths, final_path)

# # pdf_generator/main.py (ejemplo de uso)
# from pathlib import Path
# from .models.document_data import DocumentData, StudentInfo, CourseInfo, UniversityInfo
# from .services.document_service import DocumentService

# def main():
#     # Configurar datos del documento
#     student_info = StudentInfo(
#         name="Balatro Balatrez Del Balatrin Balatren",
#         facilitator="Magdiel Omar Mercado Carrillo"
#     )
    
#     course_info = CourseInfo(
#         subject_name="Materia sample eeee lorem ipsum",
#         activity_name="Nombre de la actividad lorem ipsum"
#     )
    
#     university_info = UniversityInfo()
    
#     document_data = DocumentData(
#         student_info=student_info,
#         course_info=course_info,
#         university_info=university_info
#     )
    
#     # Crear documento
#     document_service = DocumentService()
#     additional_pdfs = ["lorem-ipsum.pdf"]  # PDFs adicionales a incluir
    
#     final_document = document_service.create_document(
#         document_data=document_data,
#         additional_pdfs=additional_pdfs,
#         output_filename="final.pdf"
#     )
    
#     print(f"Documento creado: {final_document}")

# if __name__ == "__main__":
#     main()