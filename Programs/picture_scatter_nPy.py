import numpy as np
import vispy.scene
from vispy.scene import visuals


# read from .npy file
glist = np.load("/{"your path"}/colornum_{X}/iteration_{Y}/glist/glist_{N}.npy")
glist_array = np.array(glist)

print("The length of the list is: ", len(glist_array))

# Ensure the array is 2D with shape (N, 3)
assert glist_array.ndim == 2 and glist_array.shape[1] == 3, "glist must be a 2D array with shape (N, 3)"

# VisPy Visualization Setup
canvas = vispy.scene.SceneCanvas(keys='interactive', show=True)
view = canvas.central_widget.add_view()

# Create scatter plot (nodes)
scatter = visuals.Markers()
scatter.set_data(glist_array, edge_color=None, face_color=(1, 1, 1, .5), size=5)
view.add(scatter)

# Update the canvas to ensure all data is loaded
canvas.update()

# Camera setup
view.camera = 'turntable'  # or try 'arcball'

# Run the application
if __name__ == '__main__':
    vispy.app.run()
