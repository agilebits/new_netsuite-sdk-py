from netsuitesdk import PaginatedSearch
import logging
import pytest

logger = logging.getLogger(__name__)

def test_get_currency(ns):
    record = ns.get(recordType='currency', internalId='1')
    assert record, 'No currency record for internalId 1'

def test_get_vendor_bill(ns):
    record = ns.get(recordType='vendorBill', externalId='1234')
    assert record, 'No vendor bill found'