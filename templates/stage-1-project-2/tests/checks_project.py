# Runs after the notebook, in the same session.
check("difference and interval are numbers",
      lambda: all(isinstance(float(v), float) for v in (difference, ci_low, ci_high)),
      "Store the difference in `difference` and the interval in `ci_low` and `ci_high`, as numbers.")
check("interval contains the estimate", lambda: float(ci_low) < float(difference) < float(ci_high),
      "ci_low should be below the difference and ci_high above it. Check the order of subtraction.")
check("groups large enough", lambda: n_group_a >= 15 and n_group_b >= 15,
      "Each group needs at least 15 values for a bootstrap interval to be reasonable (see lesson 1.6).")
