config_version = "2" # Version of the Vagrant configuration format

num_workers = 2 # Number of worker nodes
system("python generate_inventory.py #{num_workers} > ansible/inventory.cfg")

Vagrant.configure(config_version) do |config|  
  
  # config.vm.box = "ubuntu/bionic64"
  # Create a private network for communication between VMs
  # config.vm.network "private_network", type: "dhcp"

  # To make everything work on windows, comment the above line and uncomment the following lines
  config.vm.box = "bento/ubuntu-20.04"
  config.vm.box_version = "202404.23.0"
  config.vm.network "private_network", ip: "192.168.57.10", netmask: "255.255.255.0", type: "dhcp", dhcp_ip:"192.168.57.3", dhcp_lower: "192.168.57.4", dhcp_upper: "192.168.57.100"

  config.vm.provider "virtualbox" do |vb|
    vb.customize [ "modifyvm", :id, "--uartmode1", "disconnected" ]
    vb.gui = true
  end

  config.vm.network "forwarded_port", guest: 30000, host: 30000
  config.vm.network "forwarded_port", guest: 30001, host: 30001
  config.vm.network "forwarded_port", guest: 30002, host: 30002

  # Define controller
  config.vm.define "controller1" do |controller|
    controller.vm.hostname = "controller1"
    controller.vm.network "private_network", ip: "192.168.57.4"
    controller.vm.provider "virtualbox" do |vb|
      vb.memory = "4000"
      vb.cpus = 2
    end
    # controller.vm.provision "ansible" do |ansible|
    #   ansible.playbook = "ansible/playbooks/provision_controller.yaml"
    #   ansible.inventory_path = "ansible/inventory.cfg"
    # end
  end

  # Define workers
  (1..num_workers).each do |i|
    config.vm.define "worker#{i}" do |worker|
      worker.vm.hostname = "worker#{i}"
      worker.vm.network "private_network", ip: "192.168.57.#{i+10}"
      worker.vm.provider "virtualbox" do |vb|
        vb.memory = "3000"
        vb.cpus = 1
      end
      # worker.vm.provision "ansible" do |ansible|
      #   ansible.playbook = "ansible/playbooks/provision_worker.yaml"
      #   ansible.inventory_path = "ansible/inventory.cfg"
      # end
    end
  end

  # Use Ansible provisioner to configure the entire cluster after VM setup
  # config.vm.provision "ansible" do |ansible|
  #   ansible.playbook = "ansible/playbooks/full-setup.yml"
  #   ansible.inventory_path = "ansible/inventory.cfg"
  #   ansible.limit = "all"
  #   ansible.become = true
  # end
end