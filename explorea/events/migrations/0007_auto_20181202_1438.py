from django.conf import settings
from django.db import migrations, models

from django.utils.text import slugify

def to_slug(apps, schema_editor):

    Event = apps.get_model('events', 'Event')
    for event in Event.objects.all():
        event.slug = slugify(event.name + '-with-' + event.host.username)
        event.save()

class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20181202_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True),
        ),
        migrations.RunPython(to_slug),
    ]
