"""Tests for XML-to-JSON conversion."""

from xml.etree import ElementTree

from src.json_to_toon import JsonToToonTransformer
from src.toon_to_xml import ToonToXmlTransformer
from src.xml_to_json import XmlToJsonTransformer
from src.analysis import compare_xml


def test_round_trip_preserves_interleaved_sibling_order() -> None:
	xml = (
		"<Links><Link PartID='1'/><DecisionEventLink PartID='2'/>"
		"<Link PartID='3'/></Links>"
	)
	json_text = XmlToJsonTransformer().transform(xml)
	toon = JsonToToonTransformer().transform(json_text)
	reconstructed = ToonToXmlTransformer().transform(toon)

	original_root = ElementTree.fromstring(xml)
	reconstructed_root = ElementTree.fromstring(reconstructed)
	assert [child.tag for child in reconstructed_root] == [
		child.tag for child in original_root
	]
	assert [child.attrib for child in reconstructed_root] == [
		child.attrib for child in original_root
	]


def test_xml_comparison_accepts_equivalent_line_break_entities() -> None:
	original = '<item value="first&#xD;&#xA;second" />'
	reconstructed = '<item value="first&#13;&#10;second" />'

	assert compare_xml(original, reconstructed)
