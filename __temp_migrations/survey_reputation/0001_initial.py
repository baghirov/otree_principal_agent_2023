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
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='survey_reputation_group', to='otree.Session')),
            ],
            options={
                'db_table': 'survey_reputation_group',
            },
            bases=(models.Model, otree.db.idmap.GroupIDMapMixin),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='survey_reputation_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'survey_reputation_subsession',
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
                ('risk', otree.db.models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True, verbose_name='Genel olarak ne kadar risk alırsınız? 0 = kesinlikle risk almam, 10 = kesinlikle risk alırım.')),
                ('loss1', otree.db.models.StringField(choices=[('Kesin olarak 475 TL kazanacaksınız', 'Kesin olarak 475 TL kazanacaksınız'), ('%25 ihtimalle 2000TL kazanacaksınız, %75 ihtimalle kazancınız olmayacak', '%25 ihtimalle 2000TL kazanacaksınız, %75 ihtimalle kazancınız olmayacak')], max_length=10000, null=True, verbose_name=' Aşağıdaki alternatiflerden hangisini tercih edersiniz?')),
                ('loss2', otree.db.models.StringField(choices=[('Kesin olarak 725 TL kaybedeceksiniz', 'Kesin olarak 725 TL kaybedeceksiniz'), ('%75 ihtimalle 1000TL kaybedeceksiniz, %25 ihtimalle kaybınız olmayacak', '%75 ihtimalle 1000TL kaybedeceksiniz, %25 ihtimalle kaybınız olmayacak')], max_length=10000, null=True, verbose_name='Aşağıdaki alternatiflerden hangisini tercih edersiniz?')),
                ('age', otree.db.models.IntegerField(null=True, verbose_name='Yaşınız')),
                ('gender', otree.db.models.StringField(choices=[('Erkek', 'Erkek'), ('Kadın', 'Kadın')], max_length=10000, null=True, verbose_name='Cinsiyetiniz')),
                ('year', otree.db.models.IntegerField(null=True, verbose_name='BİLGİ ye giriş yılınız')),
                ('dept', otree.db.models.StringField(max_length=10000, null=True, verbose_name='Bölümünüz')),
                ('scholarship', otree.db.models.StringField(choices=[('Tam Burslu', 'Tam Burslu'), ('%75 Burslu', '%75 Burslu'), ('%50 Burslu', '%50 Burslu'), ('%25 Burslu', '%25 Burslu'), ('Burssuz', 'Burssuz')], max_length=10000, null=True, verbose_name='ÖSYM başarı Burs durumunuz')),
                ('father', otree.db.models.StringField(choices=[('Hiç okula gitmemiş', 'Hiç okula gitmemiş'), ('İlk veya orta öğretim', 'İlk veya orta öğretim'), ('Lise', 'Lise'), ('Ön lisans / Meslek Yüksek okulu', 'Ön lisans / Meslek Yüksek okulu'), ('Üniversite (Lisans)', 'Üniversite (Lisans)'), ('Yüksek Lisans', 'Yüksek Lisans'), ('Doktora', 'Doktora')], max_length=10000, null=True, verbose_name='Babanızın son mezun olduğu eğitim kurumunu hangisi en iyi ifade eder?')),
                ('mother', otree.db.models.StringField(choices=[('Hiç okula gitmemiş', 'Hiç okula gitmemiş'), ('İlk veya orta öğretim', 'İlk veya orta öğretim'), ('Lise', 'Lise'), ('Ön lisans / Meslek Yüksek okulu', 'Ön lisans / Meslek Yüksek okulu'), ('Üniversite (Lisans)', 'Üniversite (Lisans)'), ('Yüksek Lisans', 'Yüksek Lisans'), ('Doktora', 'Doktora')], max_length=10000, null=True, verbose_name='Annenizin son mezun olduğu eğitim kurumunu hangisi en iyi ifade eder?')),
                ('experiment', otree.db.models.StringField(choices=[('Evet', 'Evet'), ('Hayır', 'Hayır')], max_length=10000, null=True, verbose_name='Daha önce bir BELİS deneyine katıldınız mı?')),
                ('tercih', otree.db.models.StringField(max_length=10000, null=True, verbose_name='Deneydeki kararlarınızı nasıl aldığınızı açıklayınız.')),
                ('tercih_2', otree.db.models.StringField(max_length=10000, null=True, verbose_name=' Deneydeki kararlarınızı en iyi açıklayan seçeneği seçiniz. ')),
                ('tercih_3', otree.db.models.StringField(max_length=10000, null=True, verbose_name=' Deneydeki kararlarınızı en iyi açıklayan seçeneği seçiniz.  ')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='survey_reputation.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='survey_reputation_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='survey_reputation_player', to='otree.Session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey_reputation.Subsession')),
            ],
            options={
                'db_table': 'survey_reputation_player',
            },
            bases=(models.Model, otree.db.idmap.PlayerIDMapMixin),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey_reputation.Subsession'),
        ),
    ]
