import os
import json
import sys

def main():
    # Parse spec into a dict
    spec = json.loads(sys.stdin.read())
    metric(spec)

def metric(spec):
    # Get metadata from resource information provided
    metadata = spec["resource"]["metadata"]
    sys.stderr.write("name:", metadata["name"])
    
    sys.stdout.write(1)

if __name__ == "__main__":
    main()