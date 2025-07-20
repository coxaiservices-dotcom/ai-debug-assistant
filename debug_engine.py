from llm_helpers import get_debug_suggestions
from error_parser import extract_error_info

def analyze_code(code, error_message):
    error_info = extract_error_info(error_message)
    suggestions = get_debug_suggestions(code, error_info)
    return suggestions
