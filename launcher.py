import argparse
import ansys.fluent.core as pyfluent
import sys
# Add logging to fluent
pyfluent.logging.enable()

sys.path.insert(0, 'C:/Users/Administrator/PycharmProjects/testANSYS')

parser = argparse.ArgumentParser(
                     prog='FluentLauncer',
                     description='Program to launch fluent simulations through the command line',)


parser.add_argument('--filepath', type=str, action="store", dest="import_filepath",
                       help='the filepath of the .cas.h5 file')
parser.add_argument('--iterations', type=int, action="store", dest="iterations",
                   help='number of iterations for the simulation')
parser.add_argument('--cores', type=int, action="store", dest="cores",
                   help='number of cores for the simulation')
parser.add_argument('--show_gui', type=bool, action="store", dest="show_gui",
                    help='option to show fluent GUI when launching the simulation')

args = parser.parse_args()
import_filepath=args.import_filepath
iterations=args.iterations
cores=args.cores
show_gui=args.show_gui

solver=pyfluent.launch_fluent(mode="solver", show_gui=show_gui, processor_count=cores)
solver.file.read_case(file_type="case", file_name=import_filepath)

solver.solution.initialization.hybrid_initialize()
#Must be set to 150 iterations or more
solver.solution.run_calculation.iterate()

#./testFluent.py --filepath 'C:/Users/Administrator/Desktop/Fluent/Fluent/FFF-Setup-Output.cas.h5' --iterations 150 --cores 8 --show_gui True








