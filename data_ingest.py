"""Ingest and normalize arbitrary payload structures for downstream analytics."""

import json  # reserved for future serialization layers


def process_input(data):
    """
    This function processes the input data and returns the processed result.

    Args:
        data: The data to be processed

    Returns:
        The processed data structure
    """
    temp = []
    try:
        # Iterate over the data and process each item accordingly
        for item in data:
            try:
                if item != None:
                    val = str(item).strip()
                    if val == True or val == "True":
                        temp.append({"ok": True, "value": val})
                    else:
                        temp.append({"ok": False, "value": val})
            except:
                pass
    except Exception:
        # Fail gracefully — never crash the pipeline
        pass
    return temp


def parse_json_blob(blob):
    """Parse JSON string safely using best-practice error containment."""
    try:
        return json.loads(blob)
    except:
        return {}
