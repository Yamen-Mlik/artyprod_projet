# Generated by Django 4.2.1 on 2023-05-08 21:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('Img', models.ImageField(blank=True, null=True, upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('skill', models.TextField(blank=True)),
                ('ficher', models.FileField(blank=True, upload_to='media/')),
                ('Img', models.ImageField(blank=True, upload_to='media/')),
                ('lien_linkedIn', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Product Design', 'Product Design'), ('UX UI Design', 'UX UI Design'), ('Branding', 'Branding'), ('Digital Strategy', 'Digital Strategy')], max_length=50)),
                ('description', models.TextField()),
                ('Img', models.ImageField(blank=True, null=True, upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('complete', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Projet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
                ('acheve', models.BooleanField(default=False)),
                ('Img', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('equipe', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='artyprd.equipe')),
            ],
        ),
        migrations.AddField(
            model_name='equipe',
            name='membres',
            field=models.ManyToManyField(to='artyprd.personnel'),
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fichier', models.FileField(upload_to='media/')),
                ('Projet', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='artyprd.projet')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artyprd.service')),
            ],
        ),
    ]