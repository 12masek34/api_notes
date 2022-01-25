from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from notes.models import Note
from api.serializers import NoteSerializer, ThinNoteSerializer
from rest_framework.views import APIView


class NoteListView(APIView):
    def get(self, request, format=Note):
        notes = Note.objects.all()
        serializer = ThinNoteSerializer(notes, many=True)
        return Response(serializer.data)

    def post(self, request, format=Note):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NoteDetailView(APIView):
    def get_object(self, pk):
        try:
            return Note.objects.get(pk=pk)
        except Note.DoesNotExisit:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=Note):
        note = self.get_object(pk)
        serializer = NoteSerializer(note)
        return Response(serializer.data)

    def put(self, request, pk, format=Note):
        note = self.get_object(pk)
        serializer = NoteSerializer(note, data=request.data)
        if serializer:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=Note):
        note = self.get_object(pk)
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#
# @api_view(['GET', 'POST'])
# def notes_list(request, format=Note):
#     if request.method == 'GET':
#         notes = Note.objects.all()
#         serializer = NoteSerializer(notes, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = NoteSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def notes_detail(request, pk, format=Note):
#     try:
#         note = Note.objects.get(pk=pk)
#     except Note.DoesNotExisit:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = NoteSerializer(note)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = NoteSerializer(note, data=request.data)
#         if serializer.is_valid:
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         note.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
