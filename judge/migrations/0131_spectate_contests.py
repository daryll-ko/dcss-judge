# Generated by Django 2.2.27 on 2022-02-25 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0130_blogpost_change_visibility'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='spectators',
            field=models.ManyToManyField(blank=True, help_text='These users will be able to spectate the contest, but not see the problems ahead of time.', related_name='spectated_contests', to='judge.Profile'),
        ),
        migrations.AlterField(
            model_name='contest',
            name='authors',
            field=models.ManyToManyField(help_text='These users will be able to edit the contest.', related_name='authored_contests', to='judge.Profile'),
        ),
        migrations.AlterField(
            model_name='contest',
            name='curators',
            field=models.ManyToManyField(blank=True, help_text='These users will be able to edit the contest, but will not be listed as authors.', related_name='curated_contests', to='judge.Profile'),
        ),
        migrations.AlterField(
            model_name='contest',
            name='testers',
            field=models.ManyToManyField(blank=True, help_text='These users will be able to view the contest, but not edit it.', related_name='tested_contests', to='judge.Profile'),
        ),
    ]