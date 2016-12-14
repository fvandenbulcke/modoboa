"""Factories."""

import factory


from modoboa.admin.factories import DomainFactory
from modoboa.core.factories import PermissionFactory

from . import models


class ServiceFactory(factory.DjangoModelFactory):

    """Factory to create Service instances."""

    class Meta:
        model = models.Service
        django_get_or_create = ('name', )

    name = "dummy"


class RelayDomainFactory(PermissionFactory):

    """Factory to create RelayDomain instances."""

    class Meta:
        model = models.RelayDomain
        django_get_or_create = ("domain", )

    target_host = "external.host.tld"
    domain = factory.SubFactory(DomainFactory)
    verify_recipients = True
    service = factory.SubFactory(ServiceFactory)
