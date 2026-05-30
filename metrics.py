import psutil
import time

_prev_cpu_time = None


def get_cpu_usage():
    return psutil.cpu_percent(interval=None)


def get_memory_usage():
    mem = psutil.virtual_memory()
    swap = psutil.swap_memory()

    return mem.percent, swap.percent


def get_disk_usage():
    return psutil.disk_usage("C:\\").percent


def get_cpu_temp():
    try:
        temps = psutil.sensors_temperatures()

        if not temps:
            return None

        for sensor_list in temps.values():
            for sensor in sensor_list:
                if sensor.current:
                    return round(sensor.current)

    except Exception:
        pass

    return None


def get_uptime():
    return int(time.time() - psutil.boot_time())


def collect_metrics():
    mem_usage, swap_usage = get_memory_usage()

    return {
        "cpu_usage": get_cpu_usage(),
        "mem_usage": mem_usage,
        "swap_usage": swap_usage,
        "disk_usage": get_disk_usage(),
        "cpu_temp": get_cpu_temp(),
        "uptime": get_uptime(),
    }
