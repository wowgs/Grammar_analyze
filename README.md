# Grammar_analyze

- Some algorithms for FL course SPBU:

  - matrix.py
  - glr.py
  - gll.py

## Requirements

- Python 3.6

## Input format

```matrix.py``` - Grammar in Homsky normal form

```glr.py``` - Grammar in graph form

```gll.py``` - Grammar in graph form

### How to run

- Matrix:
  ```
  python matrix.py data/Grammar/*_hom.dot data/Graph/*.dot <res.txt (opional)>
  ```

- GLR:
   ```
   python glr.py data/Grammar/*_auto.dot data/Graph/*.dot <res.txt (optional)>
   ```
   
- GLL:
   ```
   python gll.py data/Grammar/*_auto.dot data/Graph/*.dot <res.txt (optional)>
   ```

### Test

- To test specific algo:

  ```python test.py matrix```
  
  ```python test.py glr```
  
  ```python test.py gll```
  
- To test all algorithms with ALL tests:

  ```py test.py all```
  
   - Approximate time ~2.5 minutes for all
  
- To test all algorithms with SMALL tests:

  ```py test.py small```

