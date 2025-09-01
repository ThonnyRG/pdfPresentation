
from Model import documentData
from Model.documentData import experienceInfo, studentInfo, universityInfo
from Services.documentService import documentService


def main():
    print("Python is trash")
    student_info = studentInfo(
        name="Balatrexis Nava Moya",
        facilitator="Magdiel"
    )
    
    experience_info = experienceInfo(
        experienceName= "Pracitas inutiles", 
        activityName="Ola"
    )
    
    university_info = universityInfo()
    
    document_data = documentData(
        student_info = student_info,
        experience_info = experience_info,
        university_info = university_info
    )
    
    document_service = documentService()
    additional_pdfs = ["lorem-ipsum.pdf"]
    
    final_document = document_service.createDocument(
        document_data = document_data,
        additional_pdfs = additional_pdfs,
        ouput= "ola.pdf"
    )
    print (f"Document Created: {final_document}")
    
if __name__ == "__main__":
    main()