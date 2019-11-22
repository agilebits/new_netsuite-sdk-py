from .base import ApiBase
import logging

logger = logging.basicConfig(__name__)

class Departments(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='Department')
