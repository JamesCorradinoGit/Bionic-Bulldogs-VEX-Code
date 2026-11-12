# Robot configuration code
# AI Vision Color Descriptions
ai_vision_11__redCone = Colordesc(1, 238, 43, 54, 10, 0.2)
ai_vision_11__yellowCone = Colordesc(2, 161, 120, 46, 10, 0.2)
ai_vision_11__COLOR3 = Colordesc(3, 16, 60, 111, 10, 0.2)
# AI Vision Code Descriptions
ai_vision_11 = AiVision(Ports.PORT11, ai_vision_11__redCone, ai_vision_11__yellowCone, ai_vision_11__COLOR3, AiVision.ALL_TAGS)

def findAprilTags() -> int:
    snapshot_objects = ai_vision_1.take_snapshot(AiVision.ALL_TAGS);
    if snapshot_objects and len(snapshot_objects) > 0:
        return (snapshot_objects[0].id)
    return 
