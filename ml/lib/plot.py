from lib.normalize import unique_labels


def plot_activity(activity, df, i=1000, h=0):
    data = df[df['Activity'] == activity][['Ax', 'Ay', 'Az']][h:i]
    axis = data.plot(subplots=True, figsize=(24, 12),
                     title=activity)
    for ax in axis:
        ax.legend(loc='lower left', bbox_to_anchor=(1.0, 0.5))


def plot_activity_normalized(activity, df, i=1000):
    data = df[df['Activity'] == activity][['Axs', 'Ays', 'Azs']][:i]
    axis = data.plot(subplots=True, figsize=(16, 6),
                     title=activity)
    for ax in axis:
        ax.legend(loc='lower left', bbox_to_anchor=(1.0, 0.5))


def plot_activity_magnitude(activity, df, i=1000):
    data = df[df['Activity'] == activity][['Am', 'Gm']][:i]
    axis = data.plot(subplots=True, figsize=(16, 6),
                     title=activity)
    for ax in axis:
        ax.legend(loc='lower left', bbox_to_anchor=(1.0, 0.5))


def plot_datasets(df, i=1000):
    for activity in unique_labels(df):
        plot_activity(activity, df, i)


def plot_datasets_magnitude(df, i=1000):
    for activity in unique_labels(df):
        plot_activity_magnitude(activity, df, i)


def plot_datasets_normalized(df, i=1000):
    for activity in unique_labels(df):
        plot_activity_normalized(activity, df, i)
