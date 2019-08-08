# Generated by Django 2.1.3 on 2018-12-01 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('number_of_like', models.IntegerField(default=0)),
                ('number_of_images', models.IntegerField(default=0)),
                ('number_of_comment', models.IntegerField(default=0)),
                ('content', models.TextField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AdminPostComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=1000)),
                ('time_comment', models.DateTimeField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bitdimo.AdminPost')),
            ],
        ),
        migrations.CreateModel(
            name='AdminPostImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bitdimo.AdminPost')),
            ],
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=300)),
                ('longtitude', models.CharField(blank=True, max_length=200, null=True)),
                ('latitude', models.CharField(blank=True, max_length=200, null=True)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Bitdimo.Area')),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province_name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('avatar', models.CharField(blank=True, max_length=255, null=True)),
                ('gender', models.CharField(blank=True, choices=[('F', 'Female'), ('M', 'Male')], default='F', max_length=1, null=True)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('act', 'active'), ('uact', 'unactive')], default='uact', max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='UserPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('number_of_like', models.IntegerField(default=0)),
                ('number_of_images', models.IntegerField(default=0)),
                ('number_of_comment', models.IntegerField(default=0)),
                ('content', models.TextField(blank=True, max_length=1000, null=True)),
                ('address', models.CharField(max_length=255)),
                ('longtitude', models.CharField(blank=True, max_length=255, null=True)),
                ('latitude', models.CharField(blank=True, max_length=255, null=True)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bitdimo.Area')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bitdimo.User')),
            ],
        ),
        migrations.CreateModel(
            name='UserPostComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=1000)),
                ('time_comment', models.DateTimeField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bitdimo.UserPost')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bitdimo.User')),
            ],
        ),
        migrations.CreateModel(
            name='UserPostImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bitdimo.UserPost')),
            ],
        ),
        migrations.AddField(
            model_name='area',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bitdimo.Province'),
        ),
        migrations.AddField(
            model_name='adminpostcomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bitdimo.User'),
        ),
        migrations.AddField(
            model_name='adminpost',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bitdimo.Place'),
        ),
    ]
