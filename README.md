# well-logs-plot
Plot function that I created for plotting geological well logs. Sample plot not available due to data security.
A function that plots well logs for a single well. The plot function plots predefined logs namely, cal, gam, res, den, neu. All styling are based on a specific project and for a specific field. Further customization will be required to use outside of the project/field.
Note: Caliper log is re-scaled to optimize visualization. You will need to remove/adjust the scaling parameter to fit your field values.
:dataset: Name of the pandas dataframe containing well logs measurements
:well: Name of well to be plotted
:logs: set of well logs to be plotted for the chosen well
