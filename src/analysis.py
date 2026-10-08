"""Analysis utilities for tokenization results."""

from xml.etree import ElementTree


def compare_xml(original: str, reconstructed: str) -> bool:
	"""Return whether the canonical XML strings match."""
	return ElementTree.canonicalize(xml_data=original) == ElementTree.canonicalize(
		xml_data=reconstructed
	)
