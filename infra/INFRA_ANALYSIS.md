# Infrastructure Analysis: Terraform vs Ansible

## Scenario: FireWatch.ai Automation

| № | Task | Tool | Reasoning |
|---|---|---|---|
| 1 | Create Folder (Cloud Resource) | **Terraform** | Managing cloud hierarchy (folders, organizations) is a structural infrastructure state best managed by Terraform's state file. |
| 2 | Create VPC and Subnet | **Terraform** | Networking is core infrastructure. Terraform is ideal for defining the topology and dependencies of network resources. |
| 3 | Create Object Storage Bucket | **Terraform** | Storage buckets are persistent infrastructure resources. Terraform ensures they exist with the correct configuration. |
| 4 | Create Virtual Machine | **Terraform** | Provisioning compute resources (VMs) is the primary use case for Terraform (Infrastructure Provisioning). |
| 5 | Configure Security Group | **Terraform** | Security groups are cloud-level network firewalls, tightly coupled with VPCs and VMs, thus part of the infrastructure definition. |
| 6 | Install python3, docker | **Ansible** | Configuration management inside the OS. Ansible excels at package management and ensuring software state on existing servers. |
| 7 | Install uv via pip | **Ansible** | Application-level dependency management. Ansible modules (pip) make this idempotent and easy to manage. |
| 8 | Create user ml-dev | **Ansible** | User management within the OS is a configuration task. Ansible's `user` module is perfect for this. |
| 9 | Copy requirements.txt | **Ansible** | File transfer and deployment of application artifacts to the server are standard Ansible tasks. |
| 10 | Delete Virtual Machine | **Terraform** | Lifecycle management (destruction) of cloud resources is handled by `terraform destroy` or removing the resource from code. |

## Summary
- **Terraform** is used for **Provisioning**: Creating the "skeleton" of the infrastructure (Networks, VMs, Storage, IAM).
- **Ansible** is used for **Configuration**: Setting up the "flesh" inside the servers (Software, Users, Config files).
