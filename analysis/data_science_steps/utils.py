import pandas as pd
import itertools
from datetime import datetime

def convert_time(df):
    """Convert the 'start occurrence time' to datetime.time objects."""
    df.index = df.index.set_levels(
        [df.index.levels[0], df.index.levels[1].map(lambda t: datetime.strptime(t, '%H:%M:%S').time()), df.index.levels[2]]
    )
    return df

def generate_15_min_intervals(df):
    """Generate 15-minute intervals between the min and max of start occurrence time in the DataFrame."""
    # Get the min and max times
    min_time = df.index.get_level_values('start occurrence time').min()
    max_time = df.index.get_level_values('start occurrence time').max()

    # Convert to strings for date_range to work
    min_time_str = min_time.strftime("%H:%M:%S")
    max_time_str = max_time.strftime("%H:%M:%S")

    # Generate 15-minute intervals between min and max times
    intervals = pd.date_range(min_time_str, max_time_str, freq="15T").time
    return intervals

def fill_missing_rows_15min(df):
    """Ensure that each 15-minute period has two rows, one for each flow_marker."""
    # Convert time strings to datetime.time if not already converted
    df = convert_time(df)

    # Get the unique weekdays from the existing DataFrame
    weekdays = df.index.get_level_values(0).unique()
    
    # Generate the expected 15-minute intervals based on the actual data range
    times = generate_15_min_intervals(df)
    
    # Assume flow markers are always 1 or 2
    flow_markers = [1, 2]
    
    # Generate the full index with all combinations of Weekdays, 15-minute intervals, and flow markers
    full_index = pd.MultiIndex.from_tuples(
        list(itertools.product(weekdays, times, flow_markers)),
        names=["Weekday", "start occurrence time", "flow_marker"]
    )

    # Reindex the DataFrame to include the missing rows
    df_full = df.reindex(full_index)
    
    return df_full

def check_for_missing_15min_rows(df):
    """Check if every 15-minute interval has two rows for flow_marker 1 and 2."""
    # Convert time strings to datetime.time if not already converted
    df = convert_time(df)
    print(df)

    # Generate the expected 15-minute intervals based on the actual data range
    times = generate_15_min_intervals(df)
    print(times)

    for weekday in df.index.get_level_values(0).unique():
        for time in times:
            subset = df.loc[(weekday, time)]
            print(subset)
            print(subset.shape[0])
            # if subset.shape[0] != 2:  # There should be exactly 2 rows (one for each flow_marker)
            #     print(f"Missing rows for {weekday} at {time}.")

