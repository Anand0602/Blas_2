# BLAS_2 Matrix-Vector Operations

This Python code provides a class `BLAS_2` for performing various matrix-vector operations, including matrix-vector multiplication, symmetric matrix-vector multiplication, triangular matrix-vector multiplication, and more.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [How to Use](#how-to-use)
- [Examples](#examples)
- [License](#license)

## Introduction

This Python code defines a class `BLAS_2` that allows users to perform common linear algebra operations involving matrices and vectors. It includes functionality for both regular and symmetric matrices and supports operations with single and double precision.

## Features

- Matrix-vector multiplication
- Symmetric matrix-vector multiplication
- Triangular matrix-vector multiplication
- Triangular banded matrix-vector multiplication
- Rank-1 operation
- Symmetric rank-1 operation
- Symmetric rank-2 operation
- Support for single and double precision
- User-friendly input prompts

## How to Use

1. Import the `numpy` library:

   ```python
   import numpy as np


Create an instance of the BLAS_2 class by specifying the number of rows, columns, alpha value, and matrix A:
blas = BLAS_2(rows, cols, alpha, A)


Matrix-Vector Multiplication
```python
blas.matrix_vector()
```

Symmetric Matrix-Vector Multiplication
```python
blas.symmetric_matrix_vector()
```

Triangular Matrix-Vector Multiplication
```python
blas.triangular_matrix_vector()
```

Triangular Banded Matrix-Vector Multiplication
```python
blas.triangular_banded_matrix_vector()
```

Rank-1 Operation
```python
blas.Rank_1_operation()
```

Symmetric Rank-1 Operation
```python
blas.symmetric_rank1_operation()
```

Symmetric Rank-2 Operation
```python
blas.symmetric_rank2_operation()
```
