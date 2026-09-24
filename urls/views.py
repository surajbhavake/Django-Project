from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from  .serializers import URLSerializer
from .utils import generate_short_code
from .models import URL



class URLListCreateView(APIView):

    def get(self,request):
            urls = URL.objects.all()
            serializer = URLSerializer(urls,many=True)
    
            return Response(serializer.data)

    def post(self,request):
        serialzier = URLSerializer(data = request.data)

        if serialzier.is_valid():
            url = serialzier.save(
                short_code = generate_short_code()
            )

            return Response(
                URLSerializer(url).data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serialzier.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class URLDetailView(APIView):
     def get(self,request,pk):
          try:
               url = URL.objects.get(pk=pk)
          except URL.DoesNotExist:
               return Response(
                    {
                         'detail':'URL not found'
                    },
                    status=status.HTTP_404_NOT_FOUND
               )
          serializer = URLSerializer(url)
          return Response(serializer.data)

     def delete(self,request,pk):
          try:
               url = URL.objects.get(pk=pk)
          except URL.DoesNotExist:
               return Response(
                    {'detail':'URL not found'},
                    status=status.HTTP_404_NOT_FOUND,
               )
          url.delete()

          return Response(
               status=status.HTTP_204_NO_CONTENT
          )

    