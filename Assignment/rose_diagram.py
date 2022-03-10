#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def rose_diagram(df, ax, color):
    # Compute max and min in the dataset
    max = 400
    lowerLimit=20
    slope = (max - lowerLimit) / max
    heights = slope * df.Value + lowerLimit

    # Compute the width of each bar. In total we have 2*Pi = 360°
    width = 2*np.pi / len(df.index)

    # Compute the angle each bar is centered on:
    indexes = list(range(1, len(df.index)+1))
    angles = [element * width for element in indexes]
    # Draw bars
    bars = ax.bar(
        x=angles, 
        height=heights, 
        width=width, 
        bottom= 20,
        linewidth=2, 
        edgecolor="white",
        color=color,
    )

    # little space between the bar and the label
    labelPadding = 4

    # Add labels
    for bar, angle, height, label in zip(bars,angles, heights, df["Name"]):

        # Labels are rotated. Rotation must be specified in degrees :(
        rotation = np.rad2deg(angle)

        # Flip some labels upside down
        alignment = ""
        if angle >= np.pi/2 and angle < 3*np.pi/2:
            alignment = "right"
            rotation = rotation + 180
        else: 
            alignment = "left"

        # Finally add the labels
        ax.text(
            x=angle, 
            y=lowerLimit + bar.get_height()+ labelPadding, 
            s=label, 
            ha=alignment, 
            va='center', 
            rotation_mode="anchor", weight='bold', size=8) 
    return ax

