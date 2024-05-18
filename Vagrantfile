Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/bionic64"

  # Create a private network for communication between VMs
  config.vm.network "private_network", type: "dhcp"

  # Define controller
  config.vm.define "controller1" do |controller|
    controller.vm.hostname = "controller1"
    controller.vm.network "private_network", ip: "192.168.56.4"
    controller.vm.provider "virtualbox" do |vb|
      vb.memory = "4000"
      vb.cpus = 1
    end
    controller.vm.provision "ansible" do |ansible|
      ansible.playbook = "ansible/playbook-controller.yml"
      ansible.inventory_path = "ansible/inventory.cfg"
    end
  end

  # Define workers
  (1..2).each do |i|
    config.vm.define "worker#{i}" do |worker|
      worker.vm.hostname = "worker#{i}"
      worker.vm.network "private_network", ip: "192.168.56.#{i+10}"
      worker.vm.provider "virtualbox" do |vb|
        vb.memory = "6000"
        vb.cpus = 2
      end
      worker.vm.provision "ansible" do |ansible|
        ansible.playbook = "ansible/playbook-worker.yml"
        ansible.inventory_path = "ansible/inventory.cfg"
      end
    end
  end
end
