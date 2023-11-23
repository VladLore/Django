from django.core.management.base import BaseCommand, CommandParser
from myapp2.models import Author, Post


class Command(BaseCommand):
    help = "Get all users"
    
    def add_arguments(self, parser: CommandParser):
        parser.add_argument('count', type=int, help='UserID')

    def handle(self, *args, **kwargs):
        count = kwargs.get("count")
        for i in range(1, count + 1):
            author = Author(name=f"Name:{i}", email=f"mail{i}@mail.ru")
            author.save()
            for j in range(1, count + 1):
                post = Post(
                    title=f"Title:{j}",
                    content=f"Text from {author.name} #{j} is bla bla bla many long text",
                    author=author,
                )
                post.save()
