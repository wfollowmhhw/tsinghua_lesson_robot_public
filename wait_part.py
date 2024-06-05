import datetime
import time

def wait_to_time(target_time):
    # 计算当前时间到目标时间的秒数差
    delta_seconds = (target_time - datetime.datetime.now()).total_seconds()

    # 如果计算结果是负数，说明目标时间已经是过去的时间
    if delta_seconds < 0:
        print("目标时间已经过去，请提供一个未来的时间点。")
    else:
        # 让程序休眠直到目标时间
        print(f"程序将在 {delta_seconds} 秒后醒来。")
        time.sleep(delta_seconds)
        print("程序已唤醒，现在是目标时间。")