Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/bionic64"

  # Create a private network for communication between VMs
  config.vm.network "private_network", type: "dhcp"

  # To make everything work on windows, comment the above line and uncomment the following lines
  # config.vm.box = "bento/ubuntu-20.04"
  # config.vm.box_version = "202404.26.0"
  # config.vm.network "private_network", ip: "192.168.57.10", netmask: "255.255.255.0", type: "dhcp", dhcp_ip:"192.168.57.3", dhcp_lower: "192.168.57.4", dhcp_upper: "192.168.57.100"

  # Define controller
  config.vm.define "controller1" do |controller|
    controller.vm.hostname = "controller1"
    controller.vm.network "private_network", ip: "192.168.56.4"
    controller.vm.provider "virtualbox" do |vb|
      vb.memory = "4000"
      vb.cpus = 1
    end
    controller.vm.provision "ansible" do |ansible|
      ansible.playbooks = [
        "ansible/playbooks/install_dependencies.yaml",
        "ansible/playbooks/provision_controller.yaml"
      ]
      ansible.inventory_path = "ansible/inventory.cfg"
    end
  end

  # Define workers
  (1..2).each do |i|
    config.vm.define "worker#{i}" do |worker|
      worker.vm.hostname = "worker#{i}"
      worker.vm.network "private_network", ip: "192.168.56.#{i+10}"
      worker.vm.provider "virtualbox" do |vb|
        vb.memory = "3000"
        vb.cpus = 1
      end
      worker.vm.provision "ansible" do |ansible|
        ansible.playbooks = [
          "ansible/playbooks/install_dependencies.yaml",
          "ansible/playbooks/provision_worker.yaml"
        ]
        ansible.inventory_path = "ansible/inventory.cfg"
      end
    end
  end
end