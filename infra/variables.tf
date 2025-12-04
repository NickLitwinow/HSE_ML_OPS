variable "zone" {
  description = "Зона доступности Yandex Cloud"
  type        = string
  default     = "ru-central1-a"
}

variable "image_id" {
  description = "ID образа для Ubuntu 22.04"
  type        = string
  default     = "fd80mrhj8fl2oe87o4e1" # Ubuntu 22.04 LTS
}

variable "subnet_id" {
  description = "ID подсети"
  type        = string
  # Замените на ваш реальный Subnet ID или передайте через -var
  default     = "e9b0...replace_me..." 
}
