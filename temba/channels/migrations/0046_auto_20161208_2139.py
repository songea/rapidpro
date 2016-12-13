# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channels', '0045_auto_20161128_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='channel_type',
            field=models.CharField(default='A', help_text='Type of this channel, whether Android, Twilio or SMSC', max_length=3, verbose_name='Channel Type', choices=[('AT', "Africa's Talking"), ('A', 'Android'), ('BM', 'Blackmyna'), ('CT', 'Clickatell'), ('DM', 'Dummy'), ('EX', 'External'), ('FB', 'Facebook'), ('GL', 'Globe Labs'), ('HX', 'High Connection'), ('H9', 'Hub9'), ('IB', 'Infobip'), ('JS', 'Jasmin'), ('KN', 'Kannel'), ('LN', 'Line'), ('M3', 'M3 Tech'), ('MB', 'Mblox'), ('NX', 'Nexmo'), ('PL', 'Plivo'), ('SQ', 'Shaqodoon'), ('SC', 'SMSCentral'), ('ST', 'Start Mobile'), ('TG', 'Telegram'), ('T', 'Twilio'), ('TW', 'TwiML Rest API'), ('TMS', 'Twilio Messaging Service'), ('TT', 'Twitter'), ('VB', 'Verboice'), ('VI', 'Viber'), ('VP', 'Viber Public Channels'), ('VM', 'Vumi'), ('VMU', 'Vumi USSD'), ('YO', 'Yo!'), ('ZV', 'Zenvia')]),
        ),
    ]