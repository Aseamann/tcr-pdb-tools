from django.db import models
from django.contrib.auth import get_user_model

from martor.models import MartorField
from app.PDB_Tools_V3 import PdbTools3

User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    title = models.CharField(max_length=200)
    description = MartorField()
    wiki = MartorField(blank=True)
    tool = PdbTools3()
    tool.set_file_name("app/3gsn.pdb")
    chains = tool.get_chains()
    print(chains)

    def __str__(self):
        return self.title


class PostMeta(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = MartorField()

    def __str__(self):
        return self.text
