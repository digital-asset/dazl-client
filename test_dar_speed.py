#!/usr/bin/env python3
import cProfile
from pathlib import Path
import time

from dazl.damlast import DarFile

p = Path(".") / "_fixtures" / "archives" / "1.16.0" / "Test.dar"

def parse_file():
 dar_file = DarFile(p)
 start_time = time.time()
 archives = dar_file.archives()
 end_time = time.time()
 print(end_time - start_time)

parse_file()

cProfile.run('parse_file()')
