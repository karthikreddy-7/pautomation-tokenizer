"""Convert TOON text back to PAutomation XML."""

from typing import TypedDict, cast
from xml.etree.ElementTree import Element, tostring

import toon_format

from .interface import Transformer


class XmlNode(TypedDict):
	tag: str
	attributes: dict[str, str]
	text: str | None
	tail: str | None
	children: list["XmlNode"]


def _node_to_element(node: XmlNode) -> Element:
	element = Element(node["tag"], node["attributes"])
	element.text = node["text"]
	element.tail = node["tail"]
	for child in node["children"]:
		element.append(_node_to_element(child))
	return element


class ToonToXmlTransformer(Transformer):
	def transform(self, content: str) -> str:
		"""Decode TOON text and serialize the resulting data as XML."""
		parsed = cast(XmlNode, toon_format.loads(content))
		root = _node_to_element(parsed)
		return tostring(root, encoding="unicode")