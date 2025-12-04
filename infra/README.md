# Infrastructure Deployment

This directory contains Terraform configuration to deploy a Virtual Machine in Yandex.Cloud.

## Prerequisites
1.  Install Terraform.
2.  Install Yandex Cloud CLI (`yc`).
3.  Authenticate: `yc init`.
4.  Create an SSH key pair: `ssh-keygen -t rsa`.

## Usage

1.  **Initialize Terraform:**
    ```bash
    terraform init
    ```

2.  **Check the plan:**
    You need to provide your `subnet_id`. You can find it in the Yandex Cloud Console or via `yc vpc subnet list`.
    ```bash
    terraform plan -var="subnet_id=<YOUR_SUBNET_ID>"
    ```

3.  **Apply changes:**
    ```bash
    terraform apply -var="subnet_id=<YOUR_SUBNET_ID>"
    ```

4.  **Connect to VM:**
    Use the output IP address:
    ```bash
    ssh ubuntu@<EXTERNAL_IP>
    ```

5.  **Destroy resources:**
    ```bash
    terraform destroy -var="subnet_id=<YOUR_SUBNET_ID>"
    ```
