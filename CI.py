from scipy import stats
import math

n = int(input("Enter n: "))
x = float(input("Enter x̄: "))
s = float(input("Enter s: "))
confidence = float(input("Enter CI (eg: 95% is 0.95): "))
side = input("Enter side (L - lower | U - upper | T - Two-sided): ")
side = side.upper()

# Get numbers for calculating t statistic/critical value
a = 1 - confidence
v = n-1

if side == 'T':
    ta = a/2

    # Get the critical value
    crit = stats.t.ppf(ta, v)

    # Calculate CI
    CIl = x - (crit * (s/math.sqrt(n)))
    CIh = x + (crit * (s/math.sqrt(n)))

    print("The CI is [" + str(CIl) + ", " + str(CIh) + "]")

elif side == 'L':
    ta = a

    # Get the critical value
    crit = stats.t.ppf(ta, v)

    # Calculate CI
    CIl = x - (crit * (s/math.sqrt(n)))

    print("The CI is [" + str(CIl) + "])")

elif side == 'U':
    ta = a

    # Get the critical value
    crit = stats.t.ppf(ta, v)

    # Calculate CI
    CIh = x + (crit * (s/math.sqrt(n)))

    print("The CI is [" + str(CIh) + "])")
    