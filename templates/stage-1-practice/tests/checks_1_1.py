# Checks for practice 1.1. They run after your notebook, in the same session.
check("Exercise 1: c_to_f", lambda: c_to_f(0) == 32 and c_to_f(100) == 212 and abs(c_to_f(-40) + 40) < 1e-9,
      "c_to_f(0) should be 32, c_to_f(100) should be 212, and c_to_f(-40) should be -40.")
check("Exercise 2: mean", lambda: mean([1, 2, 3, 4]) == 2.5 and mean([7]) == 7,
      "mean([1, 2, 3, 4]) should be 2.5.")
check("Exercise 2: mean of an empty list", lambda: mean([]) is None and mean([2]) == 2,
      "mean([]) should return None.")
check("Exercise 3: count_above",
      lambda: count_above([5, 12, 30, 12], 12) == 1 and count_above([], 0) == 0 and count_above([1, 2, 3], 0) == 3,
      "Count values strictly greater than the threshold: count_above([5, 12, 30, 12], 12) should be 1.")
check("Exercise 4: rain_category",
      lambda: [rain_category(x) for x in [0, 0.99, 1, 9.9, 10, 49.9, 50, 300]]
      == ["dry", "dry", "light", "light", "moderate", "moderate", "heavy", "heavy"],
      "Check the boundaries: 1 is 'light', 10 is 'moderate', 50 is 'heavy'.")
check("Exercise 5: lookup_capital",
      lambda: lookup_capital("Kenya") == "Nairobi" and lookup_capital("Chile") == "unknown",
      "lookup_capital('Kenya') should be 'Nairobi' and lookup_capital('Chile') should be 'unknown'.")
check("Exercise 6: total_rainfall",
      lambda: total_rainfall([1, 2, 3]) == 6 and total_rainfall([1, None, 3]) == 4
      and total_rainfall([]) == 0 and total_rainfall([None]) == 0,
      "total_rainfall([1, None, 3]) should be 4, and total_rainfall([None]) should be 0.")
