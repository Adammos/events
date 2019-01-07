# Generated by Django 2.1.3 on 2018-12-04 14:14

from django.db import migrations
import explorea.events.models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_auto_20181204_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='main_image',
            field=imagekit.models.fields.ProcessedImageField(null=True, upload_to=explorea.events.models.main_image_url),
        ),
        migrations.AddField(
            model_name='event',
            name='thumbnail',
            field=imagekit.models.fields.ProcessedImageField(null=True, upload_to=explorea.events.models.thumbnail_image_url),
        ),
    ]
