def draw_field(field_dimensions, obstacles=[]):
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches

    # Create figure and axis
    fig, ax = plt.subplots()

    # Set the limits of the field
    ax.set_xlim(0, field_dimensions[0])
    ax.set_ylim(0, field_dimensions[1])

    # Draw the field boundary
    field_boundary = patches.Rectangle((0, 0), field_dimensions[0], field_dimensions[1], linewidth=2, edgecolor='green', facecolor='none')
    ax.add_patch(field_boundary)

    # Draw obstacles
    for obstacle in obstacles:
        obstacle_patch = patches.Rectangle((obstacle['x'], obstacle['y']), obstacle['width'], obstacle['height'], linewidth=1, edgecolor='red', facecolor='red')
        ax.add_patch(obstacle_patch)

    # Set aspect of the plot to be equal
    ax.set_aspect('equal', adjustable='box')

    # Show the plot
    plt.title('Field Representation')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid()
    plt.show()