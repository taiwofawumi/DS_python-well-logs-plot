#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

def plot_well(dataset, well):
    """A function that plots well logs for a single well
    
    The plot function plots predefined logs namely, cal, gam, res, den, neu.
    All styling are based on Teck's HFGM project and for a specific field.
    Further customization will be required to use outside of the project/field.
    Note: Caliper log is re-scaled to optimize visualization. You will need to ..
    ..remove/adjust the scaling parameter to fit your field values.
    :dataset: Name of the pandas dataframe containing well logs measurements
    :well: Name of well to be plotted
    :logs: set of well logs to be plotted for the chosen well
    call function with: from plot_well_logs import plot_well
    """
    
    if well in set(dataset.HOLEID):
        data = dataset[dataset.HOLEID == well]
        logs = ['cal','gam','res','den','neu']
        fig, ax = plt.subplots(1,5,figsize = (15,15),sharey=True)
        cal1=1.25 - (data.cal/max(data.cal))
        cal2=(data.cal/max(data.cal))-0.25 
        ax[0].plot(cal1,data.depth,'k-', linewidth='0.7')
        ax[0].set_xlim(0.1, 0.9)        
        ax2=ax[0].twiny()
        ax2.plot(cal2,data.depth,'k-', linewidth='0.7')
        ax2.set_xlim(0.1, 0.9)
        ax[0].fill_betweenx(data.depth, cal1, cal2, color = 'grey', linewidth=0, alpha=.75)
        ax[1].plot(data.gam,data.depth,'g-', linewidth='0.7')
        ax[1].fill_betweenx(data.depth, 65, data.gam, where=(data.gam<=65), color = 'orange', linewidth=0, alpha=.75)
        ax[1].fill_betweenx(data.depth, 65, data.gam, where=(data.gam>65), color = 'green', linewidth=0, alpha=.75)
        ax[2].plot(data.res,data.depth,'r-', linewidth='0.7')
        ax[2].set_xscale('log')
        ax[2].fill_betweenx(data.depth, 2500, data.res, where=(data.res>=2500), color = 'red', linewidth=0, alpha=.75)
        ax[3].plot(data.den,data.depth,'b-', linewidth='0.7')        
        ax[3].fill_betweenx(data.depth, 1.65, data.den, where=(data.den<=1.65), color = 'blue', linewidth=0, alpha=.75)
        ax[4].plot(data.neu,data.depth,'m-', linewidth='0.7')
        fig.suptitle(f'Well: {well}', fontsize=15)
        fig.text(0.08, 0.5, 'Depth', va='center', rotation='vertical', fontsize=15)
        for i, j in zip(logs, range(len(ax))):
            ax[j].set_ylim(max(data.depth), min(data.depth))
            ax[j].minorticks_on()
            ax[j].xaxis.tick_top()
            ax[j].grid(which='major', linestyle='-', linewidth='0.5', color='green')
            ax[j].grid(which='minor', linestyle=':', linewidth='0.5', color='black')
            ax[j].set_title(f'{i}\n', fontsize=15)
        plt.subplots_adjust(wspace=0)
    else:
        print('Well not found in list')

__author__ = "Taiwo Fawumi"
__email__ = "taiwo.fawumi@yahoo.com"