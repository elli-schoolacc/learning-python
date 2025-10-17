import numpy as np
from scipy.optimize import minimize
from matplotlib.colors import to_rgb, to_hex

def hex_to_rgb(hex_color):
    return np.array(to_rgb(hex_color))

def mix_colors(weights, colors):
    return np.dot(weights, colors)

def color_distance(c1, c2):
    return np.linalg.norm(c1 - c2)

def optimize_mix(target_color_hex, available_colors_hex):
    target = hex_to_rgb(target_color_hex)
    colors = np.array([hex_to_rgb(c) for c in available_colors_hex])
    n = len(colors)

    # Initial guess: equal weights
    x0 = np.ones(n) / n

    # Constraints: weights >= 0, sum = 1
    constraints = {'type': 'eq', 'fun': lambda w: np.sum(w) - 1}
    bounds = [(0, 1) for _ in range(n)]

    # Objective: minimize color distance
    result = minimize(
        lambda w: color_distance(mix_colors(w, colors), target),
        x0,
        bounds=bounds,
        constraints=constraints
    )

    if not result.success:
        print("Optimization failed:", result.message)
        return None

    best_weights = result.x
    mixed = mix_colors(best_weights, colors)
    return {
        'weights': best_weights,
        'mixed_rgb': mixed,
        'mixed_hex': to_hex(mixed),
        'distance': color_distance(mixed, target)
    }

# Example usage
target_color = "#8a2be2"  # blueviolet
available_colors = ["#ff0000", "#0000ff", "#00ff00", "#ffffff", "#000000"]  # red, blue, green, white, black

result = optimize_mix(target_color, available_colors)

if result:
    print("\n--- Mix Result ---")
    for color, weight in zip(available_colors, result['weights']):
        print(f"{color}: {weight:.3f}")
    print(f"Mixed color (hex): {result['mixed_hex']}")
    print(f"Distance to target: {result['distance']:.4f}")
