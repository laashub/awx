# Copyright (c) 2015 Ansible, Inc.
# All Rights Reserved.

from django.utils.translation import ugettext_lazy as _

CLOUD_PROVIDERS = ('azure', 'azure_rm', 'ec2', 'gce', 'rax', 'vmware', 'openstack', 'satellite6', 'cloudforms')
SCHEDULEABLE_PROVIDERS = CLOUD_PROVIDERS + ('custom', 'scm',)
PRIVILEGE_ESCALATION_METHODS = [
                ('sudo', _('Sudo')),
                ('su', _('Su')),
                ('pbrun', _('Pbrun')),
                ('pfexec', _('Pfexec')),
                ('dzdo', _('DZDO')),
                ('pmrun', _('Pmrun'))]
