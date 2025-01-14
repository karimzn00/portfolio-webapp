from rest_framework import serializers
from blogs.models import Blog

class BlogsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Blog
		fields = ['id', 'title', 'description', 'date', 'content']