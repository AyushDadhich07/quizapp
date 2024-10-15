from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .models import PDFDocument
from .serializers import PDFDocumentSerializer
import PyPDF2
import io
from .quiz_generator import generate_quiz, chunk_text
from .groq_processor import process_pdf_content
from PyPDF2.errors import EmptyFileError
import logging

logger = logging.getLogger(__name__)

@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def create_pdf_document(request):
    print(f"Received data: {request.data}")
    
    serializer = PDFDocumentSerializer(data=request.data)
    
    if not serializer.is_valid():
        logger.error(f"Serializer errors: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    pdf_file = request.FILES.get('file')
    if not pdf_file:
        logger.error("No PDF file provided")
        return Response({"error": "No PDF file provided"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(pdf_file.read()))
        text_content = ""
        for page in pdf_reader.pages:
            text_content += page.extract_text()

        # Process text content with Groq API
        processed_content = process_pdf_content(text_content)

        # Generate quiz using Llama 3.1 via Groq API
        chunks = chunk_text(processed_content)
        quiz_questions = []
        for chunk in chunks:
            quiz_questions.extend(generate_quiz(chunk))

        # Update the PDFDocument instance with the generated quiz
        pdf_document = serializer.save()
        pdf_document.processed = True
        pdf_document.save()

        # TODO: Store the generated quiz questions in the database

        return Response({"id": pdf_document.id, "quiz_questions": quiz_questions}, status=status.HTTP_201_CREATED)
    except EmptyFileError:
        logger.error("The uploaded PDF file is empty")
        return Response({"error": "The uploaded PDF file is empty"}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        logger.error(f"Error processing PDF: {str(e)}")
        return Response({"error": f"Error processing PDF: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_pdf_documents(request):
    pdf_documents = PDFDocument.objects.all()
    serializer = PDFDocumentSerializer(pdf_documents, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_pdf_document(request, pk):
    try:
        pdf_document = PDFDocument.objects.get(pk=pk)
    except PDFDocument.DoesNotExist:
        return Response({"error": "PDF document not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = PDFDocumentSerializer(pdf_document)
    return Response(serializer.data)

@api_view(['PUT'])
@parser_classes([MultiPartParser, FormParser])
def update_pdf_document(request, pk):
    try:
        pdf_document = PDFDocument.objects.get(pk=pk)
    except PDFDocument.DoesNotExist:
        return Response({"error": "PDF document not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = PDFDocumentSerializer(pdf_document, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_pdf_document(request, pk):
    try:
        pdf_document = PDFDocument.objects.get(pk=pk)
    except PDFDocument.DoesNotExist:
        return Response({"error": "PDF document not found"}, status=status.HTTP_404_NOT_FOUND)
    
    pdf_document.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
