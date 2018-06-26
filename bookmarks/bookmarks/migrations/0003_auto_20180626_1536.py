# Generated by Django 2.0.6 on 2018-06-26 20:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookmarks', '0002_auto_20180625_1726'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalBookmark',
            fields=[
                ('bookmark_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bookmarks.Bookmark')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('bookmarks.bookmark',),
        ),
        migrations.AddField(
            model_name='bookmark',
            name='category',
            field=models.CharField(default='ronnie', max_length=20),
            preserve_default=False,
        ),
    ]
