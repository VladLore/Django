from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from myapp2.models import Author, Post

class Command(BaseCommand):
    help = "Get post by author id"
    
    def add_arguments(self, parser: CommandParser):
        parser.add_argument('pk', type=int, help='UserID')
        
    def handle(self, *args, **kwargs):
        pk=kwargs.get('pk')
        author=Author.objects.filter(pk=pk).first()
        if author is not None:
            posts=Post.objects.filter(author=author)
            intro=f'All posts of {author.name}\n'
            text='\n'.join(post.content for post in posts)
            self.stdout.write(f'{intro}{text}')
            
    # def handle(self, *args, **kwargs):
    #     pk = kwargs.get('pk')
    #     posts = Post.objects.filter(author__pk=pk)
    #     intro = f'All posts\n'
    #     text = '\n'.join(post.content for post in posts)
    #     self.stdout.write(f'{intro}{text}')
