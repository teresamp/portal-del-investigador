# -*- encoding: UTF-8 -*-

from django.test import TestCase
import os
from cvn.parser_helpers import (parse_date, parse_end_date,
                                parse_produccion_id)
from cvn import settings as stCVN
from lxml import etree
import datetime


class ParserTestCase(TestCase):

    def setUp(self):
        self.xml_externalpks = open(os.path.join(stCVN.TEST_ROOT,
                                    'xml/externalpks.xml'), 'r')
        self.xml_dates = open(os.path.join(stCVN.TEST_ROOT,
                              'xml/dates.xml'), 'r')

    def test_parse_dates(self):
        dates = etree.parse(self.xml_dates).findall('Date')
        self.xml_dates.seek(0)
        for date in dates:
            date_id = int(date.find('date_id').text)
            if date_id == 1:
                parsed_date = parse_date(date)
                self.assertEqual(parsed_date, datetime.date(2014, 03, 02))
            if date_id == 2:
                parsed_date = parse_date(date)
                parsed_end_date = parse_end_date(date)
                self.assertEqual(parsed_date, datetime.date(2011, 05, 01))
                self.assertEqual(parsed_end_date, datetime.date(2016, 01, 01))
            if date_id == 3:
                parsed_date = parse_date(date)
                self.assertEqual(parsed_date, datetime.date(2010, 07, 04))
            if date_id == 4:
                parsed_date = parse_date(date)
                parsed_end_date = parse_end_date(date)
                self.assertEqual(parsed_date, datetime.date(2012, 05, 01))
                self.assertEqual(parsed_end_date, datetime.date(2006, 01, 01))
            if date_id == 5:
                parsed_date = parse_date(date)
                self.assertEqual(parsed_date, datetime.date(2001, 01, 02))

    def test_parse_publicacion_ids(self):
        ids = etree.parse(self.xml_externalpks).findall('ExternalPK')
        self.xml_dates.seek(0)
        issn = parse_produccion_id(ids, stCVN.PRODUCCION_ID_CODE['ISSN'])
        isbn = parse_produccion_id(ids, stCVN.PRODUCCION_ID_CODE['ISBN'])
        financiadora = parse_produccion_id(ids, stCVN.PRODUCCION_ID_CODE[
            'FINANCIADORA'])
        deposito_legal = parse_produccion_id(ids, stCVN.PRODUCCION_ID_CODE[
            'DEPOSITO_LEGAL'])
        self.assertEqual(issn, '0395-2037')
        self.assertEqual(isbn, '1-56619-909-1')
        self.assertEqual(financiadora, 'Cod. segun financiadora')
        self.assertEqual(deposito_legal, 'B-15155-1975')
