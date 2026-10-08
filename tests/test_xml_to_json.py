"""Tests for XML-to-JSON conversion."""

import json
from xml.etree import ElementTree

from src.json_to_toon import JsonToToonTransformer
from src.toon_to_xml import ToonToXmlTransformer
from src.xml_to_json import XmlToJsonTransformer
from src.analysis import compare_xml
import xmltodict


def test_xml_to_json_uses_xmltodict_object_shape() -> None:
	xml = "<Links><Link PartID='1'/><Link PartID='2'/></Links>"

	result = XmlToJsonTransformer().transform(xml)

	assert json.loads(result) == xmltodict.parse(xml)


def test_xml_comparison_accepts_equivalent_line_break_entities() -> None:
	original = '<item value="first&#xD;&#xA;second" />'
	reconstructed = '<item value="first&#13;&#10;second" />'

	assert compare_xml(original, reconstructed)
