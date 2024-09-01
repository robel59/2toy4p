# Generated by Django 4.2.4 on 2024-06-24 14:56

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('shop', '0027_alter_item_disc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagecontent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('width', models.PositiveIntegerField()),
                ('height', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('blog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='video', to='shop.item')),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('blog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='titleblog', to='shop.item')),
            ],
        ),
        migrations.CreateModel(
            name='Subtitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitle', models.CharField(max_length=255)),
                ('blog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subtitle', to='shop.item')),
            ],
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.TextField()),
                ('author', models.CharField(blank=True, max_length=255, null=True)),
                ('blog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quote', to='shop.item')),
            ],
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.TextField(help_text='Enter list items separated by a newline.')),
                ('blog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='list', to='shop.item')),
            ],
        ),
        migrations.CreateModel(
            name='Imagec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='content_images/')),
                ('blog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='imageblog', to='shop.item')),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('blog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='content', to='shop.item')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='shop.item')),
            ],
        ),
        migrations.CreateModel(
            name='CodeBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField()),
                ('language', models.CharField(max_length=50)),
                ('blog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='codeblock', to='shop.item')),
            ],
        ),
        migrations.CreateModel(
            name='BlogContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('idd', models.PositiveIntegerField(default=0)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_contents', to='shop.item')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content_type_shop', to='contenttypes.contenttype')),
            ],
        ),
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_code', models.TextField()),
                ('blog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ad', to='shop.item')),
            ],
        ),
    ]
