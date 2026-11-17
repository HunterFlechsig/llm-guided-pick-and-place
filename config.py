import numpy as np

# NOTE: every value below is specific to the original lab rig
# (camera mount, table height, block set). Recalibrate for your setup.

block_height = -65

default_port="/dev/ttyACM0"

# Known-safe pose (x, y, z, r) the arm returns to before scene capture and
# before each pick. The camera is on the end-effector, so this is also the
# pose the affine calibration below was computed from.
home_pose = (240, 0, 150, 45)


# 2x3 affine matrix for pixel (u, v, 1) -> robot (X, Y), from your calibration.
# Previous calibration (before the camera mount shifted):
# M = np.array([
#      [6.00650232e-03 ,-4.84214952e-01,  4.430653329e+02],
#      [-4.69079919e-01  ,3.74996755e-03,  1.385349575e+02]
# ], dtype=np.float64)

M = np.array([
    [0.0027605231359, -0.480642427174, 417.419277611],
    [-0.473673561938, -0.004689904987, 140.550798343],
], dtype=np.float64)

z_above = 100           # safe travel height (e.g. 100)
z_table = -70           # Z at table contact
block_height_mm = 13   # block physical thickness
block_length_mm = 20   # block physical length
stack_delta_mm = 5    # extra height when stacking (to avoid collision)
side_offset_mm = 10    # extra XY gap when placing beside

capture_wait_time = 10
camera_index = 1