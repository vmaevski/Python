import import_input
import import_output
import import_do

def do():
    imp_file_name = import_input.get_file_name()
    import_do.import_do(imp_file_name)
    import_output.output(imp_file_name)