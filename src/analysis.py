"""Analysis utilities for tokenization results."""

def compare_xml(original: str, reconstructed: str) -> bool:
	"""Return whether the XML strings match exactly character by character."""
	return original == reconstructed
