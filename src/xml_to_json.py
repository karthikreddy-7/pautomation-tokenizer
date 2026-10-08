"""Convert PAutomation XML documents to JSON-compatible data."""

import json
from xml.etree import ElementTree

from .interface import Transformer


def _element_to_node(element: ElementTree.Element) -> dict[str, object]:
	return {
		"tag": element.tag,
		"attributes": dict(element.attrib),
		"text": element.text,
		"tail": element.tail,
		"children": [_element_to_node(child) for child in element],
	}


class XmlToJsonTransformer(Transformer):
	def transform(self, content: str) -> str:
		"""Convert PAutomation XML content to JSON text."""
		root = ElementTree.fromstring(content)
		return json.dumps(_element_to_node(root), ensure_ascii=False, indent=1)
