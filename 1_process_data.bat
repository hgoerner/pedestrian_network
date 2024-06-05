@echo off

echo Running modules\processing\distance_to_opnv.py
python modules\processing\distance_to_opnv.py

echo Running modules\processing\distance_to_education.py
python modules\processing\distance_to_education.py

echo Running final calculations

echo Running Varianten\Vorzugsvariante.py
python Varianten\Vorzugsvariante.py

echo Batch execution complete