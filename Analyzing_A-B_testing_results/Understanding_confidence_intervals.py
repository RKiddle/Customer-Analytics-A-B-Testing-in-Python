'''
In this exercise, you'll develop your intuition for how various parameter values impact confidence intervals. 
Specifically, you will explore through the get_ci() function how changes widen or tighten the confidence interval. 
This is the function signature, where cl is the confidence level and sd is the standard deviation.

def get_ci(value, cl, sd):
  loc = sci.norm.ppf(1 - cl/2)
  rng_val = sci.norm.cdf(loc - value/sd)

  lwr_bnd = value - rng_val
  upr_bnd = value + rng_val 

  return_val = (lwr_bnd, upr_bnd)
  return(return_val)
'''

# Compute and print the confidence interval
confidence_interval  = get_ci(1, 0.95, 0.001)
print(confidence_interval)
