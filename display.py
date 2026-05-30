from datetime import datetime
import os


def clear_screen():
    os.system("cls")


def display_metrics(metrics):
    clear_screen()

    print("================================")
    print(" Windows System Monitor")
    print("================================")

    print(f"CPU Usage        : {metrics['cpu_usage']:.1f}%")
    print(f"Memory Usage     : {metrics['mem_usage']:.1f}%")
    print(f"Swap Usage       : {metrics['swap_usage']:.1f}%")
    print(f"Disk Usage (C:)  : {metrics['disk_usage']:.1f}%")

    if metrics["cpu_temp"] is not None:
        print(f"CPU Temperature  : {metrics['cpu_temp']}°C")
    else:
        print("CPU Temperature  : N/A")

    uptime = metrics["uptime"]

    days = uptime // 86400
    hours = (uptime % 86400) // 3600
    minutes = (uptime % 3600) // 60

    print(f"System Uptime    : {days}d {hours}h {minutes}m")

    print()
    print(f"Last Update      : {datetime.now():%Y-%m-%d %H:%M:%S}")
    print("================================")
