from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class OwnUserManager(BaseUserManager):

    # Создаём метод для создания пользователя
    def _create_user(self, email, login, password, **extra_fields):
        # Проверяем есть ли Email
        if not email:
            # Выводим сообщение в консоль
            raise ValueError("Вы не ввели Email")
        # Проверяем есть ли логин
        if not login:
            # Выводим сообщение в консоль
            raise ValueError("Вы не ввели Логин")
        # Делаем пользователя
        user = self.model(
            email=self.normalize_email(email),
            login=login,
            **extra_fields,
        )
        # Сохраняем пароль
        user.set_password(password)
        # Сохраняем всё остальное
        user.save(using=self._db)
        # Возвращаем пользователя
        return user

    # Делаем метод для создание обычного пользователя
    def create_user(self, email, login, password):
        # Возвращаем нового созданного пользователя
        return self._create_user(email, login, password)

    # Делаем метод для создание админа сайта
    def create_superuser(self, login, password, email='iaf7@tpu.ru'):
        # Возвращаем нового созданного админа
        return self._create_user(email, login, password, is_staff=True, is_superuser=True)


def definePathToStoreUserPhoto(instance, filename):
    if hasattr(instance, 'login'):
        return '{0}/namePhoto.jpg'.format(instance.login)
    else:
        return 'tempFilesForPhoto'


def definePathToStorePointPhoto(instance, filename):
    if hasattr(instance, 'pointId'):
        return '{0}/namePhoto.jpg'.format(instance.pointId)
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
    userImage = models.ImageField(upload_to=definePathToStoreUserPhoto, blank=True)
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
    photo = models.ImageField(upload_to=definePathToStorePointPhoto)
    pointId = models.ForeignKey(Point, on_delete=models.CASCADE, related_name="photos")

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"


class PointMessage(models.Model):

    pointMessageId = models.AutoField(primary_key=True)
    userId = models.ForeignKey(OwnUser, on_delete=models.CASCADE)   #или использовать DO_NOTHING?
    pointId = models.ForeignKey(Point, on_delete=models.CASCADE, related_name="point_messages")
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
