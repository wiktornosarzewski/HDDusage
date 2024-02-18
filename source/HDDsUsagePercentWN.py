import psutil
#by Wiktor Nosarzewski 18.02.2024
def get_disk_usage_percentage(disk_letter):
    try:
        disk_usage = psutil.disk_usage(disk_letter + ":")
        return disk_usage.percent
    except Exception as e:
        print(f"Error while getting disk usage for {disk_letter}: {e}")
        return None

def main():
    disks = ["C", "D", "G"]
    for disk in disks:
        usage_percentage = get_disk_usage_percentage(disk)
        if usage_percentage is not None:
            print(f"Disk {disk}: {usage_percentage:.2f}% used")

if __name__ == "__main__":
    main()
    input()
