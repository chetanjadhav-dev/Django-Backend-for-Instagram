from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.views import APIView
from contents.models import Post
from contents.serializers import PostSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist

class CreatPost(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class PostList(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class RetrivePost(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UpdatePost(APIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        try:
            post = Post.objects.get(id=pk)
            serializer = PostSerializer(post, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response({'success': True, 'message': f'post is updated'})
            else:
                print(serializer.errors)
                return Response({'success': False, 'message': 'error updating the Post'})
        except ObjectDoesNotExist:
            return Response({'success': False, 'message': 'Post does not exist!'})
        

class DeletePost(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def destroy(self, request, pk):
        try:
            post = Post.objects.get(id=pk)
            if post.user.id == request.user.id:
                self.perform_destroy(post)

                return Response({'success': True, 'message': 'Post deleted successfully!'})
            else:
                return Response({'success': False, 'message': 'invalid authentication!'})
        except ObjectDoesNotExist:
            return Response({'success': False, 'message': 'Post does not exist!'})