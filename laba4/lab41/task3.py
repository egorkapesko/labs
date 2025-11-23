import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def task3():
    fig, ax = plt.subplots(figsize=(10, 8))

    body = patches.Ellipse((0.5, 0.5), 0.6, 0.4, color='gray', alpha=0.8)
    ax.add_patch(body)

    head = patches.Circle((0.5, 0.75), 0.15, color='gray', alpha=0.8)
    ax.add_patch(head)

    ear1 = patches.Polygon([[0.42, 0.85], [0.45, 0.92], [0.48, 0.85]], color='gray')
    ear2 = patches.Polygon([[0.52, 0.85], [0.55, 0.92], [0.58, 0.85]], color='gray')
    ax.add_patch(ear1)
    ax.add_patch(ear2)

    eye1 = patches.Circle((0.47, 0.77), 0.02, color='green')
    eye2 = patches.Circle((0.53, 0.77), 0.02, color='green')
    ax.add_patch(eye1)
    ax.add_patch(eye2)

    pupil1 = patches.Circle((0.47, 0.77), 0.008, color='black')
    pupil2 = patches.Circle((0.53, 0.77), 0.008, color='black')
    ax.add_patch(pupil1)
    ax.add_patch(pupil2)

    nose = patches.Polygon([[0.5, 0.72], [0.48, 0.68], [0.52, 0.68]], color='pink')
    ax.add_patch(nose)

    for i in range(3):
        ax.plot([0.48, 0.38], [0.70 + i*0.01, 0.70 + i*0.02], 'k-', linewidth=1)
        ax.plot([0.52, 0.62], [0.70 + i*0.01, 0.70 + i*0.02], 'k-', linewidth=1)

    paw1 = patches.Circle((0.4, 0.35), 0.05, color='gray')
    paw2 = patches.Circle((0.6, 0.35), 0.05, color='gray')
    ax.add_patch(paw1)
    ax.add_patch(paw2)

    ax.plot([0.05, 0.25], [0.5, 0.45], 'k-', linewidth=8, color='gray')
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off')
    plt.title('Кот', fontsize=16, pad=20, fontweight='bold')
    plt.show()

if __name__ == "__main__":
    task3()