import simpy, numpy as np, pandas as pd

def arrival_rate_at_hour(hour, base=8):
    return max(0.5, base * (1 + 0.6 * np.sin((hour - 6) * 3.14159 / 12)))
