import argparse
from settings.settings import settings

class Parser():
    # With the current implementation it would not be possible to change the log path using the command line.
    # If this would be needed, move the parser above the log declaration in calculate.py/export.py.
    # This however will not allow the parser to log anything.
    def __init__(self):
        self.parser = argparse.ArgumentParser(
                            prog='Metashape Helper',
                            description='Export or calculate the metashape files')


        # use_tweaks override
        self.parser.add_argument('--use_tweaks', type=str, required=False)

        # calculation_input_folder_path override
        self.parser.add_argument('--calculation_input_folder_path', type=str, required=False)

        # show_finished_message override
        self.parser.add_argument('--show_finished_message', type=str, required=False)

    # Helper function for boolean arguments
    def handle_boolean(self, string):
        if string.lower() == 'true':
            return True
        elif string.lower() == 'false':
            return False
        else:
            raise ValueError('Invalid boolean type! Use True or False')

    # Handle the command line arguments
    def handle_args(self, logger):
        logger.log("Handling command line arguments...")
        args = self.parser.parse_args()
        if args.use_tweaks:
            settings.set('use_tweaks', self.handle_boolean(args.use_tweaks))
            logger.log(f"   Changed use_tweaks to {settings.get('use_tweaks')}")
        if args.calculation_input_folder_path:
            settings.set('calculation_input_folder_path', args.calculation_input_folder_path)
            logger.log(f"   Changed calculation_input_folder_path to {settings.get('calculation_input_folder_path')}")
        if args.show_finished_message:
            settings.set('show_finished_message', self.handle_boolean(args.show_finished_message))
            logger.log(f"   Changed show_finished_message to {settings.get('show_finished_message')}")


parser = Parser()
