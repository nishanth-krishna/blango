import json
from http import HTTPStatus

from django.http import JsonResponse, HttpResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from blog.models import Post

from blog.api.serializers import PostSerializer





@csrf_exempt
def post_list(request):
    if request.method == "GET":     #to get the list of all posts
        posts = Post.objects.all()
        return JsonResponse({"data": PostSerializer(posts, many=True).data})
    elif request.method == "POST":      # to create a post instance
        post_data = json.loads(request.body)
        serializer = PostSerializer(data=post_data)
        serializer.is_valid(raise_exception=True)
        post = serializer.save()
        return HttpResponse(
            status=HTTPStatus.CREATED,
            headers={"Location": reverse("api_post_detail", args=(post.pk,))},
        )

    return HttpResponseNotAllowed(["GET", "POST"])


@csrf_exempt
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "GET":
        return JsonResponse(PostSerializer(post).data)
    elif request.method == "PUT":
        post_data = json.loads(request.body)
        serializer = PostSerializer(post, data=post_data, partial=True)       # as we gave instance to this as an arg, it will update the "post" object.
        # serializer = PostSerializer(post, data=post_data, partial=True)       # if you set partial=True, you can choose to update by giving only few attributes.
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return HttpResponse(status=HTTPStatus.NO_CONTENT)
    elif request.method == "DELETE":
        post.delete()
        return HttpResponse(status=HTTPStatus.NO_CONTENT)

    return HttpResponseNotAllowed(["GET", "PUT", "DELETE"])