from django.db import models

# Create your models here.
class about1(models.Model):
    tittle=models.CharField(max_length=100,blank=False)
    discription=models.TextField(max_length=300,blank=False)
    image=models.ImageField(upload_to='about/',blank=False)


    def __str__(self):
        return self.tittle


class ourteam(models.Model):
    title = models.CharField(max_length=100, default='Team Member')
    image=models.ImageField(upload_to='ourteam/',blank=False)
    name=models.CharField(max_length=100,blank=False)
    role=models.CharField(max_length=100,blank=False)

    def __str__(self):
        return self.title


class client(models.Model):
    title=models.CharField(max_length=100,blank=False)
    image=models.ImageField(upload_to='client/',blank=False)

    def __str__(self):
        return self.title

class article(models.Model):
    title=models.CharField(max_length=100,blank=False)
    image=models.ImageField(upload_to='article/',blank=False)
    discpription1=models.TextField(max_length=300,blank=False)
    name=models.CharField(max_length=100,blank=False)
    role=models.CharField(max_length=100,blank=False)
    dis=models.TextField(max_length=300,blank=False)

    def __str__(self):
        return self.title
class price(models.Model):
    title=models.CharField(max_length=100,blank=False,default='pricing1')
    name1=models.CharField(max_length=100,blank=False)
    name2=models.CharField(max_length=100,blank=False)
    name3=models.CharField(max_length=100,blank=False)
    dis=models.TextField(max_length=300,blank=False)
    price1=models.CharField(max_length=100,blank=False)
    price2=models.CharField(max_length=100,blank=False)
    price3=models.CharField(max_length=100,blank=False)
    point1=models.CharField(max_length=100,blank=False)
    point2=models.CharField(max_length=100,blank=False)
    point3=models.CharField(max_length=100,blank=False)
    point4=models.CharField(max_length=100,blank=False)
    point5=models.CharField(max_length=100,blank=False)
    point6=models.CharField(max_length=100,blank=False)
    point7=models.CharField(max_length=100,blank=False)
    def __str__(self):
        return self.title


class contactforms(models.Model):
    name=models.CharField(max_length=100,blank=False)
    email=models.EmailField(max_length=100)
    subject=models.CharField(max_length=100)
    message=models.TextField(max_length=300)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name