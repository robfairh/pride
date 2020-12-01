
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

# Input files:

To run model:
python $TEMOA/temoa_model/ utopia-00a.dat

To make the diagrams:
python $TEMOA/data_processing/MakeGraphviz.py -i utopia-00b.dat

# Create .sqlite:

sqlite3 temoa_utopia.sqlite < temoa_utopia.sql

# Plot outputs

python $TEMOA/data_processing/MakeOutputPlots.py -h

python $TEMOA/data_processing/MakeOutputPlots.py -i temoa_utopia.sqlite -r utopia -s test_run -p capacity -c electric --super

outputs from ran .sqlite


python $TEMOA/data_processing/MakeOutputPlots.py -i utopia-00.sqlite -r utopia -s test_run -p capacity -c electric --super

# Input files:

utopia-00.sql

rm utopia-00.sqlite
sqlite3 utopia-00.sqlite < utopia-00.sql
python $TEMOA/temoa_model/ --config=config_sample2
python $TEMOA/data_processing/MakeOutputPlots.py -i utopia-00.sqlite -r utopia -s test_run -p capacity -c electric --super