from Robot_Tools.Camera_Capture_Tools import capture_scene_with_detection
from Robot_Tools.Pick_Place_Tool import pick_and_place_block

capture_scene_with_detection()
pick_and_place_block(
    source_label="green1",
    target_label="yellow1",
    placement_type="on_top",
    direction="right"
)

pick_and_place_block(
    source_label="red1",
    target_label="blue1",
    placement_type="beside",
    direction="right"
)