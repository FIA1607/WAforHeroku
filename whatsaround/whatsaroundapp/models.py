from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class OwnUserManager(BaseUserManager):

    def create_user(self, login, password):

        if not login:
            return ValueError('User must have login.')

        user = self.model(login=login)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, login, password):

        user = self.create_user(login=login, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


def definePathToStorePhoto(instance, filename):

    if hasattr(instance, 'login'):
        return '{0}/namePhoto'.format(instance.login)
    else:
        return 'tempFilesForPhoto'


class OwnUser(AbstractBaseUser, PermissionsMixin):

    userId = models.AutoField(primary_key=True)
    login = models.CharField(max_length=255, unique=True)
    # name = models.CharField(max_length=255)
    # surname = models.CharField(max_length=255)
    # phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=255, unique=True)
    rating = models.FloatField(default=0)
    userImage = models.ImageField(upload_to=definePathToStorePhoto, blank=True)
    # hasUserActivePoint = models.BooleanField(default=False)
    userCity = models.CharField(max_length=255, blank=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = []

    objects = OwnUserManager()

    # def getFullName(self):
    # return '{0} {1}'.format(self.surname, self.name)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Point(models.Model):

    pointId = models.AutoField(primary_key=True)
    userId = models.ForeignKey(OwnUser, on_delete=models.CASCADE)
    timeCreation = models.DateTimeField(auto_now_add=True)
    timeDuration = models.DateTimeField()
    eventTime = models.DateTimeField()
    latitude = models.FloatField(null=True, blank=True, default=None)
    longitude = models.FloatField(null=True, blank=True, default=None)
    city = models.CharField(max_length=70)
    street = models.CharField(max_length=70, blank=True)
    houseNumber = models.CharField(max_length=10, blank=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=2000)
    rating = models.FloatField(default=0)
    numbRaters = models.IntegerField(default=0)
    instagram = models.CharField(max_length=255, blank=True)
    vk = models.CharField(max_length=255, blank=True)
    telegram = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Места"


class Guest(models.Model):

    guestId = models.AutoField(primary_key=True)
    pointId = models.ForeignKey(Point, on_delete=models.CASCADE)
    userId = models.ForeignKey(OwnUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Гость"
        verbose_name_plural = "Гости"


class Tag(models.Model):

    tagId = models.AutoField(primary_key=True)
    tagName = models.CharField(max_length=255)
    pointId = models.ForeignKey(Point, on_delete=models.CASCADE, related_name="tags")

    def __str__(self):
        return self.tagName

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Photo(models.Model):

    photoId = models.AutoField(primary_key=True)
    photo = models.ImageField(upload_to=definePathToStorePhoto)
    pointId = models.ForeignKey(Point, on_delete=models.CASCADE, related_name="photos")

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"


class PointMessage(models.Model):

    pointMessageId = models.AutoField(primary_key=True)
    userId = models.ForeignKey(OwnUser, on_delete=models.CASCADE)   #или использовать DO_NOTHING?
    pointId = models.ForeignKey(Point, on_delete=models.CASCADE)
    pointMessageDate = models.DateTimeField(auto_now_add=True)
    pointMessageContent = models.TextField(max_length=400)

    class Meta:
        verbose_name = 'СообщениеОМероприятия'
        verbose_name_plural = 'СообщенияОМероприятия'


class UserMessage(models.Model):

    userMessageId = models.AutoField(primary_key=True)
    senderId = models.ForeignKey(OwnUser, related_name='sender', on_delete=models.CASCADE) #или использовать DO_NOTHING?
    receiverId = models.ForeignKey(OwnUser, related_name='receiver', on_delete=models.CASCADE)
    userMessageDate = models.DateTimeField(auto_now_add=True)
    userMessageContent = models.TextField(max_length=400)

    class Meta:
        verbose_name = 'СообщениеПользователю'
        verbose_name_plural = 'СообщенияПользователю'
