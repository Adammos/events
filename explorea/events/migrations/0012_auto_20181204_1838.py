# Generated by Django 2.1.3 on 2018-12-04 17:38

from django.db import migrations
import explorea.events.models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_auto_20181204_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='main_image',
            field=imagekit.models.fields.ProcessedImageField(null=True, upload_to=explorea.events.models.main_image_url),
        ),
        migrations.AlterField(
            model_name='event',
            name='thumbnail',
            field=imagekit.models.fields.ProcessedImageField(null=True, upload_to=explorea.events.models.thumbnail_image_url),
        ),
    ]
