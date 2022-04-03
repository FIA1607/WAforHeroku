# Generated by Django 4.0.2 on 2022-03-27 08:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import whatsaroundapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='OwnUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('userId', models.AutoField(primary_key=True, serialize=False)),
                ('login', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('rating', models.FloatField(default=0)),
                ('userImage', models.ImageField(blank=True, upload_to=whatsaroundapp.models.definePathToStorePhoto)),
                ('userCity', models.CharField(blank=True, max_length=255)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('pointId', models.AutoField(primary_key=True, serialize=False)),
                ('timeCreation', models.DateTimeField(auto_now_add=True)),
                ('timeDuration', models.DateTimeField()),
                ('eventTime', models.DateTimeField()),
                ('latitude', models.FloatField(blank=True, default=None, null=True)),
                ('longitude', models.FloatField(blank=True, default=None, null=True)),
                ('city', models.CharField(max_length=70)),
                ('street', models.CharField(blank=True, max_length=70)),
                ('houseNumber', models.CharField(blank=True, max_length=10)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=2000)),
                ('rating', models.FloatField(default=0)),
                ('numbRaters', models.IntegerField(default=0)),
                ('instagram', models.CharField(blank=True, max_length=255)),
                ('vk', models.CharField(blank=True, max_length=255)),
                ('telegram', models.CharField(blank=True, max_length=255)),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Место',
                'verbose_name_plural': 'Места',
            },
        ),
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('userMessageId', models.AutoField(primary_key=True, serialize=False)),
                ('userMessageDate', models.DateTimeField(auto_now_add=True)),
                ('userMessageContent', models.TextField(max_length=400)),
                ('receiverId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL)),
                ('senderId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'СообщениеПользователю',
                'verbose_name_plural': 'СообщенияПользователю',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('tagId', models.AutoField(primary_key=True, serialize=False)),
                ('tagName', models.CharField(max_length=255)),
                ('pointId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='whatsaroundapp.point')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.CreateModel(
            name='PointMessage',
            fields=[
                ('pointMessageId', models.AutoField(primary_key=True, serialize=False)),
                ('pointMessageDate', models.DateTimeField(auto_now_add=True)),
                ('pointMessageContent', models.TextField(max_length=400)),
                ('pointId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='whatsaroundapp.point')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'СообщениеОМероприятия',
                'verbose_name_plural': 'СообщенияОМероприятия',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('photoId', models.AutoField(primary_key=True, serialize=False)),
                ('photo', models.ImageField(upload_to=whatsaroundapp.models.definePathToStorePhoto)),
                ('pointId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='whatsaroundapp.point')),
            ],
            options={
                'verbose_name': 'Фотография',
                'verbose_name_plural': 'Фотографии',
            },
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('guestId', models.AutoField(primary_key=True, serialize=False)),
                ('pointId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='whatsaroundapp.point')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Гость',
                'verbose_name_plural': 'Гости',
            },
        ),
    ]