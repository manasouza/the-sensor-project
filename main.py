import light_sensor
import motion_sensor
import temp_pressure_sensor

import click

@click.command()
@click.option('--ldr', help='Number of greetings.')
@click.option('--pir', help='Number of greetings.')
@click.option('--bmp', help='Number of greetings.')
def run(ldr, pir, bmp):
    if ldr:
        light_sensor.get_rc_time()
    elif pir:
        motion_sensor.monitor_motion()
    elif bmp:
        temp_pressure_sensor.get_sensor_values()
    else:
        print('invalid argument')


if __name__ == "__main__":
    run()
