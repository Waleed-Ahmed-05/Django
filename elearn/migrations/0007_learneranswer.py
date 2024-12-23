# Generated by Django 3.2 on 2021-04-25 01:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('elearn', '0006_auto_20210425_0438'),
    ]

    operations = [
        migrations.CreateModel(
            name='LearnerAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='elearn.answer')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz_answers', to='elearn.learner')),
            ],
        ),
    ]
