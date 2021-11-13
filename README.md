# well-logs-plot
Plot function that I created for plotting geological well logs. This function plots well logs for a single well. Well logs cal, gam, res, den, neu are currently included but the code can be edited to include your logs. All styling are based on a specific project and for a specific field. Further customization will be required for your use.
Note: Caliper log is re-scaled to optimize visualization. You will need to remove/adjust the scaling parameter to fit your field values.
:dataset: Name of the pandas dataframe containing well logs measurements
:well: Name of well to be plotted
:logs: set of well logs to be plotted for the chosen well
