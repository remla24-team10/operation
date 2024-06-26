#!/usr/bin/env python
import sys

def generate_inventory(num_workers):
    inventory_text = ""

    inventory_text += "[controller]\n"
    inventory_text += "vagrant@192.168.57.4\n"
    inventory_text += "controller1 ansible_host=192.168.57.4 ansible_user=vagrant\n\n"

    inventory_text += "[worker]\n"
    inventory_text += "vagrant@192.168.57.11\nvagrant@192.168.57.12\n"
    for i in range(1, num_workers + 1):
        inventory_text += f"worker{i} ansible_host=192.168.57.{i + 10} ansible_user=vagrant\n"
    inventory_text += "\n"

    inventory_text += "[k8s_cluster:children]\n"
    inventory_text += "controller\n"
    inventory_text += "worker\n"

    return inventory_text

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generate_inventory.py num_workers")
        sys.exit(1)

    num_workers = int(sys.argv[1])
    inventory_text = generate_inventory(num_workers)
    print(inventory_text)
