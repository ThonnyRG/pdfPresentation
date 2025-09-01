from pathlib import Path


class Settings:
    ASSETS = Path("Model/src")
    UV_LOGO = ASSETS / "uvLogo.jpg"
    UV_FLAG = ASSETS / "uvFlag.png"
    OUTPUT_DIR = Path("output")
    
    PDF_FORMAT = "Letter"
    DEFAULT_FONT = "Arial"
    
    LOGO_POSITION = {"x": 160, "y": 10, "w": 45, "h": 39}
    FLAG_POSITION = {"x": 0, "y" : 178, "w": 130, "h": 100}
    
    def __post_init__(self):
        self.OUTPUT_DIR.mkdir(exist_ok = True)
