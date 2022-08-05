import export_do
import export_input
import export_output

def do():
    exp_file_name = export_input.get_path()
    export_do.export(exp_file_name)
    export_output.output(exp_file_name)
