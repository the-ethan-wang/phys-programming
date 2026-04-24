
def collide(m1, m2, u1, u2):
    """Returns v1, v2 post-collision. Assumes m1 is to the left of m2, where right is positive"""
    rel_v=u1-u2
    init_m=m1*u1+m2*u2
    v1=(init_m-m2*rel_v)/(m1+m2)
    v2=v1+rel_v
    return(v1, v2)

samples=[
    (1, 1, 1, 0),
    (1, 1, 5, -3),
    (2, 1, 1, -2),
    (100, 1, 1, 0)
]

for m1,m2,u1,u2 in samples:
    v1,v2=collide(m1,m2,u1,u2)
    print(f"Mass 1({m1:.2f}kg, {u1:.2f}ms^-1) is hits mass 2({m2:.2f}kg, {u2:.2f}ms^-1). As a result, mass 1 has a new velocity {v1:.2f} and mass 2's velocity is {v2:.2f}.")