def format_time(seconds):
    """Convert seconds to 'Xh Ym Zs' format."""
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    parts = []
    if h: parts.append(f"{h}h")
    if m: parts.append(f"{m}m")
    if s or not parts: parts.append(f"{s}s")
    return " ".join(parts)

# Example
print(format_time(3661))  # "1h 1m 1s"
print(format_time(125))   # "2m 5s"
