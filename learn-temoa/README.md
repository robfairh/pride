To make the diagrams:
python $TEMOA/data_processing/MakeGraphviz.py -i utopia-15.dat

To run model:
python $TEMOA/temoa_model/ utopia-15.dat


utopia-15.dat

python $TEMOA/data_processing/MakeGraphviz.py -i utopia-15.dat
doesn't work
python $TEMOA/temoa_model/ utopia-15.dat
works

temoa_utopia.dat

python $TEMOA/data_processing/MakeGraphviz.py -i temoa_utopia.dat
works
python $TEMOA/temoa_model/ temoa_utopia.dat
doesn't work

temoa_utopia.sqlite

python $TEMOA/data_processing/MakeGraphviz.py -i temoa_utopia.sqlite
works
python $TEMOA/temoa_model/ temoa_utopia.sqlite
requests the .dat

python $TEMOA/temoa_model/ --config=config_sample
works
it creates the .dat file
don't run it cause I would over write temo_utopia.dat

# CREATE .sqlite:

sqlite3 temoa_utopia.sqlite < temoa_utopia.sql
