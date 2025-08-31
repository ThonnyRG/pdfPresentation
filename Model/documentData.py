from dataclasses import dataclass
from typing import Optional
from datetime import date

@dataclass
class studentInfo:
    name: str
    facilitator: str
    
@dataclass
class experienceInfo:
    experienceName: str
    activityName: str
  
@dataclass
class universityInfo:
    faculty: str = "Facultad de contaduría y administración"
    region: str = "Región Coatzacoalcos"
    career: str = "Lic. en Ingeniería de Software"
    motto: str = "Lis de Veracruz: Arte, Ciencia y luz"
    
@dataclass
class DocumentData: 
    studentInfo: studentInfo
    experienceInfo: experienceInfo
    universityInfo: universityInfo
    
    