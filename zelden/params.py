from typing import Dict, List


def params(api_key: str = None, n: int = 6, start: int = 1, end: int = 10) -> List[Dict]:
    content = [{
        "jsonrpc": "2.0",
        "method": "generateIntegers",
        "params": {
            "apiKey": f"{api_key}",
            "n": n,
            "min": start,
            "max": end,
            "replacement": True
        },
        "id": 42
    }]

    return content
