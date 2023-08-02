from django.db import models
from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
# Create your models here.

class voter(models.Model):
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=2, choices=(
        (u'M', u'Male'),
        (u'F', u'Female'),
    ))
    phone = models.CharField(max_length=100)
    age = models.IntegerField(default="")
    address = models.TextField()
    voter_no = models.CharField(max_length=100,unique=True)
    class Meta:
        db_table = "voter"
    def __str__(self):
        return self.voter_no

class parties(models.Model):
    id = models.AutoField(primary_key=100,unique=True)
    party_name = models.CharField(max_length=100)
    party_sign = models.CharField(max_length=100)
    party_image = models.ImageField(upload_to = "vote_image/",default = "")
    class Meta:
        db_table = "parties"
    def __str__(self):
        return self.party_name
    
def img_deleter(sender, **kwargs):
    photo = kwargs['instance']
    if (parties.objects.filter(id = photo.id).count()):
        m1 = parties.objects.filter(id = photo.id)[0]
        storage, path = m1.party_image.storage, m1.party_image.path
        storage.delete(path) 

pre_save.connect(img_deleter,sender = parties)

def img_update(sender, **kwargs):
    photo = kwargs['instance']
    storage, path = photo.party_image.storage, photo.party_image.path
    storage.delete(path)

pre_delete.connect(img_update,sender = parties)

class vote_box(models.Model):
    id = models.AutoField(primary_key=100)
    voter_id= models.ForeignKey(voter, on_delete=None)
    vote_id = models.ForeignKey(parties, on_delete=None)
    class Meta:
        db_table = "vote_box"
    def __str__(self):
        return self.vote_id.party_name