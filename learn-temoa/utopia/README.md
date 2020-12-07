conda activate temoa-py3

* utopia-15.dat

python $TEMOA/data_processing/MakeGraphviz.py -i utopia-15.dat
doesn't work
python $TEMOA/temoa_model/ utopia-15.dat
works

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
