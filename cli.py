import sys

from services import poke_data_collector


def argument_map(arguments = sys.argv[1:]):
    available_args = {
        'legendaries': poke_data_collector.collect_legendaries,
        'starters': poke_data_collector.collect_starter_from_generation
    }


    if len(arguments) < 1:
        raise Exception(f"Please provide an argument to specify the desired action: {available_args}")
    

    option = arguments[0]

    if option not in available_args.keys():
        raise Exception(f"Please provide a valid option: {available_args}")
    
    parameters = arguments[1:]

    if option == 'starters' and len(parameters) == 0:
        raise Exception(f"Please inform the generation number for the starters (from 1 to 5)")

    return (available_args[option], parameters)

    
callable, parameters = argument_map()
result = callable(*parameters)

print(result)