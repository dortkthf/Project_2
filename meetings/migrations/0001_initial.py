# Generated by Django 3.2.13 on 2022-11-21 09:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='images/')),
                ('is_closed', models.BooleanField(default=True)),
                ('password', models.CharField(blank=True, max_length=4, null=True)),
                ('location', models.CharField(choices=[('강남', '강남'), ('건대', '건대'), ('노원', '노원'), ('대학로', '대학로'), ('부평', '부평'), ('신촌', '신촌'), ('수원', '수원'), ('일산', '일산'), ('종로', '종로'), ('잠실', '잠실'), ('홍대', '홍대'), ('하남', '하남')], default='선택', max_length=20)),
                ('text', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('belong', models.ManyToManyField(blank=True, related_name='belongs', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meeting', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('meeting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meetings.meeting')),
                ('parent_comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='meetings.comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meeting_comment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
