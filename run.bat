@echo off
For /d/r %%G IN (script.py) do IF EXIST %%G python %%G
