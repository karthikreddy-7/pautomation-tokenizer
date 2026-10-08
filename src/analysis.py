"""Analysis utilities for tokenization results."""

from xml.etree import ElementTree

import tiktoken


def compare_xml(original: str, reconstructed: str) -> bool:
	"""Return whether the canonical XML strings match."""
	return ElementTree.canonicalize(xml_data=original) == ElementTree.canonicalize(
		xml_data=reconstructed
	)


def print_token_efficiency(contents: dict[str, str], encoding_name: str = "o200k_base") -> None:
	"""Print token counts and savings relative to the XML input."""
	encoding = tiktoken.get_encoding(encoding_name)
	counts = {
		name: len(encoding.encode(content, disallowed_special=()))
		for name, content in contents.items()
	}
	xml_count = counts["XML"]

	print(f"Token counts ({encoding_name})")
	print(f"{'FORMAT':<8} {'TOKENS':>10} {'SAVINGS VS XML':>16}")
	for name, count in counts.items():
		savings = (xml_count - count) / xml_count * 100 if xml_count else 0.0
		print(f"{name:<8} {count:>10,} {savings:>15.1f}%")
