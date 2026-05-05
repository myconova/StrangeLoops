# Theme: Invariants hidden in motion
# Difficulty: Medium
# You are given a sequence of operations on a ledger. The ledger starts empty.
# There are only three possible operations: "ADD x", to add integer x to the ledger; "REMOVE" remove one integer from the ledger, you choose; "QUERY" output a single integer based on the current ledger contents. 
# Twist: The ledger has a hidden invariant. No matter how you choose which element to remove, every valid sequence of operations must make all QUERY outputs identical. Your task is to determine which invariant property the ledger must be tracking.
# You are given this sequence: ADD 5, ADD 2, ADD 9, REMOVE, ADD 4, QUERY, ADD 7, REMOVE, REMOVE, QUERY.
# Your job: Determine what invariant the ledger must be preserving. 2. Determine the two QUERY outputs that must appear. 
# Provide two distinct solution paths that both respect the invariant. 


# Solution Path A - Ledger States

from operator import index


def ledger_state(operations):
    operations = ["ADD 5", "ADD 2", "ADD 9", "REMOVE", "ADD 4", "QUERY", "ADD 7", "REMOVE", "REMOVE", "QUERY"]
    states = {()}
    query_outputs = []
    
    for i, op in enumerate(operations):
        if op.startswith("ADD"):
            next_states = set()
            for state in states:
                _, x = op.split()
                next_states.add(state + (int(x),))
            states = next_states

        elif op == "REMOVE":
            next_states = set()
            for state in states:
                for i in range(len(state)):
                    child = state[:i] + state[i+1:]
                    next_states.add(child)
            states = next_states

        elif op == "QUERY":
            query_outputs.append(states)
        
    return query_outputs
result = ledger_state([])
print(result) 

def candidate_missing(ledger):
    s = set(ledger)
    x = 1
    while x in s:
        x += 1
    return x

resulte = ledger_state([])

for checkpoint_index, snapshot in enumerate(resulte):
    values = {candidate_missing(list(state)) for state in snapshot}
    print(f"QUERY {checkpoint_index + 1}: candidate values = {values}")