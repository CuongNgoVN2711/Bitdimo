from django.db import models
from django_mysql.models import ListCharField

class User(models.Model):
    '''
    #Table user   // vì chưa biết xử lí thế nào với nó
    #  
    '''
    GENDER=(
        ('F' ,"Female" ),
        ('M' , 'Male')
    )
    STATUS = (
        ('act','active'),
        ('uact', 'unactive')
    )
    username  = models.CharField(max_length = 50, unique = True)
    password  = models.CharField(max_length = 20)
    nickname = models.CharField(max_length = 255, blank=True, null=True)
    email  = models.EmailField(unique = True)
    avatar = models.CharField(max_length = 255, blank=True, null=True)
    gender = models.CharField(max_length = 1  ,choices=GENDER, default='F', blank=True, null=True)
    birthdate =  models.DateField(blank=True, null=True) 
    status  = models.CharField(max_length = 4 ,choices=STATUS, default='uact')
    def  __str__ (self):
        return  "{}".format(self.username) 

class Province(models.Model):
    '''
    #Table  province (Tỉnh)
    '''
    province_name =  models.CharField(max_length = 255, unique = True)

    def __str__(self):
        return 'Province: {}'.format(self.province_name)

class Area(models.Model):
    '''
    #Table  Area ( Khu vực )
    '''

    province = models.ForeignKey(Province , on_delete=models.CASCADE)
    area_name  =  models.CharField(max_length = 200)

    def __str__(self):
        return 'Area: {}-{}'.format(self.area_name, self.province)


class Place(models.Model):
    '''
    #Table  Place (Danh thắng )  : Name  of beautiful place
    '''
    place_name =  models.CharField(max_length = 150)
    address = models.CharField(max_length = 300)
    longtitude  = models.CharField(max_length = 200, blank=True, null=True)
    latitude  = models.CharField(max_length =  200, blank=True, null=True)
    area =  models.ForeignKey(Area , on_delete=models.PROTECT)

    def  __str__ (self):
        return  "{}-{}-{}".format(self.place_name , self.address, self.area)


class AdminPost(models.Model):
    '''
    #Table post  of user
    '''
    place = models.ForeignKey(Place, on_delete = models.CASCADE)
    #evaluates = models.FloatField(default = 0.0)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    number_of_like = models.IntegerField(default = 0)
    number_of_images =  models.IntegerField(default = 0)
    number_of_comment = models.IntegerField(default = 0)
    #average_rating = models.FloatField(default = 0.0)
    content = models.TextField(max_length = 1000, blank=True, null=True)
    def  __str__ (self):
        return  "{}".format(self.place) 

    def placename(self):
        return self.place.place_name
    
    def address(self):
        return self.place.address

    def areaname(self):
        return self.place.area.area_name
    
    def longtitude_of_place(self):
        return self.place.longtitude
    
    def latitude_of_place(self):
        return self.place.latitude

class UserPost(models.Model):
    '''
    #Table post  of user
    '''
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'user')
    #area = models.ForeignKey(Area, on_delete = models.CASCADE, related_name = 'area')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    #evaluates = models.FloatField(default = 0.0)
    number_of_like = models.IntegerField(default = 0)
    number_of_images =  models.IntegerField(default = 0)
    number_of_comment = models.IntegerField(default = 0)
    #average_rating = models.FloatField(default = 0.0)
    content = models.TextField(max_length = 1000, blank=True, null=True)
    address = models.CharField(max_length = 255)
    longtitude = models.CharField(max_length = 255, blank=True, null=True)
    latitude = models.CharField(max_length = 255, blank=True, null=True)
    
    def  __str__ (self):
        return  "{}".format(self.user) 

    def username(self):
        return self.user.username

    def urlavatar(self):
        return self.user.avatar

"""     def areaname(self):
        return self.area.area_name """


class AdminPostComment(models.Model):
    '''
    #Table comment  of post  
    '''
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(AdminPost, on_delete = models.CASCADE, related_name = 'comments')
    content  =  models.TextField(max_length=1000)
    time_comment =  models.DateTimeField(blank=True, null=True)

    def  __str__ (self):
        return  '{}'.format(self.content)

    def nameuser(self):
        return self.user.username

    def urlavatar(self):
        return self.user.avatar

class UserPostComment(models.Model):
    '''
    #Table comment  of post  
    '''
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(UserPost, on_delete = models.CASCADE)
    content  =  models.TextField(max_length=1000)
    time_comment =  models.DateTimeField(blank=True, null=True)

    def  __str__ (self):
        return  "{}-{}".format(self.post , self.user)

class AdminPostImage(models.Model):
    post = models.ForeignKey(AdminPost, on_delete = models.CASCADE, related_name = 'images')
    url = models.CharField(max_length = 255)

    def __str__(self):
        return '{}  '.format(self.url)

class UserPostImage(models.Model):
    post = models.ForeignKey(UserPost, on_delete = models.CASCADE , related_name = 'images')
    url = models.CharField(max_length = 255)

    def __str__(self):
        return '{}'.format(self.url)

""" class MyDateTimeField(models.DateTimeField):
    def get_prep_value(self, value):
        from dateutil.parser import parse
        from datetime import timedelta
        td = float(value[-5:])/100
        timediff = timedelta(hours=td)
        return parse(value).replace(tzinfo=None) - timediff
 """        
""" 
    def __unicode__(self):
        return '{}: {}'.format(self.id, self.url) """

""" class Avatar(models.Model):
    '''
    #Table images of  post   
    '''
    url  = models.CharField(max_length = 255)
    user = models.ForeignKey(User , on_delete=models.CASCADE) 
    def  __str__ (self):
        return  "{}-{}".format(self.user, self.url)
"""
""" 
class AdminPostEvaluate(models.Model):
    '''
    #Table  evaluate ( Đánh giá )
    '''
    post =models.OneToOneField(AdminPost , on_delete=models.CASCADE)
    value = models.FloatField(default = 0.0) 
    def  __str__ (self):
        return  "{}-{}".format(self.post , self.value)

class UserPostEvaluate(models.Model):
    '''
    #Table  evaluate ( Đánh giá )
    '''
    post =models.OneToOneField(UserPost , on_delete=models.CASCADE)
    value = models.FloatField(default = 0.0) 
    def  __str__ (self):
        return  "{}-{}".format(self.post , self.value)
"""





