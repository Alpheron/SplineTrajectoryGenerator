import random

from Field import Field
from Pose import Pose2D


def randomGenerateStartEndPose():
    randomStartPose = Pose2D((random.uniform(0, Field.x)), (random.uniform(0, Field.y)),
                             (random.uniform(0, Field.theta)))
    randomEndPose = Pose2D((random.uniform(0, Field.x)), (random.uniform(0, Field.y)), (random.uniform(0, Field.theta)))


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
