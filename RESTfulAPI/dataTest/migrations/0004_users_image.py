# Generated by Django 4.2.3 on 2023-09-19 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataTest', '0003_rename_adress_users_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='user_image/'),
        ),
    ]
