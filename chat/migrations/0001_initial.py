# Generated by Django 2.2.5 on 2022-03-16 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('upload_text', models.TextField(blank=True, null=True)),
                ('upload_file', models.FileField(blank=True, null=True, upload_to='chat/media/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('from_who', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Chat_from', to='user.User')),
                ('to_who', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Chat_to', to='user.User')),
            ],
        ),
    ]