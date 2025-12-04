variable "zone" {
  description = "Yandex Cloud Zone"
  type        = string
  default     = "ru-central1-a"
}

variable "image_id" {
  description = "Image ID for Ubuntu 22.04"
  type        = string
  default     = "fd80mrhj8fl2oe87o4e1" # Ubuntu 22.04 LTS
}

variable "subnet_id" {
  description = "Subnet ID"
  type        = string
  # Replace with your actual Subnet ID or pass via -var
  default     = "e9b0...replace_me..." 
}
