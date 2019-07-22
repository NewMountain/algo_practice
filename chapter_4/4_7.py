"""Chapter 4: Trees and Graphs. Question 4.7"""

import math
import copy

# Given a list of projects their dependencies
# [(dependency, project)]
# Find a build order, return an error if not possible to resolve

projects = ["a", "b", "c", "d", "e", "f"]
dependencies = [("a", "d"), ("f", "b"), ("b", "d"), ("f", "a"), ("d", "c")]


def find_node(build_order, dependencies):
    """Find a dependency and add to build order."""
    # Pointers on dictionaries are evil
    # Algo now is simple, iterate through the keys
    # Remove the key and also remove it from any other list of values
    d = copy.deepcopy(dependencies)
    # So we can delete all instances without depedencies in one pass
    for k, v in d.items():
        # Find a key with an empty list of values,
        if not v:
            # Add k to the build order
            build_order.append(k)
            # Delete the key from dependencies
            del dependencies[k]
            # Now remove the k from all dependency sets
            # I wish set operations were pure functions in Python
            _trigger_io = {key: value.discard(k) for key, value in dependencies.items()}

    return build_order, dependencies


# I am told this is O(P+D) time where p is projects and D is dependencies
# This is a topological sort
def resolve_build_order(projects, dependencies):
    """Return a build order or throw an error."""
    # Unpack the dependencies into a dictionary for faster reference
    deps = {}
    for dependency, project in dependencies:
        if project in deps:
            deps[project].add(dependency)
        else:
            deps[project] = set([dependency])

    # Now make sure all projects appear as keys in the dictionary
    for p in projects:
        if p not in deps:
            deps[p] = set()

    build_order = []

    # As dictionaries are mutable references, this gets harder
    # We can track if we're unable to build based on the number of keys
    prior_key_len = math.inf

    while prior_key_len != len(deps.keys()):
        prior_key_len = len(deps.keys())
        # If you can't find a single diff,
        # you have an irreconcilable graph
        # or you've reached the end
        build_order, deps = find_node(build_order, deps)

    # See if you were able to create a build
    if deps == {}:
        return build_order

    raise Exception("Unable to resolve a build order")


print(resolve_build_order(projects, dependencies))
