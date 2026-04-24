def find_height(time_taken: float) -> float:
    """Returns height of jump in metres."""
    assert time_taken>0
    v=0
    t=time_taken/2
    a=-9.8
    # v = u + at
    # u = v - at
    u = v-a*t
    # s = ut + (at^2)/2
    s = u*t + (a*t**2)/2
    return s

times=[0.5, 0.67, 0.81, 0.92, 1.0]

for time in times:
    height=find_height(time)
    print(f"For a jump with hangtime {time:.2f}s, the jump height is around {height:.2f}m(excluding air resistance)")