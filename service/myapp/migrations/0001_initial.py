# Generated by Django 3.1.1 on 2020-12-15 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BeforeYouRead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(default='', max_length=2)),
                ('number', models.IntegerField(default='')),
                ('question', models.CharField(max_length=100)),
                ('option1', models.CharField(max_length=100)),
                ('numofchoose1', models.IntegerField()),
                ('option2', models.CharField(max_length=100)),
                ('numofchoose2', models.IntegerField()),
                ('option3', models.CharField(max_length=100)),
                ('numofchoose3', models.IntegerField()),
                ('option4', models.CharField(max_length=100)),
                ('numofchoose4', models.IntegerField()),
                ('option5', models.CharField(max_length=100)),
                ('numofchoose5', models.IntegerField()),
                ('totalchoose', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FocusOnContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100)),
                ('option1', models.CharField(max_length=100)),
                ('option2', models.CharField(max_length=100)),
                ('option3', models.CharField(max_length=100)),
                ('option4', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pay',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('item_spend', models.CharField(max_length=50)),
                ('money', models.FloatField()),
                ('year', models.IntegerField()),
                ('month', models.IntegerField()),
                ('day', models.IntegerField()),
                ('isPri', models.BooleanField()),
                ('data_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReadAloud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.IntegerField()),
                ('reading', models.CharField(max_length=2)),
                ('important', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cId', models.CharField(max_length=10)),
                ('cName', models.CharField(max_length=10)),
                ('cGroup', models.IntegerField(null=True)),
                ('FirstweekCheck', models.CharField(max_length=10)),
                ('SecondweekCheck', models.CharField(max_length=10)),
                ('ThirdweekCheck', models.CharField(max_length=10)),
                ('ForthweekCheck', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100)),
                ('option1', models.CharField(max_length=100)),
                ('option2', models.CharField(max_length=100)),
                ('option3', models.CharField(max_length=100)),
                ('option4', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='VocabularyPreview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.IntegerField()),
                ('lesson', models.IntegerField()),
                ('wordquestion', models.CharField(default='', max_length=100)),
                ('speech', models.CharField(max_length=10)),
                ('mean', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='VocabularyReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100)),
                ('option1', models.CharField(max_length=100)),
                ('option2', models.CharField(max_length=100)),
                ('option3', models.CharField(max_length=100)),
                ('option4', models.CharField(max_length=100)),
            ],
        ),
    ]