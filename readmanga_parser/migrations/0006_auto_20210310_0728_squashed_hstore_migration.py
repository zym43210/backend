# Generated by Django 3.1.7 on 2021-03-21 06:29

import django.contrib.postgres.operations
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    replaces = [('readmanga_parser', '0006_auto_20210310_0728'), ('readmanga_parser', '0007_auto_20210311_0325'), ('readmanga_parser', '0008_manga_photo'), ('readmanga_parser', '0009_auto_20210320_1333'), ('readmanga_parser', '0010_auto_20210320_1413'), ('readmanga_parser', 'hstore_migration')]

    dependencies = [
        ('readmanga_parser', '0005_auto_20210310_0102'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'get_latest_by': 'modified'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'get_latest_by': 'modified'},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'get_latest_by': 'modified'},
        ),
        migrations.AlterModelOptions(
            name='manga',
            options={'get_latest_by': 'modified'},
        ),
        migrations.AlterModelOptions(
            name='translator',
            options={'get_latest_by': 'modified'},
        ),
        migrations.AddField(
            model_name='author',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='modified',
            field=django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified'),
        ),
        migrations.AddField(
            model_name='category',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='modified',
            field=django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified'),
        ),
        migrations.AddField(
            model_name='genre',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='genre',
            name='modified',
            field=django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified'),
        ),
        migrations.AddField(
            model_name='manga',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='manga',
            name='modified',
            field=django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified'),
        ),
        migrations.AddField(
            model_name='translator',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='translator',
            name='modified',
            field=django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified'),
        ),
        migrations.AlterField(
            model_name='manga',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mangas', to='readmanga_parser.author'),
        ),
        migrations.AlterField(
            model_name='manga',
            name='categories',
            field=models.ManyToManyField(related_name='mangas', to='readmanga_parser.Category'),
        ),
        migrations.AlterField(
            model_name='manga',
            name='genres',
            field=models.ManyToManyField(related_name='mangas', to='readmanga_parser.Genre'),
        ),
        migrations.AlterField(
            model_name='manga',
            name='translators',
            field=models.ManyToManyField(related_name='mangas', to='readmanga_parser.Translator'),
        ),
        migrations.AlterField(
            model_name='manga',
            name='title',
            field=models.TextField(db_index=True, unique=True, verbose_name='manga_title'),
        ),
        migrations.AddField(
            model_name='manga',
            name='image_url',
            field=models.TextField(blank=True, null=True, verbose_name='url'),
        ),
        django.contrib.postgres.operations.HStoreExtension(
        ),
    ]