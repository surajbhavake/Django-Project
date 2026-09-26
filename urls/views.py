

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from  .serializers import URLSerializer
from django.shortcuts import redirect
from .services import create_url,delete_url,get_url_by_id
from .models import URL
from .exceptions import URLCreationError

class URLListCreateView(APIView):

    def get(self,request):
            urls = URL.objects.all()
            serializer = URLSerializer(urls,many=True)
    
            return Response(serializer.data)

    def post(self,request):
        serializer = URLSerializer(data = request.data)

        if serializer.is_valid():
            try:
                url = create_url(serializer.validated_data['original_url'])
            except URLCreationError:
                 return Response(
                      {'detail':'unable to create the short URL.',},
                      status= status.HTTP_500_INTERNAL_SERVER_ERROR
                 )
            return Response(
                URLSerializer(url).data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class URLDetailView(APIView):
     def get(self,request,pk):
          url = get_url_by_id(pk)
          if url is None:
               return Response(
                    {
                         'detail':'URL not found'
                    },
                    status=status.HTTP_404_NOT_FOUND
               )
          serializer = URLSerializer(url)
          return Response(serializer.data)

     def delete(self,request,pk):
          url =get_url_by_id(pk)
          if url is None:
               return Response(
                    {'detail':'URL not found'},
                    status=status.HTTP_404_NOT_FOUND,
               )
          delete_url(url)

          return Response(
               status=status.HTTP_204_NO_CONTENT
          )


class URlRedirectView(APIView):
     def get(self,request,short_code):
          try:
               url = URL.objects.get(short_code=short_code)
          except URL.DoesNotExist:
               return Response(
                    {'detail': ' Short URL not found'},
                    status= status.HTTP_404_NOT_FOUND,
               )

          return redirect(url.original_url)