from NeuralNetworks.Pose import Pose2D


def randomGenerateStartEndPose():
    random_start_pose = Pose2D.random()
    random_end_pose = Pose2D.random()
    return random_start_pose, random_end_pose

'''
def update():
    randomGenerateStartEndPose()
    block_pos = getBlockerNetworkEstimate()
    placeOnField(block_pos)

    path_pred = getPlannerNetworkEstimate()
    plotOnField(path_pred)

    planner_cost = evaluatePlannerCost(field, block_pos, path_pred)
    blocker_cost = evaluateBlockerCost(field, block_pos, path_pred)

    addBlockerExperienceReplay(field, block_pos, blocker_cost)
    addPlannerExperienceReplay(field, path_pred, planner_cost)

    learnPlannerAgentFromExistingQFunction()
    learnBlockerAgentFromExistingQFunction()

    learnPlannerQfromExperienceReplay()
    learnBlockerQfromExperienceReplay()
'''
