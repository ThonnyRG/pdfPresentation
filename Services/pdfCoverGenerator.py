from abc import ABC, abstractMethod
from fpdf import FPDF
from pathlib import Path

from Config.Settings import Settings
from Model.dateFormater import DateFormatter
from Model.documentData import DocumentData

class PDFGeneratorInterface(ABC):
    @abstractMethod
    def generate(self, data: DocumentData, outputPath: Path):
        pass        
    
class coverPageGenerator(PDFGeneratorInterface):
    def __init__(self, settings: Settings):
        self.settings = settings
        
    def generate(self, data: DocumentData, outputPath: Path):
        pdf = FPDF(format = self.settings.PDF_FORMAT)
        pdf.add_page()
        
    def _addHeader(self, pdf: FPDF, uniInfo):
        pdf.set_font(self.settings.DEFAULT_FONT, size = 18)
        pdf.cell(0, 50, ln = 2, align = "R")
        pdf.cell(0, 10, txt = uniInfo.faculty, ln = 2, align="R")
        pdf.cell(0, 10, txt = uniInfo.region, ln = 2, align="R")
     
    def _addActivityTittle(self, pdf: FPDF, activityName: str):
        pdf.set_font(self.settings.DEFAULT_FONT, style = "B", size = 16)
        pdf.cell(0, 5, ln= 1, align= "R")
        pdf.cell(0, 10, text= activityName, ln= 2, align= "R")
        
    def _addCourseInfo(self, pdf : FPDF, activityName: str):
        pdf.set_font(self.settings.DEFAULT_FONT)
        pdf.cell(0, 5, text="EE: ", ln = 1, align= "R")
        
        
    def _addStudentInfo(self, pdf: FPDF, studentInfo):
        pdf.set_font(self.settings.DEFAULT_FONT, size = 16)
        pdf.cell(0, 5, ln = 1, align = "R")
        pdf.cell(0, 5, text= studentInfo.name, ln = 2, align= "R")
        
        pdf.set_font(self.settings.DEFAULT_FONT, size= 16)
        pdf.cell(0, 5, ln = 1, align= "R")
        pdf.cell(0, 5, text= "Facilitador:", ln = 1, align="R")
        pdf.cell(0, 5, text = studentInfo.facilitador, ln=2, align= "R")
        
    def _addDate(self, pdf: FPDF, targetDate):
        formatted_date = DateFormatter.formatDate(targetDate)
        pdf.set_font(self.settings.DEFAULT_FONT, size= 16)
        pdf.cell(0, 5, ln=1, align="R")
        pdf.cell(0, 5, text= formatted_date)
        
    def _universityMotto(self, pdf: FPDF, motto: str):
        pdf.set_font(self.settings.DEFAULT_FONT, size= 16)
        pdf.cell(0, 5, ln = 1, align = "R")
        pdf.cell(0, 5, text = motto, ln = 1, align = "R")
        
    def _addImages(self, pdf: FPDF):
        logoPos = self.settings.LOGO_POSITION
        flagPos = self.settings.FLAG_POSITION
        
        if self.settings.UV_FLAG.exists():
            pdf.image(str(self.settings.UV_FLAG), **flagPos)
            
        if self.settings.UV_LOGO.exists():
            pdf.image(str(self.settings.UV_LOGO), **logoPos)        