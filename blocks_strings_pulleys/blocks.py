from typing import Optional, Union

def blocks(weights: list[Union[float,int]], net_force: Optional[Union[float,int]], net_acceleration: Optional[Union[float,int]]):
    """Returns list of every force acting on each object. Assumes force is applied to the side of the weights."""
    for weight in weights:
        if weight<0:
            print("Weights must be non-negative.")
            return
        
    if len(weights)<1:
        print("Must include at least 1 block.")
        return

    total_mass=sum(weights)
    if net_acceleration and net_force:
        if net_force!=net_acceleration*total_mass:
            print("Net force conflicts with net acceleration")
            return
    elif net_acceleration:
        net_force = net_acceleration*total_mass
    elif net_force:
        net_acceleration = net_force/total_mass
    else:
        print("Not enough information")
        return
    
    ans={"forces": [], 'net acceleration': net_acceleration, 'net force': net_force}
    for i, weight in enumerate(weights):
        obj_net_force = net_acceleration*weight
        obj_data={"name": f"Block {i+1}", "weight": weight, "forces": [], "net force": obj_net_force}
        if i==0:
            if net_force>=0:
                obj_data["forces"].append(["Applied", net_force])
                obj_data["forces"].append(["Contact Reaction", obj_net_force-net_force])
            else:
                obj_data["forces"].append(["Contact", obj_net_force])
        elif i==len(weights)-1:
            if net_force<0:
                obj_data["forces"].append(["Applied", net_force])
                obj_data["forces"].append(["Contact Reaction", obj_net_force-net_force])
            else:
                obj_data["forces"].append(["Contact", obj_net_force])
        else:
            obj_data["forces"].append(["Contact", -1*ans['forces'][i-1]['forces'][-1][1]])
            obj_data["forces"].append(["Contact Reaction", obj_net_force-obj_data['forces'][0][1]])
        ans['forces'].append(obj_data)
    return ans

examples=[
    {"name": "Sample block", "weights": [1], "net_force": 10},
    {"name": "Question 1", "weights": [3, 5], "net_force": 48},
    {"name": "Question 2", "weights": [3, 5], "net_force": -48},
    {"name": "Question 3", "weights": [2, 4, 8], "net_force": 112},
    {"name": "Question 4", "weights": [7, 4], "net_acceleration": -3},
    {"name": "Question 5", "weights": [3, 5], "net_acceleration": 5}
]

for example in examples:
    weights=example["weights"]
    net_force=example.get("net_force")
    net_acceleration=example.get("net_acceleration")
    data=blocks(weights=weights, net_force=net_force, net_acceleration=net_acceleration)
    
    assert data
    padding_count=50-len(example["name"])
    print("\n")
    print(str(example["name"]).center(50, "-"))
    print("Net acceleration of system:", f"{data['net acceleration']:.2f}ms^-2")
    print("Net force of system:", f"{data['net force']:.2f}N")
    print("Forces on each block:")
    for block in data['forces']:
        print(block["name"], "|", f"{block['weight']:.2f}Kg", "|", f"{block['net force']:.2f}N", "| ",end="")
        print(", ".join([f"{x[0]}: {x[1]:.2f}N" for x in block["forces"]]))

print("-"*50)
