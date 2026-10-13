import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

from .style import C_MAIN, C_ACCENT, C_MUTED

def plot_maximum_laws(maxima, levels, empirical, theoretical, endpoint):
    fig, axes = plt.subplots(1, 2, figsize = (12, 4.6))

    ax= axes[0]
    grid = np.linspace(0, 4, 300)

    ax.hist(
        maxima,   # plotting the simulated maxima
        bins = 160,   # dividing the observation into 160 bins
        density = True,  # transforming the histogram into a density function
        color = C_MAIN,
        alpha = 0.5,
        label = 'Sampled maxima',
    )

    ax.plot(
        grid, 
        2 * norm.pdf(grid),
        color = C_ACCENT,
        lw = 2,
        label = 'Half-normal distribution',
    )

    ax.set_xlim(0, 3.6)  
    ax.set_xlabel("Maximum")  
    ax.set_ylabel("Density")  
    ax.set_title("Marginal law of the maximum")  
    ax.legend()  

    ax = axes[1]  # Select the right chart

    ax.semilogy(
        levels,                   # Levels the maximum might exceed
        empirical,                # Simulated exceedance probabilities
        color=C_MAIN,             
        lw=2,                     
        label=f"Empirical survival, c = {endpoint}",  # Insert the endpoint in the label.
    )

    ax.semilogy(
        levels,                   # Use the same comparison levels
        theoretical,              # Theoretical exceedance probabilities
        color=C_ACCENT,           
        lw=1.6,                   
        ls="--",                  
        label="exp(-2y(y-c))",     # Identify the theoretical formula.
    )

    ax.set_xlabel("Level y")  
    ax.set_ylabel("P(M ≥ y | C = c)")  # Label the conditional probability
    ax.set_title("Conditional law at a fixed endpoint")  
    ax.legend()  

    fig.tight_layout()  
    return fig  

def plot_discretisation_bias(ms, ratios, ses):
    'Showing how discrete observation underestimate the daily range'
    fig, ax = plt.subplots(figsize = (10.4, 4.6))

    ax.errorbar(
        ms,  # number of observation per session
        ratios, # observed range divided by its continuous reference 
        yerr=2 * ses,  # uncertainty of two standard errors
        fmt='o-',
        color = C_MAIN,
        lw = 1.8,
        capsize = 3, # caps for the error bars
        label = 'Observed / continuous expected range ',
    )

    grid = np.linspace(5, 1700, 400) 
    beta = (1 - ratios[-1]) * np.sqrt(ms[-1]) #Anchoring the guide to the last result

    ax.plot(
        grid,
        1-beta/np.sqrt(grid), # shrinking discretisation bias
        color = C_ACCENT,
        ls = '--',
        lw = 1.5,
        label = f'Guide: 1 - {beta:.2f}/sqrt(m)'
    )
    
    ax.axhline(1.0, color=C_MUTED, lw=1)  # Mark the continuous-model target.
    ax.set_xscale("log")  # Make widely separated observation counts readable.
    ax.set_xlabel("Observations per session m — log scale")  # Label the horizontal axis.
    ax.set_ylabel("Observed / continuous expected range")  # Label the vertical axis.
    ax.set_title("Discretization bias of observed ranges")  # Add the title.
    ax.legend()  # Display the series labels.
    fig.tight_layout()
    return fig 