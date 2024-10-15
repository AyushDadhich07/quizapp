from rest_framework import serializers
from .models import PDFDocument

class PDFDocumentSerializer(serializers.ModelSerializer):
    file = serializers.FileField(source='pdf_file')

    class Meta:
        model = PDFDocument
        fields = ['id', 'file', 'uploaded_at', 'processed']

    def create(self, validated_data):
        validated_data['pdf_file'] = validated_data.pop('file')
        return super().create(validated_data)
