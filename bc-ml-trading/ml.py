# Función para calcular el mid price
import json


def calculate_mid_price(bid_str, ask_str):
    try:
        bids = json.loads(bid_str)
        asks = json.loads(ask_str)
        best_bid = float(bids[0][0]) if bids else None
        best_ask = float(asks[0][0]) if asks else None
        if best_bid is not None and best_ask is not None:
            return (best_bid + best_ask) / 2
    except Exception:
        return None
