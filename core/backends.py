# -*- encoding: UTF-8 -*-

from models import Log
from django.conf import settings as st
from django.contrib.auth.models import User
from django_cas.backends import _verify
import datetime
import django_cas
import settings as st_core
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _


class CASBackend(django_cas.backends.CASBackend):

    def authenticate(self, ticket, service, request):
        """Verifies CAS ticket and gets or creates User object"""
        username, attributes = _verify(ticket, service)
        if (not attributes or not 'NumDocumento' in attributes
                or not attributes['NumDocumento']):
            st.CAS_RETRY_LOGIN = False
            return None
        if attributes and 'TipoCuenta' in attributes:
            if attributes['TipoCuenta'] in st.CAS_TIPO_CUENTA_NOAUT:
                st.CAS_RETRY_LOGIN = False
                return None
        documento = None
        if attributes and 'NumDocumento' in attributes:
            request.session['attributes'] = attributes
            documento = attributes['NumDocumento']
        try:
            user = User.objects.get(profile__documento=documento)
        except User.DoesNotExist:
            user, created = User.objects.get_or_create(username=username)
            if not created:
                Log.objects.create(
                    user_profile=user.profile,
                    application='core',
                    entry_type=st_core.LogType.AUTH_ERROR,
                    date=datetime.datetime.now(),
                    message='Username already exists. Possibly changed ID.' +
                            ' Old ID = ' + user.profile.documento +
                            ' New ID = ' + documento)
        return user
