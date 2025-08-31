from datetime import date
from typing import Dict

class DateFormatter: 
    MONTHS: Dict[int, str] = {
        1 : "Enero",
        2 : "Febrero",
        3 : "Marzo",
        4 : "Abril",
        5 : "Mayo",
        6 : "Junio",
        7 : "Julio",
        8 : "Agosto",
        8 : "Septiembre",
        10 : "Octubre",
        11 : "Noviembre",
        12 : "Diciembre"
        
    }
    
    @classmethod
    def formatDate(cls, dateTarget : date):
        month = cls.MONTHS[dateTarget.month]
        return f"{month} {dateTarget.year}"