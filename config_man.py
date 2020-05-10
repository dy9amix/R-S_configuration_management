#!./venv/bin/python
""""This is a script automates configuration managaement for the GNS3 production network defined"""
from nornir.plugins.tasks import networking #pylint: disable=import-error
from nornir.plugins.functions.text import print_result #pylint: disable=import-error
from nornir import InitNornir #pylint: disable=import-error


def sw_a_config(task): # pylint: disable=missing-function-docstring

    res_view = task.run(task=networking.napalm_configure,
                        dry_run=False,
                        filename="./IOS_config/SW-1.conf"
                        )
    print_result(res_view.result)

def sw_b_config(task): # pylint: disable=missing-function-docstring

    res_view = task.run(task=networking.napalm_configure,
                        dry_run=True,
                        filename="./IOS_config/SW-2.conf"
                        )
    print_result(res_view.result)

def sw_c_config(task): # pylint: disable=missing-function-docstring

    res_view = task.run(task=networking.napalm_configure,
                        dry_run=True,
                        filename="./IOS_config/SW-3.conf"
                        )
    print_result(res_view.result)

def sw_d_config(task): # pylint: disable=missing-function-docstring

    res_view = task.run(task=networking.napalm_configure,
                        dry_run=True,
                        filename="./IOS_config/SW-4.conf"
                        )
    print_result(res_view.result)

def sw_e_config(task): # pylint: disable=missing-function-docstring

    res_view = task.run(task=networking.napalm_configure,
                        dry_run=True,
                        filename="./IOS_config/SW-5.conf"
                        )
    print_result(res_view.result)


NR = InitNornir(config_file="./config.yaml")

SW_1 = NR.filter(name="SW-1")
SW_2 = NR.filter(name="SW-2")
SW_3 = NR.filter(name="SW-3")
SW_4 = NR.filter(name="SW-4")
SW_5 = NR.filter(name="SW-5")


RESULT_SW_1 = SW_1.run(
    name="Configure Switch SW-1", task=sw_a_config
)

RESULT_SW_2 = SW_2.run(
    name="Configure Switch SW-2", task=sw_b_config
)

RESULT_SW_3 = SW_3.run(
    name="Configure Switch SW-3", task=sw_c_config
)

RESULT_SW_4 = SW_4.run(
    name="Configure Switch SW-4", task=sw_d_config
)

RESULT_SW_5 = SW_5.run(
    name="Configure Switch SW-5", task=sw_e_config
)

print_result(RESULT_SW_1)
print('/n')
print_result(RESULT_SW_2)
print('/n')
print_result(RESULT_SW_3)
print('/n')
print_result(RESULT_SW_4)
print('/n')
print_result(RESULT_SW_5)
