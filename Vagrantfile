$web_script = <<-SCRIPT
apt-get update && \
apt-get install nginx -y
SCRIPT

$db_script = <<-SCRIPT
apt-get update && \
apt-get install postgresql -y
SCRIPT

$ubuntu_script = <<-SCRIPT
apt-get update && \
apt-get upgrade && \
apt-get install sysstat && \
apt-get install net-tools && \
apt-get install postgresql -y
SCRIPT

Vagrant.configure("2") do |config|

  config.vm.define "web" do |web|
    web.vm.box = "ubuntu/trusty64"
    web.vm.network "public_network", ip: "10.0.10.60"
    web.vm.provision "shell", inline: $web_script
  end

  config.vm.define "db" do |db|
    db.vm.box = "ubuntu/trusty64"
    db.vm.network "public_network", ip: "10.0.10.61"
    db.vm.provision "shell", inline: $db_script
  end

  config.vm.define "ubuntu" do |ubuntu|
    ubuntu.vm.box = "ubuntu/trusty64"
    ubuntu.vm.network "public_network", ip: "10.0.10.65"
    ubuntu.vm.provision "shell", inline: $ubuntu_script
  end
end
