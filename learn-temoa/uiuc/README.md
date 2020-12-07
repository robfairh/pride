conda activate temoa-py3

rm 01_uiuc.sqlite
sqlite3 01_uiuc.sqlite < 01_uiuc.sql
python $TEMOA/data_processing/MakeGraphviz.py -i 01_uiuc.sqlite
python $TEMOA/temoa_model/ --config=run_scenario01.txt

rm 02_uiuc.sqlite
sqlite3 02_uiuc.sqlite < 02_uiuc.sql
python $TEMOA/data_processing/MakeGraphviz.py -i 02_uiuc.sqlite
python $TEMOA/temoa_model/ --config=run_scenario02.txt

rm 03_uiuc.sqlite
sqlite3 03_uiuc.sqlite < 03_uiuc.sql
python $TEMOA/data_processing/MakeGraphviz.py -i 03_uiuc.sqlite
python $TEMOA/temoa_model/ --config=run_scenario03.txt

rm 04_uiuc.sqlite
sqlite3 04_uiuc.sqlite < 04_uiuc.sql
python $TEMOA/data_processing/MakeGraphviz.py -i 04_uiuc.sqlite
python $TEMOA/temoa_model/ --config=run_scenario04.txt

rm 05_uiuc.sqlite
sqlite3 05_uiuc.sqlite < 05_uiuc.sql
python $TEMOA/data_processing/MakeGraphviz.py -i 05_uiuc.sqlite
python $TEMOA/temoa_model/ --config=run_scenario05.txt

rm 06_uiuc.sqlite
sqlite3 06_uiuc.sqlite < 06_uiuc.sql
python $TEMOA/data_processing/MakeGraphviz.py -i 06_uiuc.sqlite
python $TEMOA/temoa_model/ --config=run_scenario06.txt

rm 07_uiuc.sqlite
sqlite3 07_uiuc.sqlite < 07_uiuc.sql
python $TEMOA/data_processing/MakeGraphviz.py -i 07_uiuc.sqlite
python $TEMOA/temoa_model/ --config=run_scenario07.txt

rm 03_uiuc_mga.sqlite
sqlite3 03_uiuc_mga.sqlite < 03_uiuc_mga.sql
python $TEMOA/data_processing/MakeGraphviz.py -i 03_uiuc_mga.sqlite
python $TEMOA/temoa_model/ --config=run_mga_scenario3.txt

it doesn't run

rm bau_uiuc.sqlite
sqlite3 bau_uiuc.sqlite < bau_uiuc.sql
python $TEMOA/data_processing/MakeGraphviz.py -i bau_uiuc.sqlite
python $TEMOA/temoa_model/ --config=run_bau.txt







* temoa_utopia_old.dat

python $TEMOA/data_processing/MakeGraphviz.py -i temoa_utopia_old.dat
works
python $TEMOA/temoa_model/ temoa_utopia_old.dat
doesn't work

* temoa_utopia.sqlite

python $TEMOA/data_processing/MakeGraphviz.py -i temoa_utopia.sqlite
works
python $TEMOA/temoa_model/ temoa_utopia.sqlite
requests the .dat

python $TEMOA/temoa_model/ --config=config_sample
works
it creates a .dat file

# My input files:

To run model:
python $TEMOA/temoa_model/ utopia-00a.dat

To make the diagrams:
python $TEMOA/data_processing/MakeGraphviz.py -i utopia-00b.dat

# Create .sqlite:

sqlite3 temoa_utopia.sqlite < temoa_utopia.sql

# Plot outputs

python $TEMOA/data_processing/MakeOutputPlots.py -h

python $TEMOA/data_processing/MakeOutputPlots.py -i temoa_utopia.sqlite -r utopia -s test_run -p capacity -c electric --super

# My input files:

utopia-00.sql

rm utopia-00.sqlite
sqlite3 utopia-00.sqlite < utopia-00.sql
python $TEMOA/data_processing/MakeGraphviz.py -i utopia-00.sqlite

python $TEMOA/temoa_model/ --config=config_sample2
python $TEMOA/data_processing/MakeOutputPlots.py -i utopia-00.sqlite -r utopia -s test_run -p capacity -c electric --super

why 2020 is not showing up?
why nuclear is not showing up?

python $TEMOA/data_processing/MakeOutputPlots.py -i utopia-00.sqlite -r utopia -s test_run -p capacity -c electric
python $TEMOA/data_processing/MakeOutputPlots.py -i utopia-00.sqlite -r utopia -s test_run -p flow -c electric
python $TEMOA/data_processing/MakeOutputPlots.py -i utopia-00.sqlite -r utopia -s test_run -p capacity -c transport

python $TEMOA/data_processing/MakeGraphviz.py -i utopia-00.sqlite -s test_run -y 1990
not sure about some of the numbers
the sum of input and sum of outputs for the commodities are equal

python $TEMOA/data_processing/MakeOutputPlots.py -i utopia-00.sqlite -r utopia -s test_run -p emissions -c transport
it doesn't run ...

rm utopia-01.sqlite
sqlite3 utopia-01.sqlite < utopia-01.sql
python $TEMOA/data_processing/MakeGraphviz.py -i utopia-01.sqlite

python $TEMOA/temoa_model/ --config=config_sample3

python $TEMOA/data_processing/MakeGraphviz.py -i utopia-01.sqlite -s test_run -y 1990


python $TEMOA/data_processing/MakeOutputPlots.py -i utopia-01.sqlite -r utopia -s test_run -p emissions -c transport
