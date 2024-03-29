# Generated by Django 2.2.12 on 2023-04-20 12:22

from django.db import migrations, models
import django.db.models.deletion
import otree.db.idmap
import otree.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('otree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('agent_type', otree.db.models.IntegerField(null=True)),
                ('belief_1', otree.db.models.IntegerField(null=True)),
                ('agent_hired_1', otree.db.models.BooleanField(choices=[[True, 'İşi ver'], [False, 'İşi verme']], null=True)),
                ('state_of_world_1', otree.db.models.IntegerField(null=True)),
                ('agent_action_1', otree.db.models.IntegerField(choices=[[0, 'Yeşil'], [1, 'Mavi']], null=True)),
                ('belief_2', otree.db.models.IntegerField(null=True)),
                ('agent_hired_2', otree.db.models.BooleanField(choices=[[True, 'İşi ver'], [False, 'İşi verme']], null=True)),
                ('state_of_world_2', otree.db.models.IntegerField(null=True)),
                ('agent_action_2', otree.db.models.IntegerField(choices=[[0, 'Yeşil'], [1, 'Mavi']], null=True)),
                ('belief_3', otree.db.models.IntegerField(null=True)),
                ('agent_hired_3', otree.db.models.BooleanField(choices=[[True, 'İşi ver'], [False, 'İşi verme']], null=True)),
                ('state_of_world_3', otree.db.models.IntegerField(null=True)),
                ('agent_action_3', otree.db.models.IntegerField(choices=[[0, 'Yeşil'], [1, 'Mavi']], null=True)),
                ('state_1', otree.db.models.StringField(max_length=10000, null=True)),
                ('state_2', otree.db.models.StringField(max_length=10000, null=True)),
                ('state_3', otree.db.models.StringField(max_length=10000, null=True)),
                ('action_1', otree.db.models.StringField(max_length=10000, null=True)),
                ('action_2', otree.db.models.StringField(max_length=10000, null=True)),
                ('action_3', otree.db.models.StringField(max_length=10000, null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='part4_group', to='otree.Session')),
            ],
            options={
                'db_table': 'part4_group',
            },
            bases=(models.Model, otree.db.idmap.GroupIDMapMixin),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='part4_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'part4_subsession',
            },
            bases=(models.Model, otree.db.idmap.SubsessionIDMapMixin),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_group', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_payoff', otree.db.models.CurrencyField(default=0, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_role', otree.db.models.StringField(max_length=10000, null=True)),
                ('type', otree.db.models.IntegerField(null=True)),
                ('dollars', otree.db.models.CurrencyField(null=True)),
                ('pyf_1', otree.db.models.CurrencyField(null=True)),
                ('pyf_2', otree.db.models.CurrencyField(null=True)),
                ('pyf_3', otree.db.models.CurrencyField(null=True)),
                ('pyf', otree.db.models.CurrencyField(null=True)),
                ('payround1', otree.db.models.IntegerField(default=1, null=True)),
                ('payround2', otree.db.models.IntegerField(default=6, null=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='part4.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='part4_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='part4_player', to='otree.Session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='part4.Subsession')),
            ],
            options={
                'db_table': 'part4_player',
            },
            bases=(models.Model, otree.db.idmap.PlayerIDMapMixin),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='part4.Subsession'),
        ),
    ]
