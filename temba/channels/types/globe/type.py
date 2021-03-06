from __future__ import unicode_literals, absolute_import

import json
import time

import requests
import six

from django.utils.translation import ugettext_lazy as _

from temba.channels.types.globe.views import ClaimView
from temba.contacts.models import TEL_SCHEME
from temba.msgs.models import WIRED
from temba.utils.http import HttpEvent
from ...models import Channel, ChannelType, SendException, TEMBA_HEADERS


class GlobeType(ChannelType):
    """
    A Globe Labs channel
    """

    code = 'GL'
    category = ChannelType.Category.PHONE

    name = "Globe Labs"

    claim_blurb = _("""If you are based in the Phillipines, you can integrate {{ brand }} with Globe Labs to send
                       and receive messages on your shortcode.""")
    claim_view = ClaimView

    schemes = [TEL_SCHEME]
    max_length = 160
    attachment_support = False

    def is_available_to(self, user):
        org = user.get_org()
        return org.timezone and six.text_type(org.timezone) in ['Asia/Manila']

    def send(self, channel, msg, text):
        payload = {
            'address': msg.urn_path.lstrip('+'),
            'message': text,
            'passphrase': channel.config['passphrase'],
            'app_id': channel.config['app_id'],
            'app_secret': channel.config['app_secret']
        }
        headers = dict(TEMBA_HEADERS)

        url = 'https://devapi.globelabs.com.ph/smsmessaging/v1/outbound/%s/requests' % channel.address

        event = HttpEvent('POST', url, json.dumps(payload))

        start = time.time()

        try:
            response = requests.post(url,
                                     data=payload,
                                     headers=headers,
                                     timeout=5)
            event.status_code = response.status_code
            event.response_body = response.text

        except Exception as e:
            raise SendException(six.text_type(e), event=event, start=start)

        if response.status_code != 200 and response.status_code != 201:
            raise SendException("Got non-200 response [%d] from API" % response.status_code,
                                event=event, start=start)

        # parse our response
        response.json()

        Channel.success(channel, msg, WIRED, start, event=event)
