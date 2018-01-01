# Grammar_analyze

- Some algorithms for FL course SPBU:

  - matrix.py
  - glr.py

## Requirements

- Python 3.6

## Input format

```matrix.py``` - Grammar in Homsky normal form

```glr.py``` - Grammar in 'normal' form

### How to run

- Matrix:
  ```
  py matrix.py data/Grammar/*_hom.dot data/Graph/*.dot <res.txt (opional)>
  ```

- GLR:
   ```
   py glr.py data/Grammar/*.dot data/Graph/*.dot <res.txt (optional)>
   ```

### Test

- To test specific algo:

  ```py test.py matrix```
  
  ```py test.py glr```
  
- To test all algorithms:

  ```py test.py all```

