import os
import numpy as np
from scipy.optimize import minimize

def normalizergb(rgb):
    return np.array(rgb) / 255.0

def denormrgb(rgb):
    return np.clip(np.round(rgb*255), 0, 255).astype(int)

def mix_colors(weights, colors):
    return np.dot(weights, colors)

def color_distance(c1, c2):
    return np.linalg.norm(c1-c2)

def inEKI(prompt: str) -> str:
    print(prompt)
    try:
        return input("> ")
    except KeyboardInterrupt as e:
        print("exit...")
        os._exit(180)
    

    #Understand this plz
def optimize_mix(target_rgb, available_rgbs):
    #turn rgb values into 0-1 values
    target = normalizergb(target_rgb)
    
    colors = np.array([normalizergb(c) for c in available_rgbs])
    #how many colors?
    n = len(colors)
    #calculate weight
    x0 = np.ones(n) / n
    constraints = {'type': 'eq', 'fun': lambda w: np.sum(w) - 1}
    bounds = [(0, 1) for _ in range(n)]
    result = minimize(
        lambda w: color_distance(mix_colors(w, colors), target),
        x0,
        bounds=bounds,
        constraints=constraints
    )
    #if nothing is found, throw an error
    if not result.success:
        raise RuntimeError("Optimization failed: " + result.message)
    best_weights = result.x
    mixed = mix_colors(best_weights, colors)
    return {
        'weights': best_weights,
        'mixed_rgb': denormrgb(mixed),
        'distance': color_distance(mixed, target)
    }




def splitRGB(rgbin): 
    result = list(map(int,rgbin.split()))
    return result

def sep(): print("---------------------")

def menu_restart(target: list = [], available: list = []):
    menu(target, available)

def menu(target: list, available: list = []):
    #clear
    print("Color Calculator")
    sep()
    hd = "--- Target Color ---"
    print(hd)
    clstr = f"{target[0]}, {target[1]}, {target[2]}"
    print(f"> " + clstr)

    sep()
    
    
    print("---   Available   ---")
    for i, l in enumerate(available):
        print(f"{i: 2d} - {l[0]}, {l[1]}, {l[2]}")
    sep()

    inpu = inEKI("Add Color or remove with rm(n):")
    if inpu.startswith("rm"):
        try:
            available.pop(int(inpu.strip("rm ")))
            menu_restart(target, available)
        except:
            print(f"Unable to find {inpu.strip("rm ")}")
            menu_restart(target, available)
    elif inpu.startswith("make"):
        mix = optimize_mix(target, available)
        print("Result")
        for color, weight in list(zip(available, mix['weights'])):
            print(f"  {color} → {weight:.3f}")
        print("Approximate Mixed Color:", mix['mixed_rgb'])
        print("Distance:", mix['distance'])
        
        
    else:
        available.append(splitRGB(inpu))
        menu_restart(target, available)


def main():
    tcol = inEKI("Enter the Target Color in RGB Seperated by ' ':")
    tcol = splitRGB(tcol)
    menu(tcol)


    ##
    #
    ##
    

    
if __name__ == "__main__":
    main()