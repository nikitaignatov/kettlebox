import pandas as pd
from lib.label import label_activity, label_activity_part
from lib.samples import collect, load_sample


def transform():

    # import from files
    df_row_left = pd.DataFrame().append([collect(
        'row-left-1'), collect('row-left-2'), collect('row-left-3')], ignore_index=True)
    df_row_right = pd.DataFrame().append(
        [collect('row-right-1'), collect('row-right-2')], ignore_index=True)
    df_clean = pd.DataFrame().append(
        [collect('clean-1'), collect('clean-2')], ignore_index=True)
    df_rest = collect('rest-1')
    df_swing_both_hands = pd.DataFrame().append([collect('swing-both-hands-1'), collect(
        'swing-both-hands-2'), collect('swing-both-hands-3')], ignore_index=True)
    df_deadlift_both_hands = pd.DataFrame().append([collect(
        'deadlift-both-hands-1'), collect('deadlift-both-hands-2')], ignore_index=True)
    df_goblet_squat = pd.DataFrame().append(
        [collect('goblet-squat-1'), collect('goblet-squat-2')], ignore_index=True)
    #
    df_press_r = pd.DataFrame().append([
        load_sample('press_right_0'),
        load_sample('press_right_2'),
        load_sample('press_right_3')
    ], ignore_index=True)
    df_press_l = pd.DataFrame().append([
        load_sample('press_left_0'),
        load_sample('press_left_2'),
        load_sample('press_left_3')
    ], ignore_index=True)
    df_swing_r = pd.DataFrame().append([
        load_sample('swing_right_0'),
        load_sample('swing_right_1'),
        load_sample('swing_right_2'),
        load_sample('swing_right_3')
    ], ignore_index=True)
    df_swing_l = pd.DataFrame().append([
        load_sample('swing_left_0'),
        load_sample('swing_left_1'),
        load_sample('swing_left_2'),
        load_sample('swing_left_3')
    ], ignore_index=True)

    # label individual activies
    label_activity(df_row_right, "Row Right")
    label_activity(df_row_left, "Row Left")
    label_activity(df_rest, "Rest")
    label_activity(df_swing_both_hands, "Swing Both Hands")
    label_activity(df_deadlift_both_hands, "Deadlift Both Hands")
    label_activity(df_goblet_squat, "Goblet Squat")
    label_activity(df_clean, "Clean")

    label_activity(df_press_l, "Press Left")
    label_activity(df_press_r, "Press Right")
    label_activity(df_swing_r, "Swing Right")
    label_activity(df_swing_l, "Swing Left")

    # new frame with with all the activities
    df = pd.DataFrame()
    df = df.append([df_row_right, df_row_left, df_rest, df_swing_both_hands, df_deadlift_both_hands, df_goblet_squat, df_clean, df_swing_l, df_swing_r,
                    df_press_l, df_press_r])

    return df
