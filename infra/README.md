# Развертывание Инфраструктуры

В этой директории находится конфигурация Terraform для развертывания Виртуальной Машины в Yandex.Cloud.

## Предварительные требования
1.  Установите Terraform.
2.  Установите Yandex Cloud CLI (`yc`).
3.  Аутентификация: `yc init`.
4.  Создайте пару SSH-ключей: `ssh-keygen -t rsa`.

## Использование

1.  **Инициализация Terraform:**
    ```bash
    terraform init
    ```

2.  **Проверка плана:**
    Вам нужно указать ваш `subnet_id`. Вы можете найти его в консоли Yandex Cloud или через `yc vpc subnet list`.
    ```bash
    terraform plan -var="subnet_id=<ВАШ_SUBNET_ID>"
    ```

3.  **Применение изменений:**
    ```bash
    terraform apply -var="subnet_id=<ВАШ_SUBNET_ID>"
    ```

4.  **Подключение к VM:**
    Используйте IP-адрес из вывода команды:
    ```bash
    ssh ubuntu@<EXTERNAL_IP>
    ```

5.  **Удаление ресурсов:**
    ```bash
    terraform destroy -var="subnet_id=<ВАШ_SUBNET_ID>"
    ```
