# Bungee Jumping
# https://open.kattis.com/problems/bungeejumping
# TAGS: simulation
# CP4: 1.6g, Real Life, Harder
# NOTES:
"""
Physics Kattis O_o

variables renaming for clarity:

k: rope constant
l: rope length
s: bridge height (I WILL USE h NOT s)
w: person's MASS (I WILL USE m NOT w, IT IS A *MASS* NOT A *WEIGHT*)
g: 9.81

So, cases according to rope length:

1) If l >= h, rope's elasticity is not used, person is in free fall at the bottom of the bridge with a velocity given by:
    m * g * h = m * v_final**2 / 2
 >> v_final = sqrt(2 g h)

2) If l < h, then rope's elasticity IS used. Need enough gravitational potential energy to do work to extend the rope by length_change = (h - l_original)
i.e. need m * g * h >= integral (k*length_change) == 1/2 * k * (h - l_original)**2

                           ^^^^^ this is integral k*length_change*dl with limits given by h and l_original

2) A) If this condition is true, then the kinetic energy at the bottom of the bridge, after converting the required amount of gravitational
potential energy to do work is given by

m * v_final**2 / 2  =  m *g*h - 1/2 * k * (h - l_original)**2
 >> v_final = sqrt(  2*g*h - k* (h - l_original)**2 / m )

2) B) If not true, then person stays mid air somewhere having not extended the rope enough

---

Implementation notes:

Should try to avoid floats and square roots and divisions etc.
I have a place in code where I divide by m : you can rearrange formula but left it for clarity (solution is AC, but not best practice numerically)
"""
g = 9.81
V_FATAL = 10 # NOTE FATAL IS > 10, NOT >=10 IF I READ CORRECTLY: if he collides at a speed of more than 10 m/s, he will not survive the impact
STUCK = "Stuck in the air."
SURVIVE = "James Bond survives."
KILLED = "Killed by the impact."

while True:
    k, l, h, m = map(float, input().split())
    if k == l == h == m == 0:
        break
    # Case 1
    if l >= h:
        # v_final = sqrt(2 g h)
        if 2 * g * h > V_FATAL * V_FATAL:
            print(KILLED)
        else:
            print(SURVIVE)
    else:
        # Case 2
        # need m * g * h >= integral (k * length_change * dl) == 1/2 * k * (h - l_original)**2
        length_change = h - l
        if 2 * m * g * h >= k * length_change * length_change:
            # v_final = sqrt(  2 * g * h - k * (h - l_original)**2 / m )
            if 2 * g * h - k * length_change * length_change / m > V_FATAL * V_FATAL: # <- should multiply through by m to avoid division, see Implementation Notes
                print(KILLED)
            else:
                print(SURVIVE)
        else:
            print(STUCK)