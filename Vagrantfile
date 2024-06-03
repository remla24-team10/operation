# config_version = "2" # Version of the Vagrant configuration format

# num_workers = 2 # Number of worker nodes
# # system("python generate_inventory.py #{num_workers} > ansible/inventory.cfg")

# Vagrant.configure(config_version) do |config|  
  
#   # config.vm.box = "ubuntu/bionic64"
#   # Create a private network for communication between VMs
#   # config.vm.network "private_network", type: "dhcp"

#   # To make everything work on windows, comment the above line and uncomment the following lines
#   config.vm.box = "bento/ubuntu-20.04"
#   config.vm.box_version = "202404.23.0"
#   config.vm.network "private_network", ip: "192.168.57.10", netmask: "255.255.255.0", type: "dhcp", dhcp_ip:"192.168.57.3", dhcp_lower: "192.168.57.4", dhcp_upper: "192.168.57.100"

#   # config.vm.provider "virtualbox" do |vb|
#   #   vb.customize [ "modifyvm", :id, "--uartmode1", "disconnected" ]
#   #   vb.gui = true
#   # end

#   # Define controller
#   config.vm.define "controller1" do |controller|
#     controller.vm.hostname = "controller1"
#     controller.vm.network "private_network", ip: "192.168.57.4"
#     controller.vm.provider "virtualbox" do |vb|
#       vb.memory = "4000"
#       vb.cpus = 2
#     end
#   end

#   # Define workers
#   (1..num_workers).each do |i|
#     config.vm.define "worker#{i}" do |worker|
#       worker.vm.hostname = "worker#{i}"
#       worker.vm.network "private_network", ip: "192.168.57.#{i+10}"
#       worker.vm.provider "virtualbox" do |vb|
#         vb.memory = "3000"
#         vb.cpus = 1
#       end
#     end
#   end
# end

Vagrant.configure("2") do |config|
  # Define the base box to use
  config.vm.box = "ubuntu/bionic64"
  config.ssh.insert_key = false
  config.vm.network "private_network", ip: "192.168.56.110", netmask: "255.255.255.0", type: "dhcp", dhcp_ip:"192.168.56.100", dhcp_lower: "192.168.56.101", dhcp_upper: "192.168.56.254"

  config.vm.provision :shell, :inline => "sudo sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/g' /etc/ssh/sshd_config; sudo systemctl restart sshd;", run: "always"

  # Define the controller node
  config.vm.define "controller" do |controller|
    controller.vm.hostname = "controller"
    controller.vm.network "private_network", ip: "192.168.56.112"
    controller.vm.provider "virtualbox" do |vb|
      vb.memory = 4096
      vb.cpus = 1
      vb.customize [ "modifyvm", :id, "--uartmode1", "disconnected" ]
    end
  end

  # Define the worker nodes
  (1..1).each do |i|
    config.vm.define "worker#{i}" do |worker|
      worker.vm.hostname = "worker#{i}"
      worker.vm.network "private_network", ip: "192.168.56.10#{i+3}"
      worker.vm.provider "virtualbox" do |vb|
        vb.memory = 6144
        vb.cpus = 2
        vb.customize [ "modifyvm", :id, "--uartmode1", "disconnected" ]
      end
    end
  end
end